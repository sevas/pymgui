


# ------------------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------------------
set(glfw_DIR ${CMAKE_SOURCE_DIR}/deps/glfw-3.1.2/dist)
set(glfw_INCLUDE_DIRS ${glfw_DIR}/include)
set(glfw_LIBRARIES ${glfw_DIR}/lib/x64_vs2015/glfw3.lib)

set(cimgui_DIR ${CMAKE_SOURCE_DIR}/deps/cimgui)

set(cimgui_INCLUDE_DIRS ${cimgui_DIR}/cimgui)
set(imgui_INCLUDE_DIRS ${cimgui_DIR}/imgui)


set(imgui_gl2_backend_DIR ${cimgui_DIR}/imgui/examples/opengl_example)
set(imgui_gl2_backend_SOURCE_FILES
    ${imgui_gl2_backend_DIR}/imgui_impl_glfw.h
    ${imgui_gl2_backend_DIR}/imgui_impl_glfw.cpp)

source_group("deps\\imgui_gl2" FILES ${imgui_gl2_backend_SOURCE_FILES})



set(cimgui_types_DIR ${CMAKE_SOURCE_DIR}/cimgui_types)
set(cimgui_types_SOURCE_FILES
	${cimgui_types_DIR}/cimgui/cimgui_types.h
)

source_group("cimgui_types" FILES ${cimgui_types_SOURCE_FILES})


set(cimgui_demo_app_SOURCE_FILES
	${CMAKE_CURRENT_SOURCE_DIR}/main.cpp
	)

source_group("" FILES ${cimgui_demo_app_SOURCE_FILES})

# ------------------------------------------------------------------------------
# Target
# ------------------------------------------------------------------------------
add_executable(cimgui_app
	${imgui_gl2_backend_SOURCE_FILES}
	${cimgui_types_SOURCE_FILES}
		${cimgui_demo_app_SOURCE_FILES})


target_include_directories(cimgui_app
	PRIVATE
		${cimgui_types_DIR}
		${imgui_gl2_backend_DIR}
		${cimgui_INCLUDE_DIRS}
		${imgui_INCLUDE_DIRS}
		${glfw_INCLUDE_DIRS})

target_link_libraries(cimgui_app PRIVATE cimgui ${glfw_LIBRARIES})


# ------------------------------------------------------------------------------
# Workspace setup
# ------------------------------------------------------------------------------
configure_file(${CMAKE_SOURCE_DIR}/cmake/generic.in.vcxproj.user ${CMAKE_CURRENT_BINARY_DIR}/cimgui_app.vcxproj.user @ONLY WIN32)
