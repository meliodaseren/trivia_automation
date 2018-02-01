# coding: utf-8

import os
import re

for fn in os.listdir('.'):
    try:
        match = re.sub(r'rar.*', 'rar',fn)
        os.rename(fn, match)
        print("[INFO] 成功去除格式：" + match)
    except PermissionError as e:
        print(e)
        pass
    except FileExistsError as e:
        print(e)
        pass
