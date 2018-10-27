#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: cyp  date: 2018-10-13
import sys
import os




if __name__ == "__main__":
    # 在自己的脚本里访问django的数据库环境，用下面三行
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Crazy.settings')
    import django
    django.setup()
    from backend import main
    interactive_obj = main.ArgvHandler(sys.argv)
    interactive_obj.call()