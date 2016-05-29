import pymgui
from pymgui._cimgui import ffi
import os

@ffi.callback("void (ImDrawData*)")
def render(draw_data):
    print(draw_data)


def main():
    io = pymgui.get_io()
    io._io.RenderDrawListsFn = render

    font_atlas = io.fonts
    out = pymgui.get_tex_data_as_rgba32(font_atlas)

    size = pymgui.ImVec2(640, 480)
    io.DisplaySize = size

    clear_color = pymgui.ImColor(114, 144, 154, 255)
    button_size = pymgui.ImVec2(30,50)

    while True:
        f = 0.0
        pid = os.getpid()
        pymgui.new_frame()
        pymgui.begin("hello", True)

        pymgui.button("hello button", (20, 50))

        pymgui.render()


if __name__ == '__main__':
    main()
