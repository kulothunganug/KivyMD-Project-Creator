"""
    Usage:
    -----
    Use it like a normal `MDLabel` but do not to use these attr:
        * auto_scale
        * texture_size = 0
        * width = 0
        * height = 0
"""

from kivy.properties import BooleanProperty
from kivymd.uix.label import MDLabel

__all__ = ("AutoScaleLabel",)


class AutoScaleLabel(MDLabel):
    """
    AutoScaleLabel is inherited from MDLabel,
    so `MDLabel`'s all attr can be used in this.
    """

    auto_scale = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_size(self, *args):
        if self.size_hint_x is None and self.size_hint_y is None:
            return
        self.calculate_font_size()

    def calculate_font_size(self):
        if (
            not self.auto_scale
            or self.texture_size == [0, 0]
            or self.width == 0
            or self.height == 0
        ):
            return
        if self.size_hint_x is None or self.size_hint_y is None:
            if self.size_hint_x is None:
                scale = "height"
            else:
                scale = "width"
        else:
            hs = (
                self.texture_size[0] / self.texture_size[1] * self.height
            ) / self.width
            ws = (
                self.texture_size[1] / self.texture_size[0] * self.width
            ) / self.height
            if hs < 1:
                scale = "height"
            elif ws < 1:
                scale = "width"
            else:
                if ws > hs:  # Use the one that will scale less
                    scale = "width"
                else:
                    scale = "height"
        if scale == "height":
            font_size = round(
                self.font_size / self.texture_size[1] * self.height, 2
            )
        else:
            font_size = round(
                self.font_size / self.texture_size[0] * self.width, 2
            )
        if self.font_size != font_size:
            self.font_size = font_size
