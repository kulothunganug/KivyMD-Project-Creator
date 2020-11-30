import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("tab_three.kv")


class TabThree(FloatLayout, MDTabsBase):
    pass
