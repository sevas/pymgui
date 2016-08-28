# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vispy: gallery 3

"""
Example demonstrating showing a quad. Like hello_quad1.py, but now
with Texture2D and VertexBuffer, and optionally using an ElementBuffer to
draw the vertices.
"""
import os
import time
import numpy as np

import abc

from vispy import gloo
from vispy import app
from vispy.gloo import gl
# gl.use_gl('gl+')


import pymgui
from pymgui._cimgui import ffi, C



# Create a texture
im1 = np.zeros((100, 100, 3), 'float32')
im1[:50, :, 0] = 1.0
im1[:, :50, 1] = 1.0
im1[50:, 50:, 2] = 1.0

# Create vetices and texture coords, combined in one array for high performance
vertex_data = np.zeros(4, dtype=[('a_position', np.float32, 3),
                                 ('a_texcoord', np.float32, 2)])
vertex_data['a_position'] = np.array([[-0.8, -0.8, 0.0], [+0.7, -0.7, 0.0],
                                      [-0.7, +0.7, 0.0], [+0.8, +0.8, 0.0, ]])
vertex_data['a_texcoord'] = np.array([[0.0, 0.0], [0.0, 1.0],
                                      [1.0, 0.0], [1.0, 1.0]])

# Create indices and an ElementBuffer for it
indices = np.array([0, 1, 2, 1, 2, 3], np.uint16)
indices_buffer = gloo.IndexBuffer(indices)
client_indices_buffer = gloo.IndexBuffer(indices)


VERT_SHADER = """ // simple vertex shader
#version 120
attribute vec3 a_position;
attribute vec2 a_texcoord;
uniform float sizeFactor;

void main (void) {
    // Pass tex coords
    gl_TexCoord[0] = vec4(a_texcoord.x, a_texcoord.y, 0.0, 0.0);
    // Calculate position
    gl_Position = sizeFactor*vec4(a_position.x, a_position.y, a_position.z,
                                                        1.0/sizeFactor);
}
"""

FRAG_SHADER = """ // simple fragment shader
#version 120
uniform sampler2D texture1;

void main()
{
    gl_FragColor = texture2D(texture1, gl_TexCoord[0].st);
}

"""


@ffi.callback("void (ImDrawData*)")
def stub_render(draw_data):
    d = pymgui.ImDrawData(draw_data)
    print(d.valid)
    print(d.total_vertex_count)
    print(d.total_index_count)
    cmds = d.cmd_lists


