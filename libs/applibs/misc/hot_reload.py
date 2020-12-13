import os
import platform

from hot_reloader import App
from kivy.core.window import Window

from libs.uix.baseclass.root import Root

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class PROJECT_NAME(App):

    KV_FILES = {
        os.path.join(os.getcwd(), "libs", "uix", "kv", i)
        for i in os.listdir(os.path.join(os.getcwd(), "libs", "uix", "kv"))
    }

    CLASSES = {"<Root>": "root", "<HomeScreen>": "home_screen"}

    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]

    def __init__(self, **kwargs):
        super(PROJECT_NAME, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        Window.bind(on_keyboard=self._rebuild)
        self.title = "APPLICATION_TITLE"

        self.theme_cls.primary_palette = "PRIMARY_PALETTE"
        self.theme_cls.primary_hue = "PRIMARY_HUE"

        self.theme_cls.accent_palette = "ACCENT_PALETTE"
        self.theme_cls.accent_hue = "ACCENT_HUE"

        self.theme_cls.theme_style = "THEME_STYLE"

    def build_app(self):
        return Root()

    def _rebuild(self, *args):
        if args[1] == 96:  # key: `
            self.rebuild()
