#!/bin/usr/env python
import os

class rename_jfif_to_jpg:
    """
    input the folder path
    recursively unzip all the *.zip and convert *.psd to *.png
    """
    def __init__(self, path) -> None:
        self.path = path

    def convert_iterator(self, inputpath):
        """ Convert the .jfif to .png """
        os.chdir(inputpath)
        for root, dirs, files in os.walk('.'):
            for _ in files:
                if os.path.splitext(_)[1] == '.jfif':
                    filename = os.path.splitext(_)[0]
                    filepath = os.path.join(root, _)
                    targetpath = os.path.join(root, f'{filename}.jpg')
                    print(f'rename {filepath} to {targetpath}')
                    os.rename(filepath, targetpath)
        os.chdir(os.getcwd())

    def main(self):
        self.convert_iterator(self.path)

if __name__ == '__main__':

    workpath = input("Please enter your path: ")
    converter = rename_jfif_to_jpg(workpath)
    converter.main()
