import os
import platform

from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.logger import Logger
from kivymd.app import MDApp

from libs.uix.baseclass.root_screen import RootScreen

__version__ = "0.01a"


# this is needed for supporting Windows 10 with OpenGL < v2.0
# Example: VirtualBox w/ OpenGL v1.1
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

Logger.info("KivyMD Project Creator: " + f"v{__version__}")

Window.maximize()

KV_DIR = f"{os.path.dirname(__file__)}/libs/kv/"

Config.set("kivy", "exit_on_escape", "0")
Config.set("input", "mouse", "mouse,disable_multitouch")

Builder.load_file("libs/uix/kv/root_screen.kv")
Builder.load_file("libs/uix/kv/home_screen.kv")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "KivyMD Project Creator"
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"

    def build(self):
        FONT_PATH = "assets/fonts/"

        self.theme_cls.font_styles.update(
            {
                "H1": [FONT_PATH + "RobotoMono-Medium", 96, False, -1.5],
                "H2": [FONT_PATH + "Overpass-Regular", 60, False, -0.5],
                "H3": [FONT_PATH + "RobotoMono-Regular", 48, False, 0],
                "H4": [FONT_PATH + "RobotoMono-SemiBold", 34, False, 0.25],
                "H5": [FONT_PATH + "Overpass-SemiBold", 24, False, 0],
                "H6": [FONT_PATH + "RobotoMono-Medium", 20, False, 0.15],
                # "Subtitle1": [
                #     FONT_PATH + "RobotoCondensed-Regular",
                #     16,
                #     False,
                #     0.15,
                # ],
                # "Subtitle2": [
                #     FONT_PATH + "RobotoCondensed-Medium",
                #     14,
                #     False,
                #     0.1,
                # ],
                "Body1": [FONT_PATH + "Overpass-Regular", 16, False, 0.5],
                # "Body2": [FONT_PATH + "RobotoCondensed-Light", 14, False, 0.25],
                "Button": [FONT_PATH + "Overpass-Black", 14, True, 1.25],
                # "Caption": [
                #     FONT_PATH + "RobotoCondensed-Regular",
                #     12,
                #     False,
                #     0.4,
                # ],
                "Overline": [
                    FONT_PATH + "RobotoMono-Regular",
                    10,
                    True,
                    1.5,
                ],
            }
        )
        return RootScreen()


if __name__ == "__main__":
    MainApp().run()
