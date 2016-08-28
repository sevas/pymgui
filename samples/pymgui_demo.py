import pymgui
import os

import matplotlib.pyplot as plt
plt.set_cmap('viridis')


def main():
    io = pymgui.get_io()
    io.render_draw_list_func = pymgui.types.stub_render

    font_atlas = io.fonts
    font_atlas_texture = pymgui.get_tex_data_as_rgba32(font_atlas)

    io.display_size = (640, 480)

    x = io.mouse_drag_threshold

    clear_color = pymgui.ImColor(114, 144, 154, 255)
    button_size = pymgui.ImVec2(30,50)
    show_second_window = 0

    while True:
        f = 0.0
        pid = os.getpid()
        pymgui.new_frame()

        pymgui.begin("hello", True)

        pymgui.button("hello button", (20, 50))
        pymgui.button("hello button 2", (20, 60))

        pymgui.end()

        if show_second_window % 2 == 0:
            pymgui.begin("hello2", True)
            pymgui.button("hello", (45, 90))
            pymgui.end()

        pymgui.render()


if __name__ == '__main__':
    main()