class ImGuiBackend(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def register_draw_list_func(self, io):
        pass


class StubImGuiBackend(ImGuiBackend):
    def __init__(self):
        pass

    def register_draw_list_func(self, io):
        io.render_draw_list_func = stub_render


device_objects = dict()



def create_device_objects_with_gloo():
    global device_objects
    vertex_shader = """
#version 120
uniform mat4 u_mvp;
attribute highp vec2 a_position;
attribute highp vec2 a_uv;
attribute highp vec4 a_color;
varying vec2 Frag_UV;
varying vec4 Frag_Color;
void main()
{
    Frag_UV = a_uv;
    Frag_Color = a_color;
    gl_Position = u_mvp * vec4(a_position.xy,0,1);
}"""

    fragment_shader = """
#version 120
uniform sampler2D u_texture;
varying highp vec2 Frag_UV;
varying highp vec4 Frag_Color;
void main()
{
    gl_FragColor = Frag_Color * texture2D(u_texture, Frag_UV.st);
}
    """
    p = gloo.Program(vert=vertex_shader, frag=fragment_shader)
    device_objects['program'] = p

    geometry = np.array([])


def imshow(img):
    import matplotlib.pyplot as plt
    plt.imshow(img)
    plt.show()


@ffi.callback("void (ImDrawData*)")
def render_with_gloo(draw_data):
    """draw ImGui's drawlists with vispy's gloo interface

    Parameters
    ----------
    draw_data: ImDrawData

    """
    global device_objects

    # adapted from imgui_impl_ios.cpp in imgui, to target the minimal GLES API
    d = pymgui.ImDrawData(draw_data)
    io = pymgui.get_io()

    fb_scale = io.display_framebuffer_scale
    fb_width, fb_height = io.display_size

    if fb_width == 0 or fb_height == 0:
        return

    conf = gloo.get_gl_configuration()

    # backup GL state
    last_program = gl.glGetParameter(gl.GL_CURRENT_PROGRAM)
    last_texture = gl.glGetParameter(gl.GL_TEXTURE_BINDING_2D)
    last_array_buffer = gl.glGetParameter(gl.GL_ARRAY_BUFFER_BINDING)
    last_element_array_buffer = gl.glGetParameter(gl.GL_ELEMENT_ARRAY_BUFFER_BINDING)
    last_viewport = gl.glGetParameter(gl.GL_VIEWPORT)

    last_enable_blend = gl.glIsEnabled(gl.GL_BLEND),
    last_blend_equation = gl.glGetParameter(gl.GL_BLEND_EQUATION_RGB),

    last_blend_func = dict(
        last_blend_equation_alpha=gl.glGetParameter(gl.GL_BLEND_EQUATION_ALPHA),
    )

    last_gl_states = dict(
        cull_face = gl.glIsEnabled(gl.GL_CULL_FACE),
        depth_test = gl.glIsEnabled(gl.GL_DEPTH_TEST),
        scissor_test = gl.glIsEnabled(gl.GL_SCISSOR_TEST))

    gloo.set_state(blend=True)
    gloo.set_blend_equation('func_add')
    gloo.set_blend_func(salpha='src_alpha', dalpha='one_minus_src_alpha')
    gloo.set_state(cull_face=False, depth_test=False, scissor_test=True)

    gl.glActiveTexture(gl.GL_TEXTURE0)

    # Setup viewport, orthographic projection matrix
    gloo.set_viewport(0, 0, int(fb_width), int(fb_height))

    p = device_objects['program'] # type: gloo.Program

    ortho_projection = np.array([
        [2./fb_width,   0,                  0,      0],
        [0.,             2./-fb_height,     0,      0],
        [0.,             0.,                -1.,    0],
        [-1.,            1.,                0,      0]
    ])

    vtype = [('a_position', np.float32, 2),
             ('a_uv', np.float32, 2),
             # ('a_color', np.uint8, 4)]
             ('a_color', np.uint32, 1)]

             # pos_dtype = [('a_position', np.float32, 2)]
    # uv_dtype =  [('a_uv', np.float32, 2)]
    # color_dtype = [('a_color', np.uint8, 4)]
    itype = np.uint16

    display_scale = 1.0

    p['u_mvp'] = ortho_projection


    # print("draw {} cmd_list".format(len(d.cmd_lists)))
    for cmd_list in d.cmd_lists:
        vertex_count =C.ImDrawList_GetVertexBufferSize(cmd_list)
        index_count = C.ImDrawList_GetIndexBufferSize(cmd_list)

        vertex_buffer_ptr = C.ImDrawList_GetVertexPtr(cmd_list, 0)
        index_buffer_ptr = C.ImDrawList_GetIndexPtr(cmd_list, 0)

        def to_nparray(ptr, item_count, dtype):
            byte_count = item_count * dtype.itemsize
            as_bytes = ffi.buffer(ptr, byte_count)
            return np.frombuffer(as_bytes, dtype=dtype)

        ig_vertices = to_nparray(vertex_buffer_ptr, vertex_count, np.dtype(vtype))
        ig_indices = to_nparray(index_buffer_ptr, index_count, np.dtype(itype))
        # print("{} vertices to draw".format(len(ig_vertices)))
    #
        p['a_position'] = ig_vertices[:]
        # p['a_uv'] = ig_vertices['a_uv']
        # p['a_color'] = ig_vertices['a_color']
        # device_objects['geometry'] = ig_vertices
    #
    #     gl.glBufferData(gl.GL_ARRAY_BUFFER, ig_vertices, gl.GL_STREAM_DRAW)
    #     gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, indices, gl.GL_STREAM_DRAW)
    #
    #     index_buffer_offset = 0
    #     cmd_size = C.ImDrawList_GetCmdSize(cmd_list)
    #     for cmd_index in range(cmd_size):
    #         draw_cmd_ptr = C.ImDrawList_GetCmdPtr(cmd_list, cmd_index)
    #         draw_cmd = pymgui.ImDrawCmd(draw_cmd_ptr)
    #
    #         if draw_cmd.texture_id:
    #             gl.glBindTexture(gl.GL_TEXTURE_2D, draw_cmd.texture_id)
    #         x1, y1, x2, y2 = draw_cmd.clip_rect
    #
    #         gl.glScissor(
    #             x=int(x1 * display_scale),
    #             y=int(y1 * display_scale),
    #             width=int((x2 - x1) * display_scale),
    #             height=int((y2 - y1) * display_scale)
    #         )
    #
    #         start, stop = index_buffer_offset, draw_cmd.elem_count
    #         # gl.glDrawElements(gl.GL_TRIANGLES, draw_cmd.elem_count, gl.GL_UNSIGNED_SHORT, indices[index_buffer_offset:])
    #         p.draw('triangles', gloo.IndexBuffer(ig_indices[start:stop]))
    #         index_buffer_offset += draw_cmd.elem_count
    #
    # # Restore modified state
    gloo.set_state(**last_gl_states)
    gloo.set_state(blend=last_enable_blend)
    # gloo.set_blend_equation(last_blend_equation)
    # # gl.glBindVertexArray(0)
    # gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
    gl.glUseProgram(last_program)
    # gl.glActiveTexture(gl.GL_TEXTURE0)
    # gl.glBindTexture(gl.GL_TEXTURE_2D, last_texture)



@ffi.callback("void (ImDrawData*)")
def render_with_pyopengl(draw_data):
    """draw ImGui's drawlists with PyOpenGL backend

    Parameters
    ----------
    draw_data: ImDrawData

    """
    # adapted from imgui_impl_ios.cpp in imgui, to target the minimal GLES API
    d = pymgui.ImDrawData(draw_data)

    io = pymgui.get_io()

    fb_scale = io.display_framebuffer_scale
    fb_width, fb_height = io.display_size

    if fb_width == 0 or fb_height == 0:
        return


class Canvas(app.Canvas):
    def __init__(self, backend):
        self._backend = backend
        app.Canvas.__init__(self, keys='interactive')

        # Create program
        self._program = gloo.Program(VERT_SHADER, FRAG_SHADER)

        # Create vertex buffer
        self._vbo = gloo.VertexBuffer(vertex_data)

        # Set uniforms, samplers, attributes
        # We create one VBO with all vertex data (array of structures)
        # and create two views from it for the attributes.
        self._program['texture1'] = gloo.Texture2D(im1)
        self._program.bind(self._vbo)  # This does:
        #self._program['a_position'] = self._vbo['a_position']
        #self._program['a_texcoords'] = self._vbo['a_texcoords']

        gloo.set_clear_color('#245B60')

        self._timer = app.Timer('auto', connect=self.update, start=True)

        self.show()

    def on_initialize(self, event):
        global device_objects
        io = pymgui.get_io()

        if not device_objects:
            create_device_objects_with_gloo()

        # io.render_draw_list_func = self._backend.draw_list
        # io.render_draw_list_func = stub_render
        io.render_draw_list_func = render_with_gloo
        # io.render_draw_list_func = render_with_pyopengl

        # self._backend.register_draw_list_func(io)

        font_atlas = io.fonts
        self.font_atlas_texture = pymgui.get_tex_data_as_rgba32(font_atlas)

        io.display_size = self.size


    def on_resize(self, event):
        width, height = event.physical_size
        gloo.set_viewport(0, 0, width, height)

    def on_draw(self, event):
        pymgui.new_frame()

        gloo.clear()

        # Draw
        self._program['sizeFactor'] = 0.5 + np.sin(time.time() * 3) * 0.2

        # Draw (pick one!)
        # self._program.draw('triangle_strip')
        self._program.draw('triangles', indices_buffer)
        # self._program.draw('triangles', client_indices_buffer)  # Not
        # recommended

        self.draw_gui()

    def draw_gui(self):

        pymgui.begin("hello", True)

        # pymgui.button("hello button", (20, 50))
        # pymgui.button("hello button 2", (20, 60))
        #
        pymgui.end()
        # pid = os.getpid()
        pymgui.render()


if __name__ == '__main__':
    b = StubImGuiBackend()
    c = Canvas(backend=b)
    app.run()
