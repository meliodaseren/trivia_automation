#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile

class comic_ebook_generator:
    def __init__(self, path):
        self.path = path

    def zip_all_jpg(self, path):
        os.chdir(path)
        exception_list = ['backup', 'output', '.cbz']
        for folder in os.listdir(path):    
            for _except in exception_list:
                if _except in folder:
                    print(f'[WARN] ignore folder: {folder} in exception list')
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
                        print(f'zip {file} to {out_cbz}')
                        output_zip.write(os.path.join('.', file), file, zipfile.ZIP_DEFLATED)
                os.chdir(path)
                output_zip.close()
            else:
                print(f'[WARN] {dpath} is not a directory')
                continue


if __name__ == '__main__':
    folder_path = input('Please enter your path: ')
    obj = comic_ebook_generator(folder_path)
    obj.zip_all_jpg(folder_path)
