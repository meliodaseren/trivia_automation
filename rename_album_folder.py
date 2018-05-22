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

for fn in listdir('.'):
    try:
        match = sub(r'^\[\d{6}\]\s', '',fn)
        rename(fn, match)
        print("[INFO] 成功去除開頭格式：" + match)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass

for fn in listdir('.'):
    try:
        match2 = sub(r'\[(320K\+BK|320K|MP3)\]$', '',fn)
        rename(fn, match2)
        print("[INFO] 成功去除結尾格式 1：" + match2)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass

for fn in listdir('.'):
    try:
        match3 = sub(r'」／.*', '」',fn)
        rename(fn, match3)
        print("[INFO] 成功去除結尾格式 2：" + match3)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass
