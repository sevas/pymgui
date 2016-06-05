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

from vispy import gloo
from vispy import app
from vispy.gloo import gl
# gl.use_gl('gl+')

print(gl.current_backend)

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


device_objects = dict()

def create_device_objects():
    global device_objects
    vertex_shader = """
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





@ffi.callback("void (ImDrawData*)")
def render_with_gloo(draw_data):
    """draw ImGui's drawlists with vispy's gloo interface

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

    conf = gloo.get_gl_configuration()

    last_texture = gl.glGetParameter(gl.GL_TEXTURE_BINDING_2D)
    last_viewport = gl.glGetParameter(gl.GL_VIEWPORT)

    gloo.set_state(blend=True)
    gloo.set_blend_equation('func_add')
    gloo.set_blend_func(salpha='src_alpha', dalpha='one_minus_src_alpha')
    gloo.set_state(cull_face=False, depth_test=False, scissor_test=True)



    # Setup viewport, orthographic projection matrix
    gloo.set_viewport(0, 0, int(fb_width), int(fb_height))

    p = device_objects['program'] # type: gloo.Program

    ortho_projection = np.array([
        [2./fb_width,   0,                  0,      0],
        [0.,             2./-fb_height,     0,      0],
        [0.,             0.,                -1.,    0],
        [-1.,            1.,                0,      0]
    ])


    p['u_mvp'] = ortho_projection
    p['a_position'] = None
    p['a_uv'] = None
    p['a_color'] = None

    for cmd_list in d.cmd_lists:
        idx_buffer_offset = 0

        countVertices =C. ImDrawList_GetVertexBufferSize(cmd_list)
        countIndices = C.ImDrawList_GetIndexBufferSize(cmd_list)

        vertex_buffer_ptr = C.ImDrawList_GetVertexPtr(cmd_list, 0)
        index_buffer_ptr = C.ImDrawList_GetIndexPtr(cmd_list, 0)

        gl.glBufferData(gl.GL_ARRAY_BUFFER, countVertices * 20, vertex_buffer_ptr, gl.GL_STREAM_DRAW)
        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, countIndices * 2, index_buffer_ptr, gl.GL_STREAM_DRAW)



    # Restore modified state
    gl.glBindTexture(gl.GL_TEXTURE_2D, last_texture)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glPopMatrix()
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glPopMatrix()
    # gl.glPopAttrib()
    gl.glViewport(last_viewport[0], last_viewport[1], last_viewport[2], last_viewport[3])


class Canvas(app.Canvas):

    def __init__(self):
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

        gloo.set_clear_color('white')

        self._timer = app.Timer('auto', connect=self.update, start=True)

        self.show()

    def on_initialize(self, event):
        global device_objects
        io = pymgui.get_io()

        if not device_objects:
            create_device_objects()

        io.render_draw_list_func = render_with_gloo

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

        pymgui.button("hello button", (20, 50))
        pymgui.button("hello button 2", (20, 60))

        pymgui.end()
        pid = os.getpid()
        pymgui.render()


if __name__ == '__main__':
    c = Canvas()
    app.run()
