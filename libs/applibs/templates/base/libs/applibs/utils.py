import os

from kivy.lang import Builder


def load_kv(file_name, file_path=os.path.join("libs", "uix", "kv")):
    with open(os.path.join(file_path, file_name), encoding="utf-8") as kv:
        Builder.load_string(kv.read())
