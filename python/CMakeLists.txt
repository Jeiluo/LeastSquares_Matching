cmake_minimum_required(VERSION 3.12)
project(lsmatching)

set(CMAKE_CXX_STANDARD 14)

set(OpenCV_DIR "../build/opencv_install")
find_package(OpenCV REQUIRED)

add_subdirectory("../third_party/pybind11" pybind11_build)

pybind11_add_module(lsmatching
    bindings.cpp
    ../core/src/matching.cpp
    ../core/src/matrix.cpp
    ../core/src/tools.cpp
)

target_include_directories(lsmatching PRIVATE
    ../core/include
    ${OpenCV_INCLUDE_DIRS}
)

target_link_libraries(lsmatching PRIVATE ${OpenCV_LIBS})

install(TARGETS lsmatching
        LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX})

if(WIN32)
    message(STATUS "Windows detected, ensure MinGW in PATH")
endif()