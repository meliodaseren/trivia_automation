#!/usr/bin/env python
# coding: utf-8

from os import listdir, rename
from re import sub

for fn in listdir('.'):
    try:
        match = sub(r'\.rar.*', '.rar',fn)
        rename(fn, match)
        print("[INFO] 成功去除格式：" + match)
    except PermissionError as e:
        print("[ERROR]", e)
        pass
    except FileExistsError as e:
        print("[ERROR]", e)
        pass

if __name__ == '__main__':
    pass
