set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
cmake_minimum_required(VERSION 3.12)
project(LEASTSQUARES_MATCHING)

set(CMAKE_CXX_STANDARD 14)

if(MINGW)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DWIN32 -D_WINDOWS")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DWIN32 -D_WINDOWS")
endif()

if(WIN32)
    set(PARALLEL_JOBS "")
else()
    set(PARALLEL_JOBS "-- -j8")
endif()

set(OPENCV_INSTALL_DIR "${CMAKE_BINARY_DIR}/opencv_install")
set(OpenCV_DIR "${OPENCV_INSTALL_DIR}")

if(NOT EXISTS "${OPENCV_INSTALL_DIR}/OpenCVConfig.cmake")
    message(STATUS "OpenCV not found, building from source...")

    set(OPENCV_BUILD_DIR "${CMAKE_BINARY_DIR}/opencv_build")

    execute_process(
    COMMAND ${CMAKE_COMMAND} -S ${CMAKE_SOURCE_DIR}/third_party/src/opencv
            -B ${OPENCV_BUILD_DIR}
            -G "MinGW Makefiles"
            -D CMAKE_BUILD_TYPE=Release
            -D CMAKE_INSTALL_PREFIX=${OPENCV_INSTALL_DIR}
            -D BUILD_EXAMPLES=OFF
            -D BUILD_TESTS=OFF
            -D BUILD_DOCS=OFF
            -D BUILD_opencv_videoio=OFF
            -D WITH_FFMPEG=OFF
    RESULT_VARIABLE ret
)
    if(NOT ret EQUAL 0)
        message(FATAL_ERROR "Failed to configure OpenCV")
    endif()

    execute_process(
        COMMAND ${CMAKE_COMMAND} --build ${OPENCV_BUILD_DIR} --target install ${PARALLEL_JOBS}
        RESULT_VARIABLE ret
    )
    if(NOT ret EQUAL 0)
        message(FATAL_ERROR "Failed to build OpenCV")
    endif()
endif()

find_package(OpenCV REQUIRED)

add_executable(leastsquares_matching
    core/src/matching.cpp
    core/src/test.cpp
    core/src/matrix.cpp
    core/src/tools.cpp
    core/src/Correlation.cpp
    core/src/Extract.cpp
)

target_link_libraries(leastsquares_matching PRIVATE ${OpenCV_LIBS})

target_include_directories(leastsquares_matching PRIVATE
    ${CMAKE_SOURCE_DIR}/core/include
)

if(WIN32)
    foreach(lib ${OpenCV_LIBS})
        get_target_property(lib_path ${lib} LOCATION)
        add_custom_command(TARGET leastsquares_matching POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${lib_path}" $<TARGET_FILE_DIR:leastsquares_matching>
        )
    endforeach()
endif()

if(UNIX AND NOT APPLE)
    set_target_properties(leastsquares_matching PROPERTIES
        BUILD_RPATH "${OpenCV_LIB_DIR}"
        INSTALL_RPATH "${OpenCV_LIB_DIR}"
    )
endif()