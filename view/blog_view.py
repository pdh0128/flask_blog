from flask import Flask, Blueprint, request, render_template, redirect
from control.posts import Posts
from control.user_ngmt import User

blog_abtest = Blueprint('blog', __name__)



def show_posts(order): 
    posts = Posts.get()
    if order == 'newer':
        posts = reversed(posts)
    return render_template("blog_A.html", posts=posts, order=order)


@blog_abtest.route("/") 
def main_older():  # 게시물을 오래된 순으로 보여줌
    return show_posts(order='older')

@blog_abtest.route("/newer") 
def main_newer():  # 게시물을 최근 순으로 보여줌
    return show_posts(order='newer')

@blog_abtest.route("/post<int:blog_id>")
def article(blog_id):
    post = Posts.search(blog_id)[0]
    return render_template('posts.html', post=post)
    
@blog_abtest.route("/login", methods=["GET", "POST"])  
def login_page():
    if request.method == "POST":  
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        
        user = User.find(user_email)
        # 로그인이 되어있는지 검증
        try:
            if user_email == user.user_email and user_password == user.user_password:
                return redirect("/blog")
        except AttributeError:
            return "로그인 실패"

    return render_template("login.html")  

@blog_abtest.route("/write", methods=["GET"])
def write():
    title = request.args.get("title")
    description = request.args.get("description")
    content = request.args.get("description")
    posts = Posts.create(title, description, content)
    return redirect("/blog")


@blog_abtest.route("/delete", methods=["GET"])
def delete():
    blog_id = request.args.get("id")
    posts = Posts.delete(blog_id)
    return redirect("/blog")


# @blog_abtest.route("/logined")
# def logined_page():
#     return redirect("/blog")
