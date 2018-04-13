# -*- coding: utf-8 -*-
import flask as fl

bp = fl.Blueprint('main', __name__)


@bp.route('/')
def root():
    return fl.render_template("index.html")
