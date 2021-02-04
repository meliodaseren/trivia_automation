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
        print(f"|-- [Stage 1] Remove prefix")
        organize_folder(fn, folder_path)

        print(f"|-- [Stage 2] Remove prefix")
        remove_prefix(fn, folder_path)

        print(f"|-- [Stage 3] Remove suffix")
        remove_suffix(fn, folder_path)

        print(f"|-- [Stage 4] Remove singer information")
        remove_singer_info(fn, folder_path)


def organize_folder(fn, folder_path):
    try:
        fn_path = f"{folder_path}\\{fn}"

        print(f"   |-- [1-1] Remove *.url")
        url_path = f"{fn_path}\\*.url"
        url_glob = glob.glob(url_path)
        for _ in url_glob:
            print(f"  Remove {_}")
            os.remove(_)

        print(f"   |-- [1-2] Move MP3/file to previous folder, and remove empty folder")
        mp3_folder = f"{fn_path}\\MP3"
        if os.path.isdir(mp3_folder):
            for fn in os.listdir(mp3_folder):
                filename = f"{mp3_folder}\\{fn}"
                shutil.move(filename, fn_path)
            os.removedirs(mp3_folder)
    except (PermissionError, FileExistsError) as e:
        print("[ERROR]", e, fn)


def remove_prefix(fn, folder_path):
    try:
        fn_path = f"{folder_path}\\{fn}"
        #NOTE: [181017]
        match = re.sub(r'^\[\d{6}\]', '',fn)
        os.rename(f"{fn_path}", f"{folder_path}\\{match}")

        #NOTE: [2016.10.28]
        match = re.sub(r'^\[\d{4}\.\d{2}\.\d{2}\]', '',fn)
        os.rename(f"{fn_path}", f"{folder_path}\\{match}")
    except (PermissionError, FileExistsError) as e:
        print("[ERROR]", e, fn)


def remove_suffix(fn, folder_path):
    try:
        fn_path = f"{folder_path}\\{fn}"
        #NOTE: [320K+BK], [320K], [MP3]
        if re.search(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', fn):
            match = re.sub(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', '', fn)
            os.rename(f"{fn_path}", f"{folder_path}\\{match}")
    except (PermissionError, FileExistsError) as e:
        print("[ERROR]", e, fn)


def remove_singer_info(fn, folder_path):
    try:
        fn_path = f"{folder_path}\\{fn}"
        if "『" in fn or "』" in fn:
            fn_new_path = fn_path.replace("『", "「").replace("』", "」")
            print(f"  Rename {fn_path}\n  ->  {fn_new_path}")
            os.rename(f"{fn_path}", f"{fn_new_path}")
        if "」／" in fn:
            match = re.sub(r'」／.*', '」',fn)
            print(f"  Rename {fn_path} -> {folder_path}\\{match}")
            os.rename(f"{fn_path}", f"{folder_path}\\{match}")
    except (PermissionError, FileExistsError) as e:
        print("[ERROR]", e, fn)


if __name__ == '__main__':
    # folder_path = input("Please enter your path: ")
    folder_path = 'D:\\Downloads'

    organize_album(folder_path)

