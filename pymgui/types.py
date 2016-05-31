from ._cimgui import ffi, C
from collections import namedtuple


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
        self._io.DisplaySize.x = value.x
        self._io.DisplaySize.y = value.y

    @property
    def delta_time(self):
        return self._io.DeltaTime

    @property
    def fonts(self):
        return self._io.Fonts

CommandList = namedtuple("CommandList", 'cdata_ptr command_list_count')


class ImDrawData(object):
    def __init__(self, c_im_draw_data):
        self._im_draw_data = c_im_draw_data

    @property
    def valid(self):
        """bool: whether or not the draw data is valid

        Only valid after Render() is called and before the next NewFrame() is called.
        """
        return self._im_draw_data[0].Valid

    @property
    def cmd_lists(self):
        """<CData ImDrawLists**>: pointer to the list of draw commands to render

        Consider this an opaque pointer to pass to the ImDrawList_* collection of functions
        """
        return self._im_draw_data[0].CmdLists

    def cmd_lists_count(self):
        """int: number of commands in the """
        return self._im_draw_data[0].CmdListsCount

    @property
    def total_vertex_count(self):
        """int: sum of all cmd_lists vtx_buffer.Size"""
        return self._im_draw_data[0].TotalVtxCount

    @property
    def total_index_count(self):
        """int: sum of all cmd_lists idx_buffer.Size"""
        return self._im_draw_data[0].TotalIdxCount



# class ImDrawList(object):
#     def __init__(self, cdata_draw_list):
#         self._cmd_lists = cdata_draw_list
#
#     def _parse_cmd_lists(self):
#
