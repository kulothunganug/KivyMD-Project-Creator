import utils
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

utils.load_kv("home_screen.kv")


class HomeScreen(MDScreen):
    """
    Example Screen.
    """

    nav_drawer = ObjectProperty()
