#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
# import sys
# import shutil
# import zipfile
# import subprocess
from glob import glob
from os import listdir, rename


def rename_rar(folder_path):
    for fn in listdir(folder_path):
        try:
            if re.search(r'\.rar.*', fn):
                match = re.sub(r'\.rar.*', '.rar', fn)
                print(fn, match)
                rename(f"{folder_path}\\{fn}", f"{folder_path}\\{match}")
                print("[INFO] remove rar postfix" + match)
        except PermissionError as e:
            print("[ERROR]", e)
        except FileExistsError as e:
            print("[ERROR]", e)


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

'''
if __name__ == '__main__':
    startpath = input("Please enter your path: ")
    list_files(startpath)

    # if startpath:
    #     rename_rar(startpath)
    # else:
    #     rename_rar(".")
'''