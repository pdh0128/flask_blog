from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
# from flask_cors import CORS
import os
from view.blog_view import blog_abtest  
from control.user_ngmt import User

#https 프로토콜만을 지원하는 기능을 http 프로토콜로 테스트할 때 필요한 설정
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__, static_url_path="/static")
#CORS(app)
app.secret_key = "pdh0128_server"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"

app.register_blueprint(blog_abtest, url_prefix="/blog")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unathorized():
    return make_response(jsonify(success=False), 401)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='128', debug=True)