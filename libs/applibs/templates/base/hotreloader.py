"""
HotReloader
-----------
Uses kaki module for Hot Reload (limited to some uses cases).
Before using, install kaki by `pip install kaki`

"""


import os
import platform
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))

from kaki.app import App as HotReloaderApp  # NOQA: E402
from kivy.logger import LOG_LEVELS, Logger  # NOQA: E402

Logger.setLevel(LOG_LEVELS["debug"])

from kivy.core.window import Window  # NOQA: E402
from kivymd.app import MDApp  # NOQA: E402

from libs.uix.baseclass.root import Root  # NOQA: E402

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

KV_FOLDER = os.path.join(os.getcwd(), "libs", "uix", "kv")


class PROJECT_NAME(MDApp, HotReloaderApp):  # NOQA: N801
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    KV_FILES = [os.path.join(KV_FOLDER, i) for i in os.listdir(KV_FOLDER)]

    # Class to watch from *.py files
    # You need to register the *.py files in libs/uix/baseclass/*.py
    CLASSES  # NOQA: F821

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def __init__(self, **kwargs):
        super(PROJECT_NAME, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "APPLICATION_TITLE"

        self.theme_cls.primary_palette = "PRIMARY_PALETTE"
        self.theme_cls.primary_hue = "PRIMARY_HUE"

        self.theme_cls.accent_palette = "ACCENT_PALETTE"
        self.theme_cls.accent_hue = "ACCENT_HUE"

        self.theme_cls.theme_style = "THEME_STYLE"

    def build_app(self):  # build_app works like build method
        return Root()


if __name__ == "__main__":
    PROJECT_NAME().run()
