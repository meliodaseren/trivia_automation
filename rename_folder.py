
# coding: utf-8

# 開頭比對
# 找出資料夾名稱的開頭格式為 '[123456] '
# 中括號內為 6 位數字，比對後取代為空字串。

import os
import re
for fn in os.listdir('.'):
    try:
        match = re.sub(r'^\[\d{6}\]\s', '',fn)
        print("[INFO] 成功去除開頭格式：" + match)
        os.rename(fn, match)
    except PermissionError as e:
        print(e)
        pass

# 結尾比對
# 找出資料夾名稱的結尾格式為 ' [320K+BK]' 或 ' [320K]' 或 ' [MP3]'
# 比對後取代為空字串。

for fn in os.listdir('.'):
    try:
        match = re.sub(r'\[(320K\+BK|320K|MP3)\]$', '',fn)
        print("[INFO] 成功去除結尾格式：" + match)
        os.rename(fn, match)
    except PermissionError as e:
        print(e)
        pass
