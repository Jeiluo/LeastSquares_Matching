cmake_minimum_required(VERSION 3.12)
project(LEASTSQUARES_MATCHING)

if(CMAKE_COMPILER_IS_GNUCXX)
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DWIN32 -D_WINDOWS -W3")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DWIN32 -D_WINDOWS -W3")
endif()
set(OPENCV_FORCE_DISABLED_OPTIMIZATIONS ON CACHE BOOL "Disable compiler optimizations")

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 14)

# 设置 OpenCV 源代码路径（假设你将 OpenCV 源代码放在项目目录的 opencv 子目录下）
set(OpenCV_DIR "${CMAKE_SOURCE_DIR}/third_party/opencv")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# 创建你的可执行文件
add_executable(leastsquares_matching
                core/src/matching.cpp
                core/src/test.cpp
                )

# 链接 OpenCV 库
target_link_libraries(leastsquares_matching ${OpenCV_LIBS})

# 设置编译时 OpenCV 头文件路径
target_include_directories(leastsquares_matching PRIVATE
                            ${CMAKE_SOURCE_DIR}/core/include
                            )