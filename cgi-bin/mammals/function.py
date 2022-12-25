import os
import sys
import random, string
import pymysql.cursors
import hashlib
from collections import defaultdict
from http import cookies

#受け取った引数分の文字数のランダムな文字列を戻り値として出力する関数
def get_random_str(n):
	char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
	return ''.join([random.choice(char_data) for i in range(n)])

#session_keyをsha256でハッシュ化して出力する関数
def generate_hash_session_key():
    session = get_random_str(100)
    session_key = hashlib.sha256(session.encode()).hexdigest()
    return session_key    

#sqlの接続を行う関数　第一引数でsqlの命令、第二引数で読み込みか書き込みのどちらか、第三引数でデータベース名を受け取る
def connection_sql(sql, mode, db):
    connection = pymysql.connect(
        host='localhost',
        user='test_user',
        password='password',
        database=db,
        charset = "utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )                     

    if mode == "w":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
            connection.commit()

                
    elif mode =="r":
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result

#得られたクッキーからユーザー名を特定し戻り値として出力する関数
def get_user_name():
    cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ''))
    try:
        session_key = cookie["session_key"].value
    except KeyError:
        session_key = ''
    
    sql =f"select user_name from Users natural inner join session where session_key = '{session_key}'"
    cookie_user = connection_sql(sql, "r", "mammals") 
    return cookie_user

#htmlファイルを読み込んでcgiの変数を反映して出力する関数
def open_html(html_path, msg=[""], error={}):
    with open(html_path, mode="r", encoding="utf-8") as html:
        print("Content-Type: text/html\n")
        data = defaultdict(lambda: str())
        for i, j in error.items():
            data[i] = j
        print(html.read().format(msg, data))