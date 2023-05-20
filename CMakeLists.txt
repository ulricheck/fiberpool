cmake_minimum_required(VERSION 3.10)

set(PROJECT_NAME
        fiberexample)

project(${PROJECT_NAME})

find_package(Boost REQUIRED COMPONENTS fiber thread)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE Debug)

find_package(Boost REQUIRED
    COMPONENTS fiber)

add_executable(
    ${PROJECT_NAME}
        examples/main.cpp)

target_link_libraries(${PROJECT_NAME}
    PRIVATE 
        Boost::fiber 
        Boost::thread
        )

IF(UNIX)
target_link_libraries(${PROJECT_NAME}
    PRIVATE 
        pthread)
ENDIF()

include(CTest)

if (BUILD_TESTING)
    enable_testing()
    add_subdirectory(tests)
endif()

