#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Required
- requests (必须)
- pillow (可选)
Info
- author : "ksel"
- date   : "2016.12.22"
'''

import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re
import time
import argparse

# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    "Host": "go.ruc.edu.cn",
    "Referer": "go.ruc.edu.cn/a70.htm",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='/home/nera/tool/cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

def login(secret, account):
    post_url = 'http://go.ruc.edu.cn'
    postdata = {
        'DDDDD': account,
        'upass': secret,
        'hid1': '',
        'hid2': '',
        '0MKKey': '123456',
        'R6': '0',
    }
    login_page = session.post(post_url, data=postdata, headers=headers)
    login_code = login_page.text
    if login_page.status_code == 200:
        print('Congratulations! You\'re logined in now!')
    #print(login_code)
    session.cookies.save()

try:
    input = raw_input
except:
    pass

def get_account_info():
    parser = argparse.ArgumentParser(
        prog="RUC-Login",
        usage="%(prog)s [-u <username> -p <password>]",
        description="RUC-Login v1"
    )

    parser.add_argument(
        "-u",
        "--username",
        dest="username",
        type=str,
        default=None,
        help="Username, i.e. your studet/teacher id"
    )

    parser.add_argument(
        "-p",
        "--password",
        dest="password",
        type=str,
        default=None,
        help="your password"
    )

    account_info = parser.parse_args()
    return account_info
        
if __name__ == '__main__':
    account_info = get_account_info()
    account, secret = account_info.username, account_info.password
    if account is None:
        account = input('请输入你的用户名：\n>  ')
    if secret is None:
        secret = input("请输入你的密码：\n>  ")
    login(secret, account)
