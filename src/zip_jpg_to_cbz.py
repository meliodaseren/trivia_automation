#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import zipfile
# from glob import glob


def zip_all_jpg(path):
    os.chdir(path)
    for folder in os.listdir(path):
        if folder == 'backup' or folder == 'output' or '.cbz' in folder:
            print(f'[WARN] ignore folder: {folder}')
            continue

        if os.path.exists(f'{folder}.cbz'):
            print(f'[WARN] ignore folder: {folder}.cbz already exists')
            continue

        dpath = f'{path}\\{folder}'
        if os.path.isdir(dpath):    
            out_cbz = f'{folder}.cbz'
            output_zip = zipfile.ZipFile(out_cbz, 'w')
            os.chdir(dpath)
            for file in os.listdir(dpath):
                if '.png' in file or '.jpg' in file:
                    # file = f'{dpath}\\{file}'
                    print(f"zip {file} to {out_cbz}")
                    output_zip.write(os.path.join('.', file), file, zipfile.ZIP_DEFLATED)
            os.chdir(path)
            output_zip.close()
        else:
            print(f'[WARN] {folder} is not a directory')
            continue


if __name__ == '__main__':
    # folder_path = input("Please enter your path: ")
    folder_path = 'E:\\kobo ebook'
    zip_all_jpg(folder_path)
