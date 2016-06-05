import numpy as np
from . import _cimgui

ffi = _cimgui.ffi
C = _cimgui.C

# void             ImFontConfig_DefaultConstructor(ImFontConfig* config);
#
# void             ImFontAtlas_GetTexDataAsRGBA32(ImFontAtlas* atlas, unsigned char** out_pixels, int* out_width, int* out_height, int* out_bytes_per_pixel);
# void             ImFontAtlas_GetTexDataAsAlpha8(ImFontAtlas* atlas, unsigned char** out_pixels, int* out_width, int* out_height, int* out_bytes_per_pixel);
# void             ImFontAtlas_SetTexID(ImFontAtlas* atlas, void* tex);
# ImFont*          ImFontAtlas_AddFont(ImFontAtlas* atlas, const ImFontConfig* font_cfg);
# ImFont*          ImFontAtlas_AddFontDefault(ImFontAtlas* atlas, const ImFontConfig* font_cfg);
# ImFont*          ImFontAtlas_AddFontFromFileTTF(ImFontAtlas* atlas, const char* filename, float size_pixels, const ImFontConfig* font_cfg, const ImWchar* glyph_ranges);
# ImFont*          ImFontAtlas_AddFontFromMemoryTTF(ImFontAtlas* atlas, void* ttf_data, int ttf_size, float size_pixels, const ImFontConfig* font_cfg, const ImWchar* glyph_ranges);
# ImFont*          ImFontAtlas_AddFontFromMemoryCompressedTTF(ImFontAtlas* atlas, const void* compressed_ttf_data, int compressed_ttf_size, float size_pixels, const ImFontConfig* font_cfg, const ImWchar* glyph_ranges);
# ImFont*          ImFontAtlas_AddFontFromMemoryCompressedBase85TTF(ImFontAtlas* atlas, const char* compressed_ttf_data_base85, float size_pixels, const ImFontConfig* font_cfg, const ImWchar* glyph_ranges);
# void             ImFontAtlas_ClearTexData(ImFontAtlas* atlas);
# void             ImFontAtlas_Clear(ImFontAtlas* atlas);

def get_tex_data_as_rgba32(font_atlas):
    pixels = ffi.new("unsigned char**")
    width = ffi.new("int*")
    height = ffi.new("int*")
    bpp = ffi.new("int*")
    C.ImFontAtlas_GetTexDataAsRGBA32(
        font_atlas,
        pixels,
        width,
        height,
        bpp,
    )
    w, h, c = width[0], height[0], bpp[0]
    buf =  ffi.buffer(pixels[0], w*h*c)
    texture_atlas = np.frombuffer(buf, dtype=np.uint8)
    texture_atlas = texture_atlas.reshape(h, w, c)
    return texture_atlas
