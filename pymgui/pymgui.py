from . import _cimgui
from .types import IO

ffi = _cimgui.ffi
C = _cimgui.C


#
# ImGuiIO*         igGetIO();
# ImGuiStyle*      igGetStyle();
# ImDrawData*      igGetDrawData();
# void             igNewFrame();
# void             igRender();
# void             igShutdown();
# void             igShowUserGuide();
# void             igShowStyleEditor(ImGuiStyle* ref);
# void             igShowTestWindow(bool* opened);
# void             igShowMetricsWindow(bool* opened);


def get_io():
    io = C.igGetIO()
    return IO(io)


def new_frame():
    C.igNewFrame()


def render():
    C.igRender()
