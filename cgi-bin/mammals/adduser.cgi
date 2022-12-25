import cgi 
import function
import pymysql.cursors
import os
from http import cookies

form = cgi.FieldStorage()
error = {}
msg = []

cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))

if cookie:
    try:
        user_id = cookie["user_id"].value
    except KeyError:
        print("Location:./login.cgi")
    
    try:
        sql_admin = f"select admin_user from Users user_id = '{user_id}'"
        admin_user = function.connection_sql(sql_admin, "r", "mammals")
    except:
        print("Location:./toppage.cgi")
    
    if admin_user == "1":
        if form.list == []:
            msg.append("ユーザー情報を入力してください")
            function.open_html("../../html/mammals/adduser.html", msg)
        else:
            account_id = form.getfirst("account_id")
            user_password = form.getfirst("user_password")
            password_comf = form.getfirst("password_comf")
            user_name = form.getfirst("user_name")
            pronunciation = form.getfirst("pronunciation")
            mailAdress = form.getfirst("mailAdress")
            belong = form.getfirst("belong")
            admin_user = form.getfirst("admini_user")
            chief_user = form.getfirst("chief_user")
            
            if user_password == password_comf:
                sql_Users = "insert Users(user_id, account_id, user_password, user_name, pronunciation, mailAdress, belong, admin_user, chief_user)"
                sql_Users += f"values(null, '{account_id}', '{user_password}', '{user_name}', '{pronunciation}', '{mailAdress}', '{belong}', '{admin_user}', '{chief_user}');"
                function.connection_sql(sql_Users, "w", "mammals")
                
                msg.append(f"{account_id}を登録しました")
                function.open_html("../../html/mammals/adduser_success.html", msg=msg)
                
            else:
                error["error"] = "パスワードと確認用パスワードが一致しません"
                function.open_html("../../html/mammals/adduser.html")
    else:
        print("Location:./toppage.cgi")
else:
    print("Location:./login.cgi")
    