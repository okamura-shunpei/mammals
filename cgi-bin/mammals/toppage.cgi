#!/usr/bin/python3
import cgi
import pymysql.cursors
import os
from http import cookies
import function

msg = []
cookie = function.get_user_name()

if cookie:
    user_name = cookie[0]["user_name"]
    msg.append(f"こんにちは{user_name}さん<a href='./changePassword.cgi'>パスワードの変更はこちら</a>")
    function.open_html("../../html/mammals/toppage.html", msg=msg)
else:
    print("Location:./login.cgi")