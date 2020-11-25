import os
import platform
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from libs.baseclass.root_screen import Root

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == 'Windows':
    os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class PROJECT_NAME(MDApp):
    title = "PROJECT_NAME"

    def __init__(self, **kwargs):
        super(PROJECT_NAME, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "PROJECT_TITLE"

        self.theme_cls.primary_palette = "PRIMARY_PALETTE"
        self.theme_cls.primary_hue = "PRIMARY_HUE"

        self.theme_cls.accent_palette = "ACCENT_PALETTE"
        self.theme_cls.accent_hue = "ACCENT_HUE"

        self.theme_cls.theme_style = "THEME_STYLE"

    def build(self):
        PATH_TO_KV_FILES = os.path.join(self.directory, "libs", "kv")
        for kv_file in os.listdir(PATH_TO_KV_FILES):
            if kv_file.endswith(".kv"):
                Builder.load_file(os.path.join(PATH_TO_KV_FILES, kv_file))
        return Root()
