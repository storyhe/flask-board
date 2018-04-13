import flask as fl
from werkzeug.security import generate_password_hash, check_password_hash
from members.models import *


class BoardController(object):
    def __init__(self, db=None):
        self.db = db

    def check_board(self, board_name):
        if Board_list.query.filter(Board_list.name == board_name).first() is not None:
            return True
        return False

