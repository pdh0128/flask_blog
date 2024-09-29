from flask import Flask, Blueprint, request, render_template, redirect, session
from control.posts import Posts
from control.user_ngmt import User
from flask_login import login_user, current_user
blog_abtest = Blueprint('blog', __name__)



def show_posts(order): 
    if "title" in session:
        title = session['title']
        posts = Posts.search_title(title)
    else:
        posts = Posts.get()
        
    if order == 'newer':
            posts = reversed(posts)
    if current_user.is_authenticated:
        return render_template("blog_A.html", posts=posts, order=order, login=True)
    else:
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
    if current_user.is_authenticated : return render_template('posts.html', post=post, login=True)
    else : return render_template('posts.html', post=post)
    
@blog_abtest.route("/login", methods=["GET", "POST"])  
def login_page():
    if request.method == "POST":  
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        
        user = User.find(user_email)
        # DB에 있는 계정이 맞는지 검증
        if user != None:
            if user_email == user.user_email and user_password == user.user_password:
                login_user(user)
                return redirect("/blog")
            else:
                return redirect("/blog/login")
    return render_template("login.html")
        
@blog_abtest.route("/signup", methods=["GET", "POST"])  
def signup_page():
    if request.method == "POST": 
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        user = User.find(user_email)
        # DB에 있는 계정인지 확인
        if user != None:
            #이미 있는 계정
            print("이미 존재하는 계정입니다.")
            return render_template("signup.html", account=True)
        
        User.create(user_email, user_password)
        return redirect("/blog/login")

    return render_template("signup.html")

@blog_abtest.route("/write", methods=["GET"])
def write():
    title = request.args.get("title")
    description = request.args.get("description")
    content = request.args.get("content")
    posts = Posts.create(title, description, content)
    order = request.args.get("order")
    if order == 'newer':
        return redirect("/blog/newer")
    else:
        return redirect("/blog")


@blog_abtest.route("/delete", methods=["GET"])
def delete():
    blog_id = request.args.get("id")
    posts = Posts.delete(blog_id)
    order = request.args.get("order")
    if order == 'newer':
        return redirect("/blog/newer")
    else:
        return redirect("/blog")
    
@blog_abtest.route("/search", methods=["GET"])
def search():
    if "title" in session:
        del session['title']
    title = request.args.get("title")
    session['title'] = title
    return redirect("/blog")

@blog_abtest.route("/not_search")
def not_search():
    if "title" in session:
        del session['title']
    return redirect("/blog")

@blog_abtest.route("/post<int:blog_id>/update")
def update(blog_id):
    return render_template("post_update.html", blog_id=blog_id)

@blog_abtest.route("/post<int:blog_id>/updating", methods=["GET"])
def updating(blog_id):
    title = request.args.get("title")
    description = request.args.get("description")
    content = request.args.get("content")
    Posts.update(blog_id, title, description, content)
    return redirect(f"/blog/post{blog_id}")

@blog_abtest.route("/logout")
def logout():
    session.clear()
    return redirect("/blog")
