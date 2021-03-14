import os
import shutil
import stat

from kivy.lang import Builder


def load_kv(file_name, file_path=os.path.join("libs", "uix", "kv")):
    with open(os.path.join(file_path, file_name), encoding="utf-8") as kv:
        Builder.load_string(kv.read())


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src, dst)
    lst = os.listdir(src)
    if ignore:
        excl = ignore(src, lst)
        lst = [x for x in lst if x not in excl]
    for item in lst:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if symlinks and os.path.islink(s):
            if os.path.lexists(d):
                os.remove(d)
            os.symlink(os.readlink(s), d)
            try:
                st = os.lstat(s)
                mode = stat.S_IMODE(st.st_mode)
                os.lchmod(d, mode)
            except Exception:
                pass  # lchmod not available
        elif os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def edit_file(in_file, out_file=None, values=None):

    with open(in_file) as f:
        string_file = f.read()

    if values:
        for key in values.keys():
            if not values[key]:
                continue
            string_file = string_file.replace(key, values[key])

        with open(out_file if out_file else in_file, "w") as f:
            f.write(string_file)


def get_files(path, ext):
    files = []

    for i in os.listdir(path):
        if os.path.splitext(i)[1] in ext:
            files.append(os.path.join(path, i))

    return files
