from flask_login import UserMixin
from model.mysql import conn_mysqldb
from datetime import datetime

class Posts():
    
    def __init__(self, blog_id, title, description):
        self.blog_id = blog_id
        self.title = title
        self.description = description
        
    @staticmethod
    def get():
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"select * from posts;"
        db_cursor.execute(sql)
        posts = db_cursor.fetchall()
        return posts
    
    @staticmethod
    def search(blog_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"select * from posts where BLOG_ID = {blog_id};"
        db_cursor.execute(sql)
        posts = db_cursor.fetchall()
        return posts
    
    @staticmethod
    def current_get_id():
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"select BLOG_ID from posts order by desc;"
        db_cursor.execute(sql)
        id = db_cursor.fetchone()
        return id
    
    @staticmethod
    def create(title, description, content):
        now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        mysql_db = conn_mysqldb()
        db_curosor = mysql_db.cursor()
        sql = f"insert into posts(title, description, date, content) values('{title}', '{description}', '{now}', '{content}');"
        db_curosor.execute(sql)
        mysql_db.commit()
        return "Create Success"
    
    @staticmethod
    def delete(blog_id):
        mysql_db = conn_mysqldb()
        db_curosor = mysql_db.cursor()
        sql = f"delete from posts where BLOG_ID = {blog_id};"
        db_curosor.execute(sql)
        mysql_db.commit()
        return "delete Success"