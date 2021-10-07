#!/usr/bin/evn python

import os
# import sys
# import shutil
import zipfile
import subprocess
from glob import glob


class PSD_zip_to_PNG:
    def __init__(self, path) -> None:
        self.path = path


    def zip_dir(self, inputpath):
        zf = zipfile.ZipFile('{path}', 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(inputpath):
            for filename in files:
                zf.write(os.path.join(root, filename))


    def unzip(self, inputpath, outputpath):
        try:
            zf = zipfile.ZipFile(inputpath, 'r')
            zf.extractall(outputpath)
        except NotImplementedError as e:
            print(f'[ERROR] {inputpath}, That compression method is not supported')
            pass


    def zip_list(self, inputpath):
        zf = zipfile.ZipFile(inputpath, 'r')
        print(zf.namelist())


    def unzip_iterator(self, inputpath):
        for filename in glob(f'{inputpath}{os.sep}*.zip'):
            dirname = os.path.splitext(filename)[0]
            if not os.path.exists(dirname):
                if zipfile.is_zipfile(filename):
                    print(f'[INFO] unzip {filename}')
                    self.unzip(filename, dirname)
                else:
                    print(f'[ERROR] {filename} is not zip')
            else:
                print(f'[WARN] {dirname} is exist')


    def convert_iterator(self, inputpath):
        os.chdir(inputpath)
        for subdir, dirs, files in os.walk('.'):
            for _ in files:
                if os.path.splitext(_)[1] == '.psd':
                    # psd_path = f'{subdir}{os.sep}{_}'
                    psd_path = f'{subdir}{os.sep}{_}[0]'
                    filename = os.path.splitext(_)[0]
                    png_path = f'{subdir}{os.sep}{filename}.png'

                    # Convert the .psd to .png by ImageMagick
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
        os.chdir(os.getcwd())


    def main(self):
        self.unzip_iterator(self.path)
        self.convert_iterator(self.path)


if __name__ == '__main__':

    workpath = input("Please enter your path: ")

    converter = PSD_zip_to_PNG(workpath)
    converter.main()

