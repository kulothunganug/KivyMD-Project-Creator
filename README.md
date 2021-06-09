<p align="center">
  <img height="128" src="https://github.com/Kulothungan16/KivyMD-Project-Creator/raw/main/assets/images/logo.png">
  <h1 align="center">KivyMD Project Creator</h1>
  <p align="center">A GUI Based Tool to Create Project for <a href="https://github.com/kivymd/KivyMD">KivyMD</a>.</p>
</p>

<br>

## Features
* Ready-to-start a new project with various templates and theme customization.
* After Creating the project, it provides a file named `hotreloader.py` that already setuped [`kaki`](https://github.com/tito/kaki/) for hot reload.
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

### Dependencies
- [Python](https://www.python.org/) 3.6+
- [Kivy](https://github.com/kivy/kivy) >= 2.0.0 ([Installation](https://kivy.org/doc/stable/gettingstarted/installation.html))
- [Plyer](https://github.com/kivy/plyer)
- [KivyMD](https://github.com/kivymd/KivyMD) >= 0.104.2.dev0 (from master branch)
- [SweetAlert](https://github.com/kivymd-extensions/sweetalert)
- [kaki](https://github.com/tito/kaki) for hotreloader

### Installation
```
git clone https://github.com/Kulothungan16/KivyMD_Project_Creator
cd KivyMD_Project_Creator
pip install https://github.com/kivymd/KivyMD/archive/master.zip
pip install -r requirements.txt
```
and run it via `python main.py`
