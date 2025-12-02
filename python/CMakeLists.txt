cmake_minimum_required(VERSION 3.12)
project(lsmatching)

set(CMAKE_CXX_STANDARD 14)

set(OpenCV_DIR "../build/opencv_install")
find_package(OpenCV REQUIRED)

add_subdirectory("../third_party/pybind11" pybind11_build)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static-libgcc -static-libstdc++")

pybind11_add_module(_lsmatching
    bindings.cpp
    ../core/src/matching.cpp
    ../core/src/matrix.cpp
    ../core/src/tools.cpp
    ../core/src/Correlation.cpp
    ../core/src/Extract.cpp
)

target_include_directories(_lsmatching PRIVATE
    ../core/include
    ${OpenCV_INCLUDE_DIRS}
)

target_link_libraries(_lsmatching PRIVATE ${OpenCV_LIBS})

install(TARGETS _lsmatching
        LIBRARY DESTINATION "${CMAKE_INSTALL_PREFIX}/lsmatching")

# 安装 __init__.py
install(FILES ./package/__init__.py
        DESTINATION "${CMAKE_INSTALL_PREFIX}/lsmatching")

if(WIN32)
    install(DIRECTORY ../build/opencv_install/x64/mingw/bin/
        DESTINATION "${CMAKE_INSTALL_PREFIX}/lsmatching"
        FILES_MATCHING PATTERN "*.dll"
        )
endif()

if(WIN32)
    message(STATUS "Windows detected, ensure MinGW in PATH")
endif()