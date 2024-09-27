import pymongo

mongo_conn = pymongo.MongoClient('mongodb://localhost')

def conn_mongodb():
    try:
        mongo_conn.admin.command("ismaster")
        blog_db = mongo_conn['blog_session_db']['blog_ab']
    except:
       mongo_conn = pymongo.MongoClient('mongodb://localhost')
       blog_db = mongo_conn['blog_session_db']['blog_ab']
    return blog_db