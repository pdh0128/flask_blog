from model.mongo import conn_mongodb
from datetime import datetime
class BlogSession():
    blog_page = {"A" : "blog_A.html", "B" : "blog_B.html"}
    session_cnt = 0;
    
    @staticmethod
    def save_session_info(session_ID, user_email, webpage_name):
        now = datetime.now().strptime("%Y/%m/%d %H:%m:%S")

        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            "session_ip" : session_ID,
            "user_email": user_email,
            "page":webpage_name,
            "access_time":now
        })
    
    @staticmethod
    def get_blog_page(blog_id=None):
        if blog_id == None:
            if not BlogSession.session_cnt:
                not BlogSession
                return "blog_A.html"
            else:
                not BlogSession
                return "blog_B.html"
        else:
            return BlogSession.blog_page[blog_id]