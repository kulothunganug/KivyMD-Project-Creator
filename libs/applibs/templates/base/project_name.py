import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class PROJECT_NAME(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(PROJECT_NAME, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "APPLICATION_TITLE"

        self.theme_cls.primary_palette = "PRIMARY_PALETTE"
        self.theme_cls.primary_hue = "PRIMARY_HUE"

        self.theme_cls.accent_palette = "ACCENT_PALETTE"
        self.theme_cls.accent_hue = "ACCENT_HUE"

        self.theme_cls.theme_style = "THEME_STYLE"

    def build(self):
        return Root()
