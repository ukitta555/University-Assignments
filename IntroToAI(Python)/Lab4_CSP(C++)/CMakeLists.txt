cmake_minimum_required(VERSION 3.15)
project(class_scheduling_csp)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

add_executable(class_scheduling_csp main.cpp src/CSP.cpp src/Classes.cpp)