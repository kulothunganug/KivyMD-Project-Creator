import os

from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

import utils
from constants import TEMPLATES_FOLDER


class TemplatesScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change_to_home(self):
        self.manager.current = "home"

    def change_to_get_details(self):
        if not self.manager.has_screen("get_details"):
            utils.load_kv("get_details_screen.kv")
            from libs.uix.baseclass.get_details_screen import GetDetailsScreen

            screen_object = GetDetailsScreen(name="get_details")
            self.manager.add_widget(screen_object)

        for widget in self.ids.container.children:
            if widget.state == "down":
                template_name = widget.name
                get_details = self.manager.get_screen("get_details")
                get_details.selected_template = template_name
                SELECTED_TEMPLATE_FOLDER = os.path.join(  # NOQA: N806
                    TEMPLATES_FOLDER, template_name
                )
                get_details.template_py_files = utils.get_files(
                    SELECTED_TEMPLATE_FOLDER, [".py"]
                )
                get_details.template_kv_files = utils.get_files(
                    SELECTED_TEMPLATE_FOLDER, [".kv"]
                )

                self.manager.current = "get_details"
                break


class CustomImage(
    ToggleButtonBehavior, MDBoxLayout, HoverBehavior, ThemableBehavior
):
    name = StringProperty()
    use_toggle_behavior = BooleanProperty(True)
