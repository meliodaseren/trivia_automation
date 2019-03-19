#!/usr/bin/env python
# coding: utf-8

import os
import shutil
import re

# 開頭比對
# 找出資料夾名稱的開頭格式為 '[123456] '
# 中括號內為 6 位數字，比對後取代為空字串。

# 結尾比對
# 找出資料夾名稱的結尾格式為 ' [320K+BK]' 或 ' [320K]' 或 ' [MP3]'
# 比對後取代為空字串。

folder_path = 'E:\BitComet Downloads'
rar_backup_path = "E:\\BitComet Downloads\\RAR_Backup"
files = os.listdir(folder_path)

if not os.path.exists(rar_backup_path):
    os.makedirs(rar_backup_path)

for file in files:
    if file.endswith('.rar'):
        shutil.move(os.path.join(folder_path, file), os.path.join(rar_backup_path, file))

for fn in os.listdir(folder_path):
    try:
        # [181017]
        match = re.sub(r'^\[\d{6}\]', '',fn)
        os.rename(fn, match)
        print("[INFO] 成功去除開頭之日期格式：" + match)
    except PermissionError as e:
        print("[ERROR]", e)
        pass
    except FileExistsError as e:
        print("[ERROR]", e)
        pass

for fn in os.listdir(folder_path):
    try:
        # [2016.10.28]
        match = re.sub(r'^\[\d{4}\.\d{2}\.\d{2}\]', '',fn)
        os.rename(fn, match)
        print("[INFO] 成功去除開頭之日期格式：" + match)
    except PermissionError as e:
        print("[ERROR]", e)
        pass
    except FileExistsError as e:
        print("[ERROR]", e)
        pass

for fn in os.listdir(folder_path):
    try:
        # [320K+BK], [320K], [MP3]
        match2 = re.sub(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', '',fn)
        match2 = re.sub(r'\[(320K.*|MP3.*)\]$', '',fn)
        os.rename(fn, match2)
        print("[INFO] 成功去除後綴格式：" + match2)
    except PermissionError as e:
        print("[ERROR]", e)
        pass
    except FileExistsError as e:
        print("[ERROR]", e)
        pass


for fn in os.listdir(folder_path):
    try:
        # 」／.*
        match3 = re.sub(r'」／.*', '」',fn)
        os.rename(fn, match3)
        print("[INFO] 成功去除後綴之歌手資訊：" + match3)
    except PermissionError as e:
        print("[ERROR]", e)
        pass
    except FileExistsError as e:
        print("[ERROR]", e)
        pass

if __name__ == '__main__':
    pass
