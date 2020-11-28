import os
import shutil

from kivy.clock import Clock
from kivy.properties import ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.color_definitions import hue, palette
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd_extensions.sweetalert import SweetAlert
from plyer import filechooser

from libs.applibs import utils


class GetDetailsScreen(MDScreen):
    selected_template = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, interval):
        self.on_file_chooser_open = OnFileChooserOpen()
        menu_items = [{"text": primary_palette} for primary_palette in palette]
        self.primary_palette_menu = MDDropdownMenu(
            caller=self.ids.primary.ids.primary_palette,
            items=menu_items,
            width_mult=3,
        )
        self.primary_palette_menu.bind(on_release=self.set_primary_palette_item)

        self.accent_palette_menu = MDDropdownMenu(
            caller=self.ids.accent.ids.accent_palette,
            items=menu_items,
            width_mult=3,
        )
        self.accent_palette_menu.bind(on_release=self.set_accent_palette_item)

        hue_items = [{"text": hue_code} for hue_code in hue]

        self.primary_hue_menu = MDDropdownMenu(
            caller=self.ids.primary.ids.primary_hue,
            items=hue_items,
            width_mult=2,
        )
        self.primary_hue_menu.bind(on_release=self.set_primary_hue_item)

        self.accent_hue_menu = MDDropdownMenu(
            caller=self.ids.accent.ids.accent_hue,
            items=hue_items,
            width_mult=2,
        )
        self.accent_hue_menu.bind(on_release=self.set_accent_hue_item)

        theme_style_items = [
            {"text": theme_style} for theme_style in ["Light", "Dark"]
        ]
        self.theme_style_menu = MDDropdownMenu(
            caller=self.ids.theme_style.ids.theme_style,
            items=theme_style_items,
            width_mult=3,
        )
        self.theme_style_menu.bind(on_release=self.set_theme_style_item)

    def create_project(
        self,
        _application_title,
        _project_name,
        _application_version,
        _path_to_project,
        _author_name,
    ):
        (
            APPLICATION_TITLE,
            PROJECT_NAME,
            APPLICATION_VERSION,
            PATH_TO_PROJECT,
            AUTHOR_NAME,
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
            SweetAlert().fire("Please Fill Up All the Fields!", type="warning")
            return

        if " " in PROJECT_NAME:
            SweetAlert().fire(
                "Please Don't Use Space in Project Name", type="warning"
            )
            return

        FULL_PATH_TO_PROJECT = os.path.join(PATH_TO_PROJECT, PROJECT_NAME)
        if os.path.exists(FULL_PATH_TO_PROJECT):
            SweetAlert().fire("Folder Path Already Exists!")
            return

        if self.selected_template not in [
            "empty",
            "basic",
            "bottom-navigation",
        ]:
            SweetAlert().fire("This Template is Not Yet Available Now.")
            return

        project_name = PROJECT_NAME.lower()
        TEMPLATE_FOLDER = os.path.join("libs", "applibs", "templates")
        utils.copytree(
            os.path.join(TEMPLATE_FOLDER, "base"), FULL_PATH_TO_PROJECT
        )

        os.rename(
            os.path.join(FULL_PATH_TO_PROJECT, "project_name.py"),
            os.path.join(FULL_PATH_TO_PROJECT, f"{project_name}.py"),
        )

        if self.selected_template == "empty":
            pass
        elif self.selected_template == "basic":
            BASIC_KV_FILES = utils.get_files(
                os.path.join(TEMPLATE_FOLDER, "basic"), [".kv"]
            )
            for kv_file in BASIC_KV_FILES:
                shutil.copy(
                    kv_file,
                    os.path.join(FULL_PATH_TO_PROJECT, "libs", "uix", "kv"),
                )
        elif self.selected_template == "bottom-navigation":
            BOTTOM_NAV_FOLDER = os.path.join(
                TEMPLATE_FOLDER, "bottom-navigation"
            )
            BOTTOM_NAV_PY_FILES = utils.get_files(BOTTOM_NAV_FOLDER, [".py"])
            BOTTOM_NAV_KV_FILES = utils.get_files(BOTTOM_NAV_FOLDER, [".kv"])
            for py_file in BOTTOM_NAV_PY_FILES:
                shutil.copy(
                    py_file,
                    os.path.join(
                        FULL_PATH_TO_PROJECT, "libs", "uix", "baseclass"
                    ),
                )
            for kv_file in BOTTOM_NAV_KV_FILES:
                shutil.copy(
                    kv_file,
                    os.path.join(FULL_PATH_TO_PROJECT, "libs", "uix", "kv"),
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
                    "PRIMARY_PALETTE": self.ids.primary.ids.primary_palette.current_item,
                    "PRIMARY_HUE": self.ids.primary.ids.primary_hue.current_item,
                    "ACCENT_PALETTE": self.ids.accent.ids.accent_palette.current_item,
                    "ACCENT_HUE": self.ids.accent.ids.accent_hue.current_item,
                    "THEME_STYLE": self.ids.theme_style.ids.theme_style.current_item,
                },
            )

        SweetAlert().fire(
            "Congrat's",
            f"Project {PROJECT_NAME} Has Been Created Successfully!",
            type="success",
        )

    def set_primary_palette_item(self, instance_menu, instance_menu_item):
        self.ids.primary.ids.primary_palette.set_item(instance_menu_item.text)
        instance_menu.dismiss()

    def set_accent_palette_item(self, instance_menu, instance_menu_item):
        self.ids.accent.ids.accent_palette.set_item(instance_menu_item.text)
        instance_menu.dismiss()

    def set_primary_hue_item(self, instance_menu, instance_menu_item):
        self.ids.primary.ids.primary_hue.set_item(instance_menu_item.text)
        instance_menu.dismiss()

    def set_accent_hue_item(self, instance_menu, instance_menu_item):
        self.ids.accent.ids.accent_hue.set_item(instance_menu_item.text)
        instance_menu.dismiss()

    def set_theme_style_item(self, instance_menu, instance_menu_item):
        self.ids.theme_style.ids.theme_style.set_item(instance_menu_item.text)
        instance_menu.dismiss()

    def open_file_manager(self, text_input_instance):
        def _open_file_chooser(i):
            filechooser.choose_dir(on_selection=self.on_path_selection)
            text_input_instance.focus = False
            self.on_file_chooser_open.dismiss()

        if text_input_instance.focus:
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
