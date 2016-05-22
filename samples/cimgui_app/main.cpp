// ImGui - standalone example application for Glfw + OpenGL 2, using fixed pipeline
// If you are new to ImGui, see examples/README.txt and documentation at the top of imgui.cpp.


#include <cimgui/cimgui_types.h>
#include <cimgui.h>


#include <stdio.h>
#include <GLFW/glfw3.h>
#include "imgui_impl_glfw.h"


static void error_callback(int error, const char* description)
{
	fprintf(stderr, "Error %d: %s\n", error, description);
}

int main(int, char**)
{
	// Setup window
	glfwSetErrorCallback(error_callback);
	if (!glfwInit())
		return 1;
	GLFWwindow* window = glfwCreateWindow(1280, 720, "ImGui OpenGL2 example", NULL, NULL);
	glfwMakeContextCurrent(window);
	int w, h;
	glfwGetWindowSize(window, &w, &h);
	// Setup ImGui binding

	ImGui_ImplGlfw_Init(window, true);

	// Load Fonts
	// (there is a default font, this is only if you want to change it. see extra_fonts/README.txt for more details)
	//ImGuiIO& io = ImGui::GetIO();
	//io.Fonts->AddFontDefault();
	//io.Fonts->AddFontFromFileTTF("../../extra_fonts/Cousine-Regular.ttf", 15.0f);
	//io.Fonts->AddFontFromFileTTF("../../extra_fonts/DroidSans.ttf", 16.0f);
	//io.Fonts->AddFontFromFileTTF("../../extra_fonts/ProggyClean.ttf", 13.0f);
	//io.Fonts->AddFontFromFileTTF("../../extra_fonts/ProggyTiny.ttf", 10.0f);
	//io.Fonts->AddFontFromFileTTF("c:\\Windows\\Fonts\\ArialUni.ttf", 18.0f, NULL, io.Fonts->GetGlyphRangesJapanese());

	bool show_test_window = true;
	bool show_another_window = false;
	//ImVec4 clear_color = ImColor(114, 144, 154);
	float clear_color[3] = { 114.f/255, 144.f/255, 154.f/255};


	// Main loop
	while (!glfwWindowShouldClose(window))
	{
		glfwPollEvents();
		ImGui_ImplGlfw_NewFrame();

		// 1. Show a simple window
		// Tip: if we don't call ImGui::Begin()/ImGui::End() the widgets appears in a window automatically called "Debug"
		{
			static float f = 0.0f;
			igText("Hello, world");
			igSliderFloat("float", &f, 0.f, 1.f, ".3f", 1.f);

			igColorEdit3("clear color", &clear_color[0]);


//			ImGui::Text("Hello, world!");
//			ImGui::SliderFloat("float", &f, 0.0f, 1.0f);
//			ImGui::ColorEdit3("clear color", (float*)&clear_color);
//			if (ImGui::Button("Test Window")) show_test_window ^= 1;
//			if (ImGui::Button("Another Window")) show_another_window ^= 1;
//			ImGui::Text("Application average %.3f ms/frame (%.1f FPS)", 1000.0f / ImGui::GetIO().Framerate, ImGui::GetIO().Framerate);
		}

		//// 2. Show another simple window, this time using an explicit Begin/End pair
		//if (show_another_window)
		//{
		//	ImGui::SetNextWindowSize(ImVec2(200, 100), ImGuiSetCond_FirstUseEver);
		//	ImGui::Begin("Another Window", &show_another_window);
		//	ImGui::Text("Hello");
		//	ImGui::End();
		//}

		//// 3. Show the ImGui test window. Most of the sample code is in ImGui::ShowTestWindow()
		//if (show_test_window)
		//{
		//	ImGui::SetNextWindowPos(ImVec2(650, 20), ImGuiSetCond_FirstUseEver);
		//	ImGui::ShowTestWindow(&show_test_window);
		//}

		// Rendering
		int display_w, display_h;
		glfwGetFramebufferSize(window, &display_w, &display_h);
		glViewport(0, 0, display_w, display_h);
		//glClearColor(clear_color.x, clear_color.y, clear_color.z, clear_color.w);
		glClearColor(clear_color[0], clear_color[1], clear_color[2], 1.f);
		glClear(GL_COLOR_BUFFER_BIT);
		//ImGui::Render();
		igRender();
		glfwSwapBuffers(window);
	}

	// Cleanup
	ImGui_ImplGlfw_Shutdown();
	glfwTerminate();

	return 0;
}
