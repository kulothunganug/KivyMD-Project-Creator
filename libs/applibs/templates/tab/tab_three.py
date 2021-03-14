from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

import utils

utils.load_kv("tab_three.kv")


class TabThree(FloatLayout, MDTabsBase):
    """
    Tab Item Three.
    """
