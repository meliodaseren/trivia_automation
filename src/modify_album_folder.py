#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import shutil
import re

def organize_album_folders(folder_path):
    for fn in os.listdir(folder_path):
        # Backup the specific files
        if fn.endswith('.rar'):
            shutil.move(f"{folder_path}\\{fn}", f"{backup_path}\\{fn}")
            continue
        elif fn.endswith('.mp4'):
            shutil.move(f"{folder_path}\\{fn}", f"{backup_path}\\{fn}")
            continue
        elif fn.endswith('.avi'):
            shutil.move(f"{folder_path}\\{fn}", f"{backup_path}\\{fn}")
            continue

        fn_path = f"{folder_path}\\{fn}"
        print("[INFO] Processing", fn)

        print("[Stage 1-1] Check the *.url in folder")
        #if fn.endswith(f'{fn_path}\\.url'):
            #print(fn)
            #os.remove()
        
        url_path = f"{fn_path}\\*.url"
        url_glob = glob.glob(url_path)
        #print("[INFO]", url_path, url_glob)
        for _ in url_glob:
            print(f"Remove the {_}")
            os.remove(_)

        print("[Stage 1-2] Move MP3 file to previous folder, and remove empty folder")
        mp3_folder = f"{folder_path}\\{fn}\\MP3"
        if os.path.isdir(mp3_folder):
    #        print("[INFO] MP3 folder is exist", mp3_folder)
            for fn in os.listdir(mp3_folder):
                filename = f"{mp3_folder}\\{fn}"
                shutil.move(filename, fn_path)
            os.removedirs(mp3_folder)

        print("[Stage 1-3] Replace『』to「」")
        fn_new = fn.replace("『", "「").replace("』", "」")
        os.rename(f"{folder_path}\\{fn}", f"{folder_path}\\{fn_new}")

def remove_date_postfix(folder_path):
    '''
    找出資料夾名稱的開頭格式為 '[123456] '
    中括號內為 6 位數字，比對後取代為空字串。
    '''
    for fn in os.listdir(folder_path):
        if fn == 'backup': continue
        try:
            # [181017]
            match = re.sub(r'^\[\d{6}\]', '',fn)
            os.rename(f"{folder_path}\\{fn}", f"{folder_path}\\{match}")
            #print("[INFO] 成功去除開頭之日期格式：" + match)
        except PermissionError as e:
            print("[ERROR]", e)
            pass
        except FileExistsError as e:
            print("[ERROR]", e)
            pass

    for fn in os.listdir(folder_path):
        if fn == 'backup': continue
        try:
            # [2016.10.28]
            match = re.sub(r'^\[\d{4}\.\d{2}\.\d{2}\]', '',fn)
            os.rename(f"{folder_path}\\{fn}", f"{folder_path}\\{match}")
            #print("[INFO] 成功去除開頭之日期格式：" + match)
        except PermissionError as e:
            print("[ERROR]", e)
            pass
        except FileExistsError as e:
            print("[ERROR]", e)
            pass

def remove_suffix(folder_path):
    '''
    找出資料夾名稱的結尾格式為 ' [320K+BK]' 或 ' [320K]' 或 ' [MP3]'
    比對後取代為空字串。
    '''
    for fn in os.listdir(folder_path):
        if fn == 'backup': continue
        try:
            # [320K+BK], [320K], [MP3]
            match = re.sub(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', '',fn)
            #match = re.sub(r'\[(320K.*|MP3.*)\]$', '',fn)
            os.rename(f"{folder_path}\\{fn}", f"{folder_path}\\{match}")
            #print("[INFO] 成功去除後綴格式：" + match)
        except PermissionError as e:
            print("[ERROR]", e)
            pass
        except FileExistsError as e:
            print("[ERROR]", e)
            pass

def remove_singer_info(folder_path):
    for fn in os.listdir(folder_path):
        if fn == 'backup': continue
        try:
            # 」／.*
            match = re.sub(r'」／.*', '」',fn)
            os.rename(f"{folder_path}\\{fn}", f"{folder_path}\\{match}")
            #print("[INFO] 成功去除後綴之歌手資訊：" + match)
        except PermissionError as e:
            print("[ERROR]", e)
            pass
        except FileExistsError as e:
            print("[ERROR]", e)
            pass

if __name__ == '__main__':
    folder_path = input("Please enter your path: ")
    backup_path = f"{folder_path}\\backup"
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
    
    print("[Stage 1] Organize album folder")
    organize_album_folders(folder_path)
    remove_date_postfix(folder_path)

    print("[Stage 2] Remove the prefix and suffix of album folder")
    remove_suffix(folder_path)
    remove_singer_info(folder_path)
