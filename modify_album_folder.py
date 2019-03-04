#!/usr/bin/env python
# coding: utf-8

import os
import glob
import shutil
#import sys
#import re

folder_path = "G:\\Google 雲端硬碟\\ACGMusic\\190106_backup"
dirs = os.listdir(folder_path)
for dir in dirs:
    dir_path = f"{folder_path}\\{dir}"
#    print("[INFO]", dir_path)

    # NOTE: [Stage 1] Check the *.url in folder
    print("[Stage 1] Check the *.url in folder")
    url_path = f"{dir_path}\\*.url"
    url_glob = glob.glob(url_path)
    for _ in url_glob:
        os.remove(_)
#    print("[INFO]", url_glob)

    # NOTE: [Stage 2] Move MP3 file to previous folder
    print("[Stage 2] Move MP3 file to previous folder, and remove empty folder")
    mp3_folder = f"{folder_path}\\{dir}\\MP3"
    if os.path.isdir(mp3_folder):
#        print("[INFO] MP3 folder is exist", mp3_folder)
        file_in_mp3_folder_list = os.listdir(mp3_folder)
        for f in file_in_mp3_folder_list:
            filename = f"{mp3_folder}\\{f}"
            shutil.move(filename, dir_path)
        os.removedirs(mp3_folder)

    # NOTE: [Stage 3] Replace『』to「」
    print("[Stage 3] Replace『』to「」")
    dir_new = dir.replace("『", "「").replace("』", "」")
    os.rename(f"{folder_path}\\{dir}", f"{folder_path}\\{dir_new}")
