
# coding: utf-8

# 比對規則：找出資料夾名稱的格式為 '[123456] ' 開頭，中括號內為 6 位數字，比對後取代為空字串。

import os
import re
for fn in os.listdir('.'):
    try:
        match = re.sub(r'^\[\d{6}\]\s', '',fn)
        print(match)
        os.rename(fn, match)
    except PermissionError as e:
        print(e)
        pass
