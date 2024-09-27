from flask_login import UserMixin
from model.mysql import conn_mysqldb
from datetime import datetime

class User(UserMixin):
    
    def __init__(self, user_id, user_email, user_password,blog_id):
        self.id = user_id
        self.user_email = user_email
        self.user_password = user_password
        self.blog_id = blog_id
        
    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"select * from user info where user_id = {str(user_id)};"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id = user[0], user_email = user[1], user_password=user[2], blog_id=user[3])
        return user
    
    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = f"select * from user info where user_email = {str(user_email)};"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id = user[0], user_email = user[1], user_password=user[2], blog_id=user[3])
        return user
    
    @staticmethod
    def create(user_email, user_password, blog_id):
        user = User.find(user_email)
        if user == None:
            mysql_db = conn_mysqldb()
            db_curosor = mysql_db.cursor()
            sql = f"insert into user_info (user_email, user_password, blog_id) values ({str(user_email)}, {str(blog_id)}, {str(user_password)});"
            db_curosor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user