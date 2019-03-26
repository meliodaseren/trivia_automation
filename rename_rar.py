#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir, rename
import re

def rename_rar(folder_path):
    for fn in listdir(folder_path):
        try:
            if re.search(r'\.rar.*', fn):
                match = re.sub(r'\.rar.*', '.rar', fn)
                print(fn, match)
                rename(f"{folder_path}\\{fn}", f"{folder_path}\\{match}")
                print("[INFO] 成功去除格式：" + match)
        except PermissionError as e:
            print("[ERROR]", e)
            pass
        except FileExistsError as e:
            print("[ERROR]", e)
            pass

if __name__ == '__main__':
    folder_path = input("Please enter your path: ")
    rename_rar(folder_path)
