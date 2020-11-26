import json

from kivy.clock import Clock
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager


class Root(ScreenManager):
    """
    The Root (or Assembler) of the app
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
            1. Create screen_name_py.py in libs/baseclass/
            2. Create screen_name_kv.kv in libs/kv/
            3. Add the screen details in screens.json like below:
                {
                    "from libs.uix.baseclass.screen_name_py import ScreenClassName": {
                        "screen_name": "my_screen_name",
                        "factory": "Factory.ScreenClassName()",
                        "kv_file": "screen_name_kv"
                    }
                }
                Note: In .JSON you must not use:
                        * Extra Commas
                        * Comments
                        * Trailing White Spaces.
        """
        with open("screens.json") as f:
            screens = json.load(f)
            for import_screen, screen_details in screens.items():
                exec(import_screen)  # excecuting imports
                screen_object = eval(
                    screen_details["factory"]
                )  # adding it to Factory
                screen_object.name = screen_details[
                    "screen_name"
                ]  # giving the name of the screen
                self.add_widget(
                    screen_object
                )  # finally adding it to the screen manager
