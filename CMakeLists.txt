project(pymgui)
cmake_minimum_required(VERSION 3.3)
project(pymgui)

file(MAKE_DIRECTORY ${CMAKE_SOURCE_DIR}/_outputs/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/_outputs/bin)

set(CMAKE_DEBUG_POSTFIX d)

add_subdirectory(deps)
add_subdirectory(samples/cimgui_app)
