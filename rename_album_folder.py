#!/usr/bin/env python
# coding: utf-8

from os import rename, listdir
from re import sub

# 開頭比對
# 找出資料夾名稱的開頭格式為 '[123456] '
# 中括號內為 6 位數字，比對後取代為空字串。

# 結尾比對
# 找出資料夾名稱的結尾格式為 ' [320K+BK]' 或 ' [320K]' 或 ' [MP3]'
# 比對後取代為空字串。

folder_path = 'E:\BitComet Downloads'

for fn in listdir(folder_path):
    print(fn)

for fn in listdir(folder_path):
    try:
        # [181017]
        match = sub(r'^\[\d{6}\]', '',fn)
        rename(fn, match)
        print("[INFO] 成功去除開頭之日期格式：" + match)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass

for fn in listdir(folder_path):
    try:
        # [2016.10.28]
        match = sub(r'^\[\d{4}\.\d{2}\.\d{2}\]', '',fn)
        rename(fn, match)
        print("[INFO] 成功去除開頭之日期格式：" + match)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass

for fn in listdir(folder_path):
    try:
        # [320K+BK], [320K], [MP3]
        match2 = sub(r'\[(320K\+BK|320K|MP3|MP3\s320K|MP3\s320K\+BK)\]$', '',fn)
        match2 = sub(r'\[(320K.*|MP3.*)\]$', '',fn)        
        rename(fn, match2)
        print("[INFO] 成功去除後綴格式：" + match2)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass


for fn in listdir(folder_path):
    try:
        # 」／.*
        match3 = sub(r'」／.*', '」',fn)
        rename(fn, match3)
        print("[INFO] 成功去除後綴之歌手資訊：" + match3)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass
