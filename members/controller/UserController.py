import flask as fl
from werkzeug.security import generate_password_hash, check_password_hash
from members.models import *


class UserController(object):
    def __init__(self, db=None):
        self.db = db

    def add_user(self, user_id, user_pw):
        if user_id is None or user_pw is None:
            return False
        if user_id is "" or user_pw is "":
            return False

        user = User()
        user.userid = user_id
        user.password = self.set_password(user_pw)

        try:
            self.db.add(user)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()

        return False

    def check_user(self, userid, userpassword):
        login = User.query.filter(User.userid == userid).first()

        if login is None:
            return False

        if userid == login.userid and self.check_password(login.password, userpassword) is True:
            fl.session['userinfo'] = {"userid": login.userid, "nickname": login.nickname, "useridx": login.idx}
            return True

        return False

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    def get_username(self):
        if 'userinfo' in fl.session:
            return fl.session['userinfo']['nickname']
        return None

    def get_userid(self):
        if 'userinfo' in fl.session:
            return fl.session['userinfo']['userid']
        return None

    def get_useridx(self):
        if 'userinfo' in fl.session:
            return fl.session['userinfo']['useridx']
        return None
