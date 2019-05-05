#!/usr/bin/python3
# _*_coding:utf-8 _*_
# 创建时间: 2019/4/11 10:20  
# 创建人员: 廖志妹

import json
import sys
sys.path.append('/Cookie/')

def get_Cookie():
    str = ''
    with open('tycookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    cookie = [item["name"] + "=" + item["value"] for item in listCookies]
    cookiestr = '; '.join(item for item in cookie)
    print(cookiestr)
    return cookiestr

def getCookies():
    with open('tycookies.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    return listCookies

