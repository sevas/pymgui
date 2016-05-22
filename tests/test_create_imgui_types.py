import pytest
from math import fabs
from pymgui import ImVec2, ImVec4, ImColor

eps = 1E-3


def test_create_imvec2():
    v2 = ImVec2()
    assert fabs(v2.x) < eps and fabs(v2.y) < eps

    v2 = ImVec2(x=3.5)
    assert fabs(v2.x - 3.5) < eps and fabs(v2.y) < eps

    v2 = ImVec2(y=3.5)
    assert fabs(v2.x) < eps and fabs(v2.y - 3.5) < eps

    x, y = 32.5, 698.2
    v2 = ImVec2(x, y)
    assert fabs(v2.x - x) < eps and fabs(v2.y - y) < eps

def test_create_imcolor():
    values = 14, 14, 49, 255
    color = ImColor(*values)
    assert color.rgba() == values

    color = ImColor.from_ImVec4(ImVec4(0.2, 0.2, 0.2, 1.0))
    assert color.rgba() == (51,51, 51, 255)
