from __future__ import annotations

import logging

import numpy as np

from manim import BackgroundRectangle, Circle, Sector

logger = logging.getLogger(__name__)


def test_get_arc_center():
    np.testing.assert_array_equal(
        Sector(arc_center=[1, 2, 0]).get_arc_center(), [1, 2, 0]
    )


def test_BackgroundRectangle(manim_caplog):
    c = Circle()
    bg = BackgroundRectangle(c)
    bg.set_style(fill_opacity=0.42)
    assert bg.get_fill_opacity() == 0.42
    bg.set_style(fill_opacity=1, hello="world")
    assert (
        "Argument {'hello': 'world'} is ignored in BackgroundRectangle.set_style."
        in manim_caplog.text
    )
