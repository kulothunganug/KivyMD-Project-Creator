import os

folder = os.path.dirname(os.path.realpath(__file__))


def format(path):
    dirs = os.listdir(folder + f"/{path}")

    for i in dirs:
        if ".py" in i:
            os.system(f"python3.9 -m black {folder}/{path}/{i}")
            os.system(f"python3.9 -m isort {folder}/{path}/{i}")


format(".")
