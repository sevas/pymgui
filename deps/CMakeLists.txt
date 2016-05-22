

# ------------------------------------------------------------------------------
# Source files
# ------------------------------------------------------------------------------
set(imgui_DIR ${CMAKE_CURRENT_SOURCE_DIR}/cimgui/imgui)
set(cimgui_DIR ${CMAKE_CURRENT_SOURCE_DIR}/cimgui/cimgui)


set(cimgui_HEADER_FILES
	${cimgui_DIR}/cimgui.h
)

set(cimgui_SOURCE_FILES
	${cimgui_DIR}/cimgui.cpp
	${cimgui_DIR}/drawList.cpp
	${cimgui_DIR}/fontAtlas.cpp
)


set(imgui_SOURCE_FILES
	${imgui_DIR}/imgui_internal.h
	${imgui_DIR}/imgui.h
	${imgui_DIR}/imgui.cpp
	${imgui_DIR}/imgui_draw.cpp
	${imgui_DIR}/imgui_demo.cpp)




source_group("cimgui" FILES ${cimgui_HEADER_FILES} ${cimgui_SOURCE_FILES})
source_group("deps\\imgui" FILES ${imgui_SOURCE_FILES})


# ------------------------------------------------------------------------------
# Targets
# ------------------------------------------------------------------------------
add_library(cimgui SHARED
	${imgui_SOURCE_FILES}
	${imgui_gl2_backend_SOURCE_FILES}
	${cimgui_SOURCE_FILES}
	${cimgui_HEADER_FILES})

target_link_libraries(cimgui PUBLIC ${glfw_LIBRARIES} opengl32.lib)

target_include_directories(cimgui
	PUBLIC
		$<BUILD_INTERFACE:${cimgui_DIR}>
		$<BUILD_INTERFACE:${glfw_INCLUDE_DIRS}>
		$<BUILD_INTERFACE:${imgui_gl2_backend_DIR}>
		$<BUILD_INTERFACE:${cimgui_types_DIR}>
	PRIVATE
		${imgui_DIR}
		${cimgui_types_DIR})

target_compile_definitions(cimgui PUBLIC _MBCS PRIVATE CIMGUI_EXPORTS _USRDLL)

if(MSVC)
	target_compile_options(cimgui PRIVATE $<$<CONFIG:Release>:/GL /Oi>)
endif()

set(pymgui_DIR ${CMAKE_SOURCE_DIR}/pymgui/_dlls)
if(NOT EXISTS ${pymgui_DIR})
	file(MAKE_DIRECTORY ${pymgui_DIR})
endif()

add_custom_command(TARGET cimgui POST_BUILD
	COMMAND ${CMAKE_COMMAND} -E copy_if_different $<TARGET_FILE:cimgui> ${pymgui_DIR}
	COMMAND ${CMAKE_COMMAND} -E copy_if_different $<TARGET_PDB_FILE:cimgui> ${pymgui_DIR})
