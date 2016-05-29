from . import _cimgui
from . import types

ffi = _cimgui.ffi
C = _cimgui.C

# // Window
# bool             igBegin(const char* name, bool* p_opened, ImGuiWindowFlags flags);
# bool             igBegin2(const char* name, bool* p_opened, const struct ImVec2 size_on_first_use, float bg_alpha, ImGuiWindowFlags flags);
# void             igEnd();
# bool             igBeginChild(const char* str_id, const struct ImVec2 size, bool border, ImGuiWindowFlags extra_flags);
# bool             igBeginChildEx(ImGuiID id, const struct ImVec2 size, bool border, ImGuiWindowFlags extra_flags);
# void             igEndChild();
# void             igGetContentRegionMax(struct ImVec2* out);
# void             igGetContentRegionAvail(struct ImVec2* out);
# float            igGetContentRegionAvailWidth();
# void             igGetWindowContentRegionMin(struct ImVec2* out);
# void             igGetWindowContentRegionMax(struct ImVec2* out);
# float            igGetWindowContentRegionWidth();
# ImDrawList*      igGetWindowDrawList();
# void             igGetWindowPos(struct ImVec2* out);
# void             igGetWindowSize(struct ImVec2* out);
# float            igGetWindowWidth();
# float            igGetWindowHeight();
# bool             igIsWindowCollapsed();
# void             igSetWindowFontScale(float scale);


def begin(name, opened, flags=0):
    s = ffi.new("const char[]", bytes(name, 'ascii'))
    b = ffi.new("bool*", opened)
    C.igBegin(s, b, flags)


def end():
    _cimgui.C.end()
