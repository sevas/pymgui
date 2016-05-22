import pymgui
from pymgui._cimgui import ffi
import os

@ffi.callback("void (ImDrawData*)")
def render(draw_data):
    print(draw_data)


def main():
    io = pymgui.C.igGetIO()
    io.RenderDrawListsFn = render

    size = pymgui.ImVec2(640, 480)
    io.DisplaySize.x = size.x
    io.DisplaySize.y = size.y

    clear_color = pymgui.ImColor(114, 144, 154, 255)
    button_size = pymgui.ImVec2(30,50)

    while True:
        f = 0.0
        pid = os.getpid()
        s = ffi.new("const char[]", b"hello world")
        pymgui.C.igButton(s, (20, 50))
        # pymgui.C.igSliderFloat("float",  f, 0., 1., ".3f", 1.)

        # pymgui.C.igColorEdit3("clear color", clear_color)

        pymgui.C.igRender()


if __name__ == '__main__':
    main()
