# -*- coding: utf-8 -*-
import flask as fl
from members.tool import *
from members.models import User
from members.controller.UserController import UserController
from members.database import db_session
from werkzeug.security import generate_password_hash, check_password_hash

bp = fl.Blueprint('member', __name__, url_prefix="/member")

@bp.route('/')
def root():
    return fl.render_template("member/index.html")

@bp.route("/login")
def login():
    if 'userinfo' in fl.session:
        return alert_and_redirect("이미 로그인 되었습니다.", "/")
    return fl.render_template("member/login.html", title="로그인")

@bp.route("/login/check", methods=['POST'])
def logincheck():
    userid = fl.request.form.get("userid")
    userpw = fl.request.form.get("userpassword")

    if userid is "" or userpw is "":
        return "사용자 정보가 필요합니다"

    controller = UserController(db=db_session)
    login = controller.check_user(userid, userpw)
    if login is True:
        return alert_and_redirect("로그인 되었습니다." , "/")

    return alert_and_redirect("로그인 실패 " , fl.url_for("member.login"))


@bp.route("/logout")
def logout():
    if 'userinfo' in fl.session:
        fl.session.pop('userinfo', None)
        return alert_and_redirect("로그아웃 되었습니다..", "/")

    return alert_and_redirect("로그인 부터 진행해주세요. " , fl.url_for("member.login"))

@bp.route("/join")
def join():
    return fl.render_template("member/join.html", title="회원가입")

@bp.route("/join", methods=["POST"])
def join_result():
    userid = fl.request.form.get("userid")
    userpw = fl.request.form.get("userpassword")

    if userid is "" or userpw is "":
        return "사용자 정보가 필요합니다"

    controller = UserController(db=db_session)

    if controller.add_user(userid, userpw) is False:
        return alert_and_redirect("회원가입 실패 " , fl.url_for("member.join"))

    return alert_and_redirect("로그인 페이지로 이동합니다.", fl.url_for("member.login"))

