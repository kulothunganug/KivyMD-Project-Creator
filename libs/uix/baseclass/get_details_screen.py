import json
import os
import shutil
from datetime import datetime

from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import ColorProperty, ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.color_definitions import hue, palette
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd_extensions.sweetalert import SweetAlert
from plyer import filechooser

from libs.applibs import utils

from constants import BASE_TEMPLATE_FOLDER, MISC_FOLDER, TEMPLATES_FOLDER


class GetDetailsScreen(MDScreen):
    selected_template = StringProperty()
    template_py_files = ListProperty()
    template_kv_files = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ignore_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~ "  # NOQA: W605
        self.on_file_chooser_open = OnFileChooserOpen()

        Clock.schedule_once(self._late_init)

    def _late_init(self, interval):
        primary_palette_items = [
            {
                "text": primary_palette,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=primary_palette: self.set_primary_palette_item(
                    x
                ),
            }
            for primary_palette in palette
        ]
        self.primary_palette_menu = MDDropdownMenu(
            caller=self.ids.primary.ids.primary_palette,
            items=primary_palette_items,
            width_mult=3,
        )

        accent_palette_items = [
            {
                "text": accent_palette,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=accent_palette: self.set_accent_palette_item(
                    x
                ),
            }
            for accent_palette in palette
        ]

        self.accent_palette_menu = MDDropdownMenu(
            caller=self.ids.accent.ids.accent_palette,
            items=accent_palette_items,
            width_mult=3,
        )

        primary_hue_items = [
            {
                "text": hue_code,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=hue_code: self.set_primary_hue_item(x),
            }
            for hue_code in hue
        ]

        self.primary_hue_menu = MDDropdownMenu(
            caller=self.ids.primary.ids.primary_hue,
            items=primary_hue_items,
            width_mult=2,
        )

        accent_hue_items = [
            {
                "text": hue_code,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=hue_code: self.set_accent_hue_item(x),
            }
            for hue_code in hue
        ]

        self.accent_hue_menu = MDDropdownMenu(
            caller=self.ids.accent.ids.accent_hue,
            items=accent_hue_items,
            width_mult=2,
        )

        theme_style_items = [
            {
                "text": theme_style,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=theme_style: self.set_theme_style_item(
                    x
                ),
            }
            for theme_style in ["Light", "Dark"]
        ]
        self.theme_style_menu = MDDropdownMenu(
            caller=self.ids.theme_style.ids.theme_style,
            items=theme_style_items,
            width_mult=3,
        )

    def create_project(
        self,
        _application_title,
        _project_name,
        _application_version,
        _path_to_project,
        _author_name,
    ):

        (
            APPLICATION_TITLE,  # NOQA: N806
            PROJECT_NAME,  # NOQA: N806
            APPLICATION_VERSION,  # NOQA: N806
            PATH_TO_PROJECT,  # NOQA: N806
            AUTHOR_NAME,  # NOQA: N806
        ) = (
            _application_title.strip(),
            _project_name.strip(),
            _application_version.strip(),
            _path_to_project.strip(),
            _author_name.strip(),
        )

        if (
            len(APPLICATION_TITLE)
            and len(PROJECT_NAME)
            and len(APPLICATION_VERSION)
            and len(PATH_TO_PROJECT)
            and len(AUTHOR_NAME)
        ) == 0:
            return SweetAlert().fire(
                "Please Fill Up All the Fields!", type="warning"
            )

        chars = ""
        for char in list(self.ignore_chars):
            if char in PROJECT_NAME:
                chars += char

        if chars:
            return SweetAlert().fire(
                f"Please Don't Use '{chars}' in Project Name",
                type="warning",
            )
        else:
            for i in "1234567890":
                if PROJECT_NAME.startswith(i):
                    return SweetAlert().fire(
                        "Please Don't Use numbers as starting"
                        + "letters of the Project Name",
                        type="warning",
                    )

        FULL_PATH_TO_PROJECT = os.path.join(  # NOQA: N806
            PATH_TO_PROJECT, PROJECT_NAME
        )
        self.path_to_project = FULL_PATH_TO_PROJECT
        project_name = PROJECT_NAME.lower()

        if not os.path.exists(PATH_TO_PROJECT):
            return SweetAlert().fire(
                "Folder Path not Exists!",
                PATH_TO_PROJECT,
                type="warning",
            )

        if os.path.exists(FULL_PATH_TO_PROJECT):
            return SweetAlert().fire(
                f"Folder Named {project_name} is Already Exists! in '{PATH_TO_PROJECT}'",  # NOQA: E501
                type="warning",
            )

        utils.copytree(BASE_TEMPLATE_FOLDER, FULL_PATH_TO_PROJECT)

        os.rename(
            os.path.join(FULL_PATH_TO_PROJECT, "project_name.py"),
            os.path.join(FULL_PATH_TO_PROJECT, f"{project_name}.py"),
        )

        PROJECT_UIX_FOLDER = os.path.join(  # NOQA: N806
            FULL_PATH_TO_PROJECT, "libs", "uix"
        )

        for py_file in self.template_py_files:
            shutil.copy(
                py_file,
                os.path.join(PROJECT_UIX_FOLDER, "baseclass"),
            )
        for kv_file in self.template_kv_files:
            shutil.copy(
                kv_file,
                os.path.join(PROJECT_UIX_FOLDER, "kv"),
            )

        for file in utils.get_files(FULL_PATH_TO_PROJECT, [".py", ".spec"]):
            utils.edit_file(
                in_file=file,
                values={
                    "APPLICATION_TITLE": APPLICATION_TITLE,
                    "PROJECT_NAME": PROJECT_NAME,
                    "project_name": project_name,
                    "APPLICATION_VERSION": APPLICATION_VERSION,
                    "AUTHOR_NAME": AUTHOR_NAME,
                    "PRIMARY_PALETTE": self.ids.primary.ids.primary_palette.current_item,  # NOQA: E501
                    "PRIMARY_HUE": self.ids.primary.ids.primary_hue.current_item,  # NOQA: E501
                    "ACCENT_PALETTE": self.ids.accent.ids.accent_palette.current_item,  # NOQA: E501
                    "ACCENT_HUE": self.ids.accent.ids.accent_hue.current_item,
                    "THEME_STYLE": self.ids.theme_style.ids.theme_style.current_item,  # NOQA: E501
                },
            )

        with open(os.path.join(TEMPLATES_FOLDER, "classes.json")) as f:
            data = json.loads(f.read())

        utils.edit_file(
            in_file=os.path.join(FULL_PATH_TO_PROJECT, "hotreloader.py"),
            values={
                "CLASSES": f"CLASSES = {str(data[self.selected_template])}"
            },
        )

        if self.ids.gitignore.active:
            shutil.copy(
                os.path.join(MISC_FOLDER, ".gitignore"),
                FULL_PATH_TO_PROJECT,
            )
        if self.ids.readme.active:
            self.edit_misc_file("README.md", {"PROJECT_NAME": PROJECT_NAME})
        if self.ids.license.active:
            self.edit_misc_file(
                "LICENSE",
                {
                    "YEAR": str(datetime.now().year),
                    "COPYRIGHT_HOLDER": AUTHOR_NAME,
                },
            )

        SweetAlert().fire(
            "Congrat's",
            f"Project '{PROJECT_NAME}' Has Been Created Successfully!",
            type="success",
        )

    def edit_misc_file(self, file, values):
        _misc_file = os.path.join(MISC_FOLDER, file)
        shutil.copy(
            _misc_file,
            self.path_to_project,
        )
        misc_file = os.path.join(self.path_to_project, file)
        utils.edit_file(in_file=misc_file, values=values)

    def set_primary_palette_item(self, text):
        self.ids.primary.ids.primary_palette.set_item(text)
        self.primary_palette_menu.dismiss()

    def set_accent_palette_item(self, text):
        self.ids.accent.ids.accent_palette.set_item(text)
        self.accent_palette_menu.dismiss()

    def set_primary_hue_item(self, text):
        self.ids.primary.ids.primary_hue.set_item(text)
        self.primary_hue_menu.dismiss()

    def set_accent_hue_item(self, text):
        self.ids.accent.ids.accent_hue.set_item(text)
        self.accent_hue_menu.dismiss()

    def set_theme_style_item(self, text):
        self.ids.theme_style.ids.theme_style.set_item(text)
        self.theme_style_menu.dismiss()

    def open_file_manager(self):
        def _open_file_chooser(i):
            filechooser.choose_dir(on_selection=self.on_path_selection)
            self.on_file_chooser_open.dismiss()

        self.on_file_chooser_open.open()
        Clock.schedule_once(_open_file_chooser, 0.3)

    def on_path_selection(self, path):
        self.ids.path_to_project.text = path[0]

    def change_to_templates(self):
        self.manager.current = "templates"


class ColorWidget(BoxLayout):
    rgba_color = ColorProperty()


class OnFileChooserOpen(BaseDialog):
    pass
