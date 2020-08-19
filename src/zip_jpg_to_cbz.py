#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import zipfile


def zip_all_jpg(input_path, output_path):
    for folder in os.listdir(input_path):
        if os.path.isdir(folder):
            out_cbz = f'{folder}.cbz'
            zip_1 = zipfile.ZipFile(out_cbz, 'w')
            for file in os.listdir(f'{input_path}/{folder}'):
                # file = f'{input_path}/{folder}/{file}'
                os.chdir(f'{input_path}/{folder}')
                print(f"zip {file} to {out_cbz}")
                zip_1.write(os.path.join('.', file), file, zipfile.ZIP_DEFLATED)
                os.chdir(output_path)
            zip_1.close()
        else:
            # print(f'{folder} is not directory')
            pass


def rename_rar(input_path):
    for fn in os.listdir(input_path):
        try:
            if re.search(r'\.zip.*', fn):
                match = re.sub(r'\.zip.*', '.cbz', fn)
                print(fn, match)
                os.rename(f"{input_path}\\{fn}", f"{input_path}\\{match}")
                print("[INFO] rename zip to cbz" + match)
        except PermissionError as e:
            print("[ERROR]", e)
        except FileExistsError as e:
            print("[ERROR]", e)


if __name__ == '__main__':
    # folder_path = input("Please enter your path: ")
    input_folder = 'G:\Kobo Forma'
    output_folder = 'G:\Kobo Forma'

    zip_all_jpg(input_folder, output_folder)

    # if folder_path:
    #     rename_rar(folder_path)
    # else:
    #     rename_rar(".")
