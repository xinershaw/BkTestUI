# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
import MySQLdb as Db


class DB(object):
    def __init__(self, db_name):
        self.db_host = '192.168.3.201'
        self.db_port = 3306
        self.db_user = 'xiaoxin'
        self.db_pwd = '111111'
        self.db_name = db_name

        self.conn = self.open_connection()

    def open_connection(self):
        try:
            db = Db.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_user,
                passwd=self.db_pwd,
                db=self.db_name,
                charset='utf8'
                )
            return db
        except Exception as e:
            print "连接数据库失败！", e

    def query(self, sql_string):
        cursor = self.conn.cursor()
        result = None
        try:
            cursor.execute(sql_string)
            result = cursor.fetchall()
        except Exception as e:
            print "数据库查询失败！", e
        finally:
            cursor.close()
            self.conn.close()
            return result