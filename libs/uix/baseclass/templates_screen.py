import utils
from kivy.graphics import Color, RoundedRectangle
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class TemplatesScreen(MDScreen):
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
                self.manager.get_screen(
                    "get_details"
                ).selected_template = widget.name
                self.manager.current = "get_details"
                break


class CustomImage(
    ToggleButtonBehavior, MDBoxLayout, HoverBehavior, ThemableBehavior
):
    name = StringProperty()
    use_toggle_behavior = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(CustomImage, self).__init__(**kwargs)
        self.allow_no_selection = False
        self.group = "activites"

    def on_state(self, instance, state):
        if self.use_toggle_behavior:
            if state == "normal":
                with self.canvas.before:
                    Color(rgba=self.theme_cls.bg_normal)
                    RoundedRectangle(pos=self.pos, size=self.size)
            elif state == "down":
                with self.canvas.before:
                    Color(rgba=self.theme_cls.primary_dark)
                    RoundedRectangle(pos=self.pos, size=self.size)

    def on_enter(self):
        if self.state == "normal" and self.use_toggle_behavior:
            with self.canvas.before:
                Color(rgba=self.theme_cls.bg_dark)
                RoundedRectangle(size=self.size, pos=self.pos)

    def on_leave(self):
        if self.state == "normal" and self.use_toggle_behavior:
            with self.canvas.before:
                Color(rgba=self.theme_cls.bg_normal)
                RoundedRectangle(pos=self.pos, size=self.size)
