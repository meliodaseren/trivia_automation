#!/usr/bin/env python

import os
# import glob
import shutil
import re


class album_organizer:
    def __init__(self, path) -> None:
        self.path = path


    def main(self, backup=True):
        if backup:
            self.backup_files(self.path)
        for fn in os.listdir(self.path):
            print(f"\nProcessing {fn}")
            print(f"|-- [Stage 1]")
            self.organize_album_dir(fn, self.path)
            print(f"|-- [Stage 2]")
            self.raname_album_dir(fn, self.path)


    def backup_files(self, folder_path):
        backup_path = f"{folder_path}\\backup"
        if not os.path.exists(backup_path):
            os.makedirs(backup_path)
        for fn in os.listdir(folder_path):
            if fn == 'backup':
                continue
            if fn.endswith('.rar'):
                shutil.move(f"{folder_path}\\{fn}", f"{backup_path}\\{fn}")
            elif fn.endswith('.mp4'):
                shutil.move(f"{folder_path}\\{fn}", f"{backup_path}\\{fn}")


    def organize_album_dir(self, fn, folder_path):
        try:
            fn_path = f"{folder_path}\\{fn}"
            print(f"   |-- [1-1] Remove *.url")
            # url_path = f"{fn_path}\\*.url"
            # url_glob = glob.glob(url_path)
            # for _ in url_glob:
            #     print(f"  Remove {_}")
            #     os.remove(_)
            for root, dirs, files in os.walk(fn_path):
                for _ in files:
                    if ".url" in _:
                        print(f"  Remove {_}")
                        os.remove(f"{fn_path}\\{_}")

            print(f"   |-- [1-2] Move MP3/file to previous folder, and remove empty folder")
            mp3_folder = f"{fn_path}\\MP3"
            if os.path.isdir(mp3_folder):
                for fn in os.listdir(mp3_folder):
                    filename = f"{mp3_folder}\\{fn}"
                    shutil.move(filename, fn_path)
                os.removedirs(mp3_folder)
        except (PermissionError, FileExistsError, FileNotFoundError) as e:
            print(e, fn)


    def raname_album_dir(self, fn, folder_path):
        print(f"   |-- [2-1] Rename the album folder")
        try:
            fn_path = f"{folder_path}\\{fn}"
            fn_new = f"{fn}"

            #NOTE: [181017]
            if re.search(r'^\[\d{6}\]', fn_new):
                fn_new = re.sub(r'^\[\d{6}\]', '',fn_new)
            #NOTE: [2016.10.28]
            if re.search(r'^\[\d{4}\.\d{2}\.\d{2}\]', fn_new):
                fn_new = re.sub(r'^\[\d{4}\.\d{2}\.\d{2}\]', '', fn_new)
            #NOTE: [320K+BK], [320K], [MP3]
            if re.search(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', fn_new):
                fn_new = re.sub(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', '', fn_new)
            #NOTE: Singer information
            if "『" in fn_new:
                fn_new = re.sub("『", "「", fn_new)
            if "』" in fn_new:
                fn_new = re.sub("』", "」", fn_new)
            if "」／" in fn_new:
                fn_new = re.sub(r'」／.*', '」', fn_new)

            if fn_new != fn:
                print(f"  Rename {fn_path}\n -> {folder_path}\\{fn_new}")
                os.rename(f"{fn_path}", f"{folder_path}\\{fn_new}")

        except (PermissionError, FileExistsError, FileNotFoundError) as e:
            print(e, fn)


if __name__ == '__main__':
    folder_path = input("Please enter your path: ")
    #folder_path = 'D:\\Downloads'
    obj = album_organizer(folder_path)
    obj.main(backup=False)

