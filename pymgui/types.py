from ._cimgui import ffi


def ImVec2(x=0.0, y=0.0):
    out = ffi.new("ImVec2*")
    out.x = float(x)
    out.y = float(y)
    return out


def ImVec4(x=0.0, y=0.0, z=0.0, w=0.0):
    out = ffi.new("ImVec4*")
    out.x = float(x)
    out.y = float(y)
    out.z = float(z)
    out.w = float(w)
    return out


class ImColor(object):
    def __init__(self, r=0, g=0, b=0, a=255):
        scale = 1.0 / 255.0
        self._value = ImVec4(r*scale, g*scale, b*scale, a*scale)

    @classmethod
    def from_ImVec4(cls, vec4):
        value = ImVec4(vec4.x, vec4.y, vec4.z, vec4.w)
        color = cls()
        color._value = value
        return color

    def rgba(self):
        scale = 255.0
        return tuple([int(self._value.x * scale), int(self._value.y * scale), int(self._value.z * scale), int(self._value.w * scale)])


class IO(object):
    def __init__(self, io):
        self._io = io

    @property
    def display_size(self):
        return self._io.DisplaySize

    @display_size.setter
    def display_size(self, value):
        if isinstance(value, tuple):
            value = ImVec2(*value)
        self._io.DisplaySize = value

    @property
    def delta_time(self):
        return self._io.DeltaTime

    @property
    def fonts(self):
        return self._io.Fonts
