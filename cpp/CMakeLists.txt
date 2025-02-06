cmake_minimum_required(VERSION 3.16)
project(steganography-lsb VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)
find_package(OpenCV REQUIRED)

if(WIN32)
    add_executable(${PROJECT_NAME} WIN32
        src/main.cpp
        src/mainWindow.cpp
        src/prestige.cpp
        include/mainWindow.hpp
        include/prestige.hpp
    )
else()
    add_executable(${PROJECT_NAME}
        src/main.cpp
        src/mainWindow.cpp
        src/prestige.cpp
        include/mainWindow.hpp
        include/prestige.hpp
    )
endif()

target_include_directories(${PROJECT_NAME} PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME} PRIVATE
    Qt6::Widgets
    ${OpenCV_LIBS}
) 