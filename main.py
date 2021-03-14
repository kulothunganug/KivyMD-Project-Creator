import os
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))

import platform  # NOQA: E402

from kivy.config import Config  # NOQA: E402
from kivy.core.window import Window  # NOQA: E402
from kivy.logger import Logger  # NOQA: E402
from kivymd.app import MDApp  # NOQA: E402

from libs.uix.baseclass.root import Root  # NOQA: E402

import utils  # NOQA: E402

__version__ = "v0.3.0b"


if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

Logger.info("KivyMD Project Creator: " + __version__)

Window.maximize()

KV_DIR = f"{os.path.dirname(__file__)}/libs/kv/"

Config.set("kivy", "exit_on_escape", "0")
Config.set("input", "mouse", "mouse,disable_multitouch")

utils.load_kv("root.kv")
utils.load_kv("home_screen.kv")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "KivyMD Project Creator"
        self.icon = "assets/images/logo.png"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"

    def build(self):
        FONT_PATH = os.path.join("assets", "fonts/")  # NOQA: N806

        self.theme_cls.font_styles.update(
            {
                "H1": [FONT_PATH + "RobotoMono-Medium", 96, False, -1.5],
                "H2": [FONT_PATH + "Overpass-Regular", 60, False, -0.5],
                "H3": [FONT_PATH + "RobotoMono-Regular", 48, False, 0],
                "H4": [FONT_PATH + "RobotoMono-SemiBold", 34, False, 0.25],
                "H5": [FONT_PATH + "Overpass-SemiBold", 24, False, 0],
                "H6": [FONT_PATH + "RobotoMono-Medium", 20, False, 0.15],
                "Subtitle1": [
                    FONT_PATH + "Overpass-Regular",
                    16,
                    False,
                    0.15,
                ],
                "Subtitle2": [
                    FONT_PATH + "Overpass-Regular",
                    14,
                    False,
                    0.1,
                ],
                "Body1": [FONT_PATH + "Overpass-Regular", 16, False, 0.5],
                "Body2": [FONT_PATH + "Overpass-Regular", 14, False, 0.25],
                "Button": [FONT_PATH + "Overpass-Black", 14, True, 1.25],
                "Caption": [
                    FONT_PATH + "RobotoMono-Regular",
                    12,
                    False,
                    0.4,
                ],
                "Overline": [
                    FONT_PATH + "RobotoMono-Regular",
                    10,
                    True,
                    1.5,
                ],
            }
        )
        return Root()


if __name__ == "__main__":
    MainApp().run()
