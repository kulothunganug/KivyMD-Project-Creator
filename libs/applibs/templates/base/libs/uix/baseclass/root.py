import json

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

import utils

utils.load_kv("root.kv")


class Root(ScreenManager):
    """
    The Root (or Assembler) of the App.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.add_screens)
        """
        Adding the screens to the Root (ScreenManager).
        """

    def add_screens(self, interval):
        """
        If you need to use more screens in your app,
        Create your screen files like below:
            1. Create screen_file.py in libs/uix/baseclass/
            2. Create screen_file.kv in libs/uix/kv/
            3. Add the screen details in screens.json like below:
                {
                    ...,
                    "screen_name": {
                        "import": "from libs.uix.baseclass.screen_py_file import ScreenObject",
                        "kv": "libs/uix/kv/screen_kv_file.kv",
                        "object": "ScreenObject()"
                    }
                }
                Note: In .JSON you must not use:
                        * Unneeded Commas
                        * Comments
        """
        with open("screens.json") as f:
            screens = json.load(f)

        for screen_name in screens.keys():
            screen_details = screens[screen_name]
            Builder.load_file(screen_details["kv"])
            exec(screen_details["import"])  # excecuting imports
            screen_object = eval(screen_details["object"])  # calling it
            screen_object.name = screen_name  # giving the name of the screen
            self.add_widget(
                screen_object
            )  # finally adding it to the screen manager
