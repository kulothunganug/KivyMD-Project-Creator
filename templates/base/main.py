import json
import traceback

from kivy.factory import Factory
from project_name import PROJECT_NAME

__version__ = "APPLICATION_VERSION"

"""
Registering factories from factory.json.
"""
r = Factory.register

with open("factory_registers.json") as fd:
    custom_widgets = json.load(fd)
    for module, _classes in custom_widgets.items():
        for _class in _classes:
            r(_class, module=module)


try:
    PROJECT_NAME().run()
except Exception:
    error = traceback.format_exc()

    """
    If the app encounters an error it automatically saves the
    error in a file called ERROR.log.
    You can use this for BugReport purposes.
    """
    with open("ERROR.log", "w") as error_file:
        error_file.write(error)

    print(error)
