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
        return (int(self._value.x * scale),
                int(self._value.y * scale),
                int(self._value.z * scale),
                int(self._value.w * scale))


@ffi.callback("void (ImDrawData*)")
def stub_render(draw_data):
    d = ImDrawData(draw_data)
    print("valid?        {}".format(d.valid))
    print("vertex_count: {}".format(d.total_vertex_count))
    print("index_count:  {}".format(d.total_index_count))
    cmds = d.cmd_lists


class IO(object):
    """Python interface to an ImGuiIO C struct

    That C struct contains the state of the global ImGui instance, such as:

    - the window size
    - the path to log and configuration files
    - the current user-supplied function for rendering draw lists
    - the font atlas

    This class provides read/write properties that read and write the attributes
    in the C struct.

    Attributes
    ----------
    display_size
    delta_time
    ini_saving_rate
    ini_file_name
    log_file_name
    mouse_double_click_time
    mouse_double_click_max_time
    mouse_drag_threshold
    -- keymap
    -- key_repeat_delay
    -- key_repeat_rate
    -- user_data

    fonts
    font_global_scale
    font_allow_user_scaling
    display_framebuffer_scale
    display_visible_min
    display_visible_max

    """
    def __init__(self, io):
        self._io = io
        self._user_render_callback = None

    @property
    def display_size(self):
        """tuple: Display size, in pixels. For clamping windows positions.
        Not set by default
        """
        ds = self._io.DisplaySize
        return ds.x, ds.y

    @display_size.setter
    def display_size(self, value):
        if isinstance(value, tuple):
            value = ImVec2(*value)
        self._io.DisplaySize.x = value.x
        self._io.DisplaySize.y = value.y

    @property
    def delta_time(self):
        """float: Time elapsed since last frame, in seconds.

        Default is 1.0/60.0
        """
        return self._io.DeltaTime

    @property
    def ini_saving_rate(self):
        """float: Maximum time between saving positions/sizes to .ini file, in seconds

        Default is 5.0
        """
        return self._io.IniSavingRate

    @property
    def ini_file_name(self):
        """str: Path to .ini file. None to disable .ini saving.

        Default value is "imgui.ini"
        """
        s = ffi.new("const char[]", self._io.IniFileName)
        return s

    @ini_file_name.setter
    def ini_file_name(self, value):
        pass

    @property
    def log_file_name(self):
        """str: Path to .log file (default parameter to ImGui::LogToFile when no file is specified).

        Default value is "imgui_log.txt"
        """
        s = ffi.new("const char[]", self._io.LogFileName)
        return s

    @log_file_name.setter
    def log_file_name(self, value):
        pass

    @property
    def mouse_double_click_time(self):
        """float: Time for a double-click, in seconds.

        Default value is 0.3
        """
        return self._io.MouseDoubleClickTime

    @mouse_double_click_time.setter
    def mouse_double_click_time(self, value):
        self._io.MouseDoubleClickTime = value

    @property
    def mouse_double_click_max_dist(self):
        """float: Distance threshold to stay in to validate a double-click, in pixels.

        Default value is 6.0
        """
        return self._io.MouseDoubleClickTime

    @mouse_double_click_max_dist.setter
    def mouse_double_click_max_dist(self, value):
        self._io.MouseDoubleClickMaxDist = value

    @property
    def mouse_drag_threshold(self):
        """float: Distance threshold before considering we are dragging.

        Default value is 6.0
        """
        return self._io.MouseDoubleClickTime

    @mouse_drag_threshold.setter
    def mouse_drag_threshold(self, value):
        self._io.MouseDragThreshold = value

    @property
    def fonts(self):
        """<CData ImFontAtlas*>: Load and assemble one or more fonts into a single tightly packed texture. Output to Fonts array.

        Default value is set automatically by ImGui.

        We do not provide a python interface to access the contents of the font
        atlas. Consider this an opaque pointer to use as a parameter for the
        functions in :py:mod:`pymgui.font_atlas`.
        """
        return self._io.Fonts

    @property
    def font_global_scale(self):
        """float: Global scale all fonts.

        Default value is 1.0
        """
        return self._io.FontGlobalScale

    @font_global_scale.setter
    def font_global_scale(self, value):
        self._io.FontGlobalScale = value

    @property
    def font_allow_user_scaling(self):
        """bool: Allow user scaling text of individual window with CTRL+Wheel.

        Default value is False
        """
        return self._io.FontAllowUserScaling

    @font_allow_user_scaling.setter
    def font_allow_user_scaling(self, value):
        self._io.FontAllowUserScaling = value

    @property
    def display_framebuffer_scale(self):
        """2-tuple: For retina display or other situations where window coordinates are different from framebuffer coordinates.

        User storage only, presently not used by ImGui.

        Default value is (1.0, 1,0)
        """
        framebuffer_scale = self._io.DisplayFramebufferScale
        return framebuffer_scale.x, framebuffer_scale.y

    @display_framebuffer_scale.setter
    def display_framebuffer_scale(self, value):
        self._io.DisplayFramebufferScale.x = value[0]
        self._io.DisplayFramebufferScale.y = value[1]

    @property
    def display_visible_min(self):
        """2-tuple: If you use DisplaySize as a virtual space larger than your screen, set DisplayVisibleMin/Max to the visible area.

        Default value is (0.0, 0,0)
        """
        framebuffer_scale = self._io.DisplayVisibleMin
        return framebuffer_scale.x, framebuffer_scale.y

    @display_visible_min.setter
    def display_visible_min(self, value):
        self._io.DisplayVisibleMin.x = value[0]
        self._io.DisplayVisibleMin.y = value[1]

    @property
    def display_visible_max(self):
        """2-tuple: If the values are the same, we defaults to Min=(0.0f) and Max=DisplaySize

        Default value is (0.0, 0,0)
        """
        framebuffer_scale = self._io.DisplayVisibleMax
        return framebuffer_scale.x, framebuffer_scale.y

    @display_visible_max.setter
    def display_visible_max(self, value):
        self._io.DisplayVisibleMax.x = value[0]
        self._io.DisplayVisibleMax.y = value[1]

    @property
    def render_draw_list_func(self):
        return self._user_render_callback

    @render_draw_list_func.setter
    def render_draw_list_func(self, func):
        self._user_render_callback = func
        self._io.RenderDrawListsFn = func


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

    # @property
    # def cmd_lists(self):
    #     """<CData ImDrawLists**>: pointer to the list of draw commands to render
    #
    #     Consider this an opaque pointer to pass to the ImDrawList_* collection of functions
    #     """
    #     return self._im_draw_data[0].CmdLists
    #
    @property
    def cmd_lists_count(self):
        """int: number of commands in the """
        return self._im_draw_data[0].CmdListsCount

    @property
    def cmd_lists(self):
        cmd_lists = self._im_draw_data[0].CmdLists
        for n in range(self.cmd_lists_count):
            cmd_list = cmd_lists[n]
            yield cmd_list

    @property
    def total_vertex_count(self):
        """int: sum of all cmd_lists vtx_buffer.Size"""
        return self._im_draw_data[0].TotalVtxCount

    @property
    def total_index_count(self):
        """int: sum of all cmd_lists idx_buffer.Size"""
        return self._im_draw_data[0].TotalIdxCount


class ImDrawVertex(object):
    def __init__(self):
        pass


class ImDrawCmd(object):
    def __init__(self, imdrawcmd_cdata):
        self._cdata = imdrawcmd_cdata

    @property
    def elem_count(self):
        """uint: Number of indices (multiple of 3) to be rendered as triangles. Vertices are stored in the callee ImDrawList's vtx_buffer[] array, indices in idx_buffer[]."""
        return int(self._cdata[0].ElemCount)

    @property
    def clip_rect(self):
        """tuple: Clipping rectangle(x1, y1, x2, y2)"""
        r = self._cdata[0].ClipRect
        return r.x, r.y, r.z, r.w

    @property
    def texture_id(self):
        """int: User-provided texture ID. Set by user in ImfontAtlas::SetTexID() for fonts or passed to Image*() functions. Ignore if never using images or multiple fonts atlas"""

        x = ffi.cast("int*", self._cdata[0].TextureId)
        if x:
            return int(x[0])
        else:
            return None
