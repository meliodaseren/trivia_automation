#!/usr/bin/evn python

import os
import sys
import zipfile
import subprocess
from glob import glob
import shutil


def zip_dir(path):
    zf = zipfile.ZipFile('{path}', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for filename in files:
            zf.write(os.path.join(root, filename))


def unzip(path, outputpath):
    try:
        zf = zipfile.ZipFile(path, 'r')
        zf.extractall(outputpath)
    except NotImplementedError as e:
        print(f'[ERROR] {path}, That compression method is not supported')
        pass


def zip_list(path):
    zf = zipfile.ZipFile(path, 'r')
    print(zf.namelist())


if __name__ == '__main__':

    workpath = '.'

    for filename in glob(f'{workpath}{os.sep}*.zip'):
        dirname = os.path.splitext(filename)[0]
        if not os.path.exists(dirname):
            if zipfile.is_zipfile(filename):
                print(f'[INFO] unzip {filename}')
                unzip(filename, dirname)
            else:
                print(f'[ERROR] {filename} is not zip')
        else:
            print(f'[WARN] {dirname} is exist')

    for subdir, dirs, files in os.walk(f'{workpath}'):
        for _ in files:
            if os.path.splitext(_)[1] == '.psd':
                # psd_path = f'{subdir}{os.sep}{_}'
                psd_path = f'{subdir}{os.sep}{_}[0]'
                filename = os.path.splitext(_)[0]
                png_path = f'{subdir}{os.sep}{filename}.png'

                # ImageMagick
                # https://imagemagick.org/script/download.php
                # https://imagemagick.org/script/convert.php
                if not os.path.exists(png_path):
                    # print(f'[INFO] convert {psd_path} -flatten {png_path}')
                    # os.system(f'convert {psd_path} -flatten {png_path}')
                    # subprocess.Popen(f'convert {psd_path} -flatten {png_path}')

                    print(f'[INFO] convert {psd_path} {png_path}')
                    # os.system(f'convert {psd_path} {png_path}')
                    p = subprocess.Popen(f'convert {psd_path} {png_path}', shell=True)
                    p.wait()
                else:
                    pass
                    # print(f'[WARN] {png_path} is exist')
