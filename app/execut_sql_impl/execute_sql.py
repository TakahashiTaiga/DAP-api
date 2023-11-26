import mysql.connector
from mysql.connector import errorcode


class executeSql():

    def __init__(self):
        # configファイルか環境変数にする
        self.mysql_user = 'root'
        self.mysql_pass = 'mysqlpassword'
        self.mysql_port = 13306
        self.mysql_db = 'prototype_db'
        self.cursor

    def create_connection(self):
        try:
            conn = mysql.connector.connect(
                user=self.mysql_user,
                password=self.mysql_pass,
                port=self.mysql_port,
                database=self.mysql_db
            )
            self.cursor = conn.cursor(dictionary=True)

        except mysql.connector.Error as err:
            print('error')
            print(err)

    def execute_sql(self, query):
        try:
            conn = mysql.connector.connect(
                user=self.mysql_user,
                password=self.mysql_pass,
                port=self.mysql_port,
                database=self.mysql_db
            )
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()

            return result

        except mysql.connector.Error as err:
            print('error')
            print(err)

    def close_coonnection(self):
        try:
            self.cursor.close()
        except mysql.connector.Error as err:
            print('error')
            print(err)
