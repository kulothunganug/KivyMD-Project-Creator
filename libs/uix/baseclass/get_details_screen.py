import os

from kivy.clock import Clock
from kivy.properties import ColorProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivymd.color_definitions import hue, palette
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd_extensions.sweetalert import SweetAlert
from plyer import filechooser

from libs.applibs.utils import copytree, edit_file, get_files


class GetDetailsScreen(MDScreen):
    selected_template = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, interval):

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
        _project_title,
        _project_name,
        _version,
        _path_to_project,
        _author_name,
    ):
        (
            PROJECT_TITLE,
            PROJECT_NAME,
            APPLICATION_VERSION,
            PATH_TO_PROJECT,
            AUTHOR_NAME,
        ) = (
            _project_title.strip(),
            _project_name.strip(),
            _version.strip(),
            _path_to_project.strip(),
            _author_name.strip(),
        )
        if (
            len(PROJECT_TITLE)
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

        # Assinging custom variables
        project_name = PROJECT_NAME.lower()

        # popup = LoadingPopup()
        # popup_label = popup.ids.label
        # popup.open()

        # popup_label.text = "Copying project files"

        copytree("templates/base", FULL_PATH_TO_PROJECT)

        os.rename(
            os.path.join(FULL_PATH_TO_PROJECT, "project_name.py"),
            os.path.join(FULL_PATH_TO_PROJECT, f"{project_name}.py"),
        )

        # popup_label.text = "Editing files according to your needs"

        for file in get_files(FULL_PATH_TO_PROJECT):
            edit_file(
                in_file=file,
                values={
                    "PROJECT_TITLE": PROJECT_TITLE,
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

        # popup.dismiss()
        SweetAlert().fire(
            "Congrat's",
            f"Project {PROJECT_NAME} Has Been Created Successfully!",
            type="success",
        )

        # if self.selected_template == "backdrop":
        #     copytree("templates/backdrop", FULL_PATH_TO_PROJECT)
        # elif self.selected_template == "basic":
        #     copytree("templates/basic", FULL_PATH_TO_PROJECT)
        # elif self.selected_template == "bottom-nav":
        #     copytree("templates/bottom-nav", FULL_PATH_TO_PROJECT)
        # elif self.selected_template == "empty":
        #     pass
        # elif self.selected_template == "nav-drawer":
        #     copytree("templates/nav-drawer", FULL_PATH_TO_PROJECT)
        # elif self.selected_template == "tabs":
        #     copytree("templates/tabs", FULL_PATH_TO_PROJECT)

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
        if text_input_instance.focus:
            filechooser.choose_dir(on_selection=self.on_path_selection)
            text_input_instance.focus = False

    def on_path_selection(self, path):
        self.ids.path_to_project.text = path[0]

    def change_to_templates(self):
        self.manager.current = "templates"


class ColorWidget(BoxLayout):
    rgba_color = ColorProperty()


class LoadingPopup(ModalView):
    pass
