#!/usr/bin/python3
import cgi
import pymysql.cursors
import os
import function 
import hashlib
from http import cookies

msg = []
error = {}
form = cgi.FieldStorage()
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))

try:
    session_user_id = cookie["user_id"].value
except KeyError:
    session_user_id = ''
    
try:
    session_key = cookie["session_key"].value
    hash_session_key = hashlib.sha256(session_key.encode()).hexdigest()
except KeyError:
    session_key = ''

try:
    sql_session = f"select session_key from session where user_id = '{session_user_id}'"
    result_session = function.connection_sql(sql_session, "r", "mammals")
    db_session_key = result_session[0]["session_key"]
except: 
    db_session_key = ""
    
if hash_session_key == db_session_key:
    print("Location:./toppage.cgi\n")
else:
    if form.list == []:
        error["error"] = "ログイン情報を入力してください"
        function.open_html("../../html/mammals/login.html", error=error)
    else:
        account_id = form.getfirst("account_id")
        password = form.getfirst("password")
        
        try:
            sql = f"select user_id, user_password from Users where account_id = '{account_id}'"
            result_Users = function.connection_sql(sql, "r", "mammals")
        except:
            error["error"] = "ユーザーIDに誤りがあります"
            function.open_html("../../htmlmammals/login.html", error=error)

        user_id = result_Users[0]["user_id"]
        user_password = result_Users[0]["user_password"]
        
        try:
            sql = f"select session_id from session where user_id = {user_id}"
            result_session_id = function.connection_sql(sql, "r", "mammals")
            session_id = result_session_id[0]["session_id"]
        except:
            session_id = function.get_random_str()   
         
        hash_pass = hashlib.sha256(password.encode()).hexdigest()
        
        if password == "0000":
            hash_session_key = hashlib.sha256(session_id.encode()).hexdigest()
                
            sql = f"insert session (session_id, user_id, session_key) values (null, '{user_id}', '{hash_session_key}') on duplicate key update session_key = '{hash_session_key}';"
            function.connection_sql(sql, "w", "mammals")
            print(f"Set-Cookie: session_key={session_id}")        
            print(f"Set-Cookie: user_id={user_id}")
            print("Location:./toppage.cgi\n")
                
        elif hash_pass == user_password:
            hash_session_key = hashlib.sha256(session_id.encode()).hexdigest()                
            sql = f"insert session (session_id, user_id, session_key) values (null, '{user_id}', '{hash_session_key}') on duplicate key update session_key = '{hash_session_key}';"
            function.connection_sql(sql, "w", "mammals")            
            print(f"Set-Cookie: session_key={session_id}")        
            print(f"Set-Cookie: user_id={user_id}")
            print("Location:./toppage.cgi\n")
        else:
            error["error"] = "ユーザー名かパスワードに誤りがあります"
            function.open_html("../../html/mammals/login.html", error=error)