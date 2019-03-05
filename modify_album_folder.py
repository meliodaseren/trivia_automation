#!/usr/bin/env python
# coding: utf-8

import os
import glob
import shutil
import re

folder_path = "E:\\BitComet Downloads"
dirs = os.listdir(folder_path)

rar_backup_path = "E:\\BitComet Downloads\\RAR_Backup"
if not os.path.exists(rar_backup_path):
    os.makedirs(rar_backup_path)

for dir in dirs:
    
    if dir.endswith('.rar'):
        #shutil.move(os.path.join(folder_path, dir), os.path.join(rar_backup_path, dir))
        shutil.move(f"{folder_path}\\{dir}", f"{rar_backup_path}\\{dir}")

    dir_path = f"{folder_path}\\{dir}"
    print("[INFO] Processing", dir)

    print("[Stage 1-1] Check the *.url in folder")
    if dir.endswith('.url'):
        print(dir)
        #os.remove()
    '''
    url_path = f"{dir_path}\\*.url"
    url_glob = glob.glob(url_path)
    print("[INFO]", url_path, url_glob)
    for _ in url_glob:
        print(_)
        os.remove(_)
    '''

    print("[Stage 1-2] Move MP3 file to previous folder, and remove empty folder")
    mp3_folder = f"{folder_path}\\{dir}\\MP3"
    if os.path.isdir(mp3_folder):
#        print("[INFO] MP3 folder is exist", mp3_folder)
        file_in_mp3_folder_list = os.listdir(mp3_folder)
        for f in file_in_mp3_folder_list:
            filename = f"{mp3_folder}\\{f}"
            shutil.move(filename, dir_path)
        os.removedirs(mp3_folder)

    print("[Stage 1-3] Replace『』to「」")
    dir_new = dir.replace("『", "「").replace("』", "」")
    os.rename(f"{folder_path}\\{dir}", f"{folder_path}\\{dir_new}")


print("[Stage 2] Remove the prefix and sufix of album folder")
# 開頭比對
# 找出資料夾名稱的開頭格式為 '[123456] '
# 中括號內為 6 位數字，比對後取代為空字串。

# 結尾比對
# 找出資料夾名稱的結尾格式為 ' [320K+BK]' 或 ' [320K]' 或 ' [MP3]'
# 比對後取代為空字串。

for fn in os.listdir(folder_path):
    if fn == 'RAR_Backup': continue
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
    if fn == 'RAR_Backup': continue
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

for fn in os.listdir(folder_path):
    if fn == 'RAR_Backup': continue
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

for fn in os.listdir(folder_path):
    if fn == 'RAR_Backup': continue
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
