from flask import Flask, Blueprint, request, render_template, redirect

blog_abtest = Blueprint('blog', __name__)
posts = [{
        "BLOG_ID" : 1,
        "title" : "박동현 그는 ..",
        "description" : "뛰어난..",
        "date" : "2024/09/26 12:20:21"
    },
    {
        "BLOG_ID": 2,
        "title": "두 번째 블로그 포스트",
        "description": "더 많은 내용..",
        "date": "2024/09/27 12:20:22"
        }]


@blog_abtest.route("/")
def main():
    return render_template("blog_A.html", posts=posts)

@blog_abtest.route("/login", methods=["GET", "POST"])  
def login_page():
    if request.method == "POST":  
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        
        # 어드민 검증
        if user_email == "admin@donghyunmail.com" and user_password == "1234":
            return redirect("/blog")
        else:
            return "로그인 실패"

    return render_template("login.html")  

# @blog_abtest.route("/logined")
# def logined_page():
#     return redirect("/blog")
