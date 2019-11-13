cmake_minimum_required(VERSION 3.10)

set(PROJECT_NAME
        fiberexample)

project(${PROJECT_NAME})

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE Debug)

find_package(Boost REQUIRED
    COMPONENTS fiber)

add_executable(
    ${PROJECT_NAME}
        examples/main.cpp)

target_link_libraries(${PROJECT_NAME}
    PRIVATE 
        CONAN_PKG::Boost
        pthread)

include(CTest)

if (BUILD_TESTING)
    enable_testing()
    add_subdirectory(tests)
endif()

