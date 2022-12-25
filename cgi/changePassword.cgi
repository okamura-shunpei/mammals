#!/usr/bin/python3
import cgi
import pymysql.cursors
import function
import hashlib
import os

form = cgi.FieldStorage()
msg = []
error = {}

if form.list == []:
    function.open_html("../html/changePassword.html", error=error)
else:
    account_id = form.getfirst("account_id")
    now_password = form.getfirst("now_password")
    new_password = form.getfirst("new_password")
    re_new_password = form.getfirst("re_new_password")
    sql_Users = f"select * from Users where account_id = '{account_id}'"
    result_Users = function.connection_sql(sql_Users, "r", "mammals")
    user_id = result_Users[0]["user_id"]
    sql_account_id = result_Users[0]["account_id"]
    user_password = result_Users[0]["user_password"]
    user_name = result_Users[0]["user_name"]
    mailAdress = result_Users[0]["mailAdress"]
    belong = result_Users[0]["belong"]
    admin_user = result_Users[0]["admin_user"]
    chief_user = result_Users[0]["chief_user"] 
    hash_now = hashlib.sha256(now_password.encode()).hexdigest()
    if new_password != re_new_password: 
        error["password"] = "新しいパスワードが一致しません\n"
        function.open_html("../html/changePassword.html", error=error)
    elif user_password != hash_now and user_password != "0000":
        error["password"] = "現在のパスワードが一致しません。ユーザー名あるいは現在のパスワードに誤りがあります\n"
        function.open_html("../html/changePassword.html", error=error)
    else:
        hash_new_password = hashlib.sha256(new_password.encode()).hexdigest()
        sql_changePassword = f"insert Users (user_id, account_id, user_password, mailAdress, belong, admin_user, chief_user) values ('{user_id}', '{sql_account_id}', '{hash_new_password}', '{mailAdress}', '{belong}', '{admin_user}', '{chief_user}') on duplicate key update user_password = '{hash_new_password}'"
        function.connection_sql(sql_changePassword, "w", "mammals")
        msg.append("パスワードが変更されました\n")
        function.open_html("../html/changePassword.html", msg=msg)
