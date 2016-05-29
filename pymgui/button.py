from . import _cimgui
from . import types


def button(name, size):
    s = _cimgui.ffi.new("const char[]", b"hello world")
    return _cimgui.C.igButton(s, (20, 50))
