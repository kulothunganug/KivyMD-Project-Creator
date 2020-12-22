# KivyMD Project Creator
A GUI Based Tool to Create Project for [KivyMD](https://github.com/kivymd/KivyMD).

## Features
* Ready-to-start a new project with various templates and theme customization.
* Automatically creates (optionally) `.gitignore`, `README.md`, `LICENSE` for `git` purposes.
* Creates `buildozer.spec` that already filled up.
* Gives better source code management (Folder Structure 👇).
```
project_name (Base Project Files)
|____libs (Code files)
| |____uix (UI files)
| | |____baseclass (PY files)
| | |____kv (KV files)
| | |____components (Custom UIX)
| |____applibs (Custom Modules files)
|____assets (Images and Font files)
```

## Dependencies
- [Python](https://www.python.org/) 3.6+
- [Kivy](https://github.com/kivy/kivy) >= 2.0.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Plyer](https://github.com/kivy/plyer)
- [KivyMD](https://github.com/kivymd/KivyMD) >= 0.104.2.dev0 (from master branch)
- [SweetAlert](https://github.com/kivymd-extensions/sweetalert)

## Installation
```
git clone https://github.com/Kulothungan16/KivyMD_Project_Creator
cd KivyMD_Project_Creator
pip install https://github.com/kivymd/KivyMD/archive/master.zip
pip install -r requirements.txt
```
and run it via `python main.py`
