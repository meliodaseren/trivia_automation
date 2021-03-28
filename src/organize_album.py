#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import shutil
import re


def organize_album(folder_path):
    backup_path = f"{folder_path}\\backup"
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    for fn in os.listdir(folder_path):
        if fn == 'backup':
            continue
        # NOTE: move .rar/.mp4 to backup folder
        if fn.endswith('.rar'):
            shutil.move(f"{folder_path}\\{fn}", f"{backup_path}\\{fn}")
            continue
        elif fn.endswith('.mp4'):
            shutil.move(f"{folder_path}\\{fn}", f"{backup_path}\\{fn}")
            continue

        print(f"\nProcessing {fn}")
        print(f"|-- [Stage 1]")
        organize_folder(fn, folder_path)

        print(f"|-- [Stage 2]")
        rename_folder(fn, folder_path)


def organize_folder(fn, folder_path):
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
    except (PermissionError, FileExistsError) as e:
        print("[ERROR]", e, fn)


def rename_folder(fn, folder_path):
    try:
        fn_path = f"{folder_path}\\{fn}"
        match = fn

        #NOTE: [181017]
        if re.search(r'^\[\d{6}\]', match):
            match = re.sub(r'^\[\d{6}\]', '',match)
            
        #NOTE: [2016.10.28]
        if re.search(r'^\[\d{4}\.\d{2}\.\d{2}\]', match):
            match = re.sub(r'^\[\d{4}\.\d{2}\.\d{2}\]', '', match)

        #NOTE: [320K+BK], [320K], [MP3]
        if re.search(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', match):
            match = re.sub(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', '', match)

        #NOTE: Singer information
        if "『" in match:
            match = re.sub("『", "「", match)
        if "』" in match:
            match = re.sub("』", "」", match)
        if "」／" in match:
            match = re.sub(r'」／.*', '」', match)
        
        print(f"  Rename {fn_path}\n -> {folder_path}\\{match}")
        os.rename(f"{fn_path}", f"{folder_path}\\{match}")

    except (PermissionError, FileExistsError) as e:
        print("[ERROR]", e, fn)


if __name__ == '__main__':
    # folder_path = input("Please enter your path: ")
    folder_path = 'D:\\Downloads'

    organize_album(folder_path)

