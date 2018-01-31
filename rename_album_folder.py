# coding: utf-8

import os
import re

# 開頭比對
# 找出資料夾名稱的開頭格式為 '[123456] '
# 中括號內為 6 位數字，比對後取代為空字串。

# 結尾比對
# 找出資料夾名稱的結尾格式為 ' [320K+BK]' 或 ' [320K]' 或 ' [MP3]'
# 比對後取代為空字串。

for fn in os.listdir('.'):
    try:
        match = re.sub(r'^\[\d{6}\]\s', '',fn)
        os.rename(fn, match)
        print("[INFO] 成功去除開頭格式：" + match)

        match2 = re.sub(r'」／.*', '」',fn)
        os.rename(fn, match2)
        match3 = re.sub(r'\[(320K\+BK|320K|MP3)\]$', '',fn)
        os.rename(fn, match3)
        print("[INFO] 成功去除結尾格式：" + match3)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass
