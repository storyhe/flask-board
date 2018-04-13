# -*- coding: utf-8 -*-
import flask as fl
from members.tool import *
from members.models import *
from members.database import db_session
bp = fl.Blueprint('bbs', __name__, url_prefix="/bbs")
from members.controller.UserController import UserController

@bp.route('/<board_id>')
def bbs_list(board_id):
    if board_id is "":
       return redirect("/")
    posts = Board.query.filter(Board.boardId == board_id).all()
    return fl.render_template("pages/list.html", board_id=board_id, posts=posts)

@bp.route('/<board_id>/write', methods=['GET'])
def write(board_id):
    return fl.render_template("pages/write.html", board_id=board_id)

@bp.route('/<board_id>/write', methods=['POST'])
def writeok(board_id):
    title = fl.request.form.get("title")
    content = fl.request.form.get("content")

    if title is "" or content is "":
        return "본문이 필요합니다."

    controller = UserController(db=db_session)
    post = Board()
    post.boardId = board_id

    post.member_idx = controller.get_useridx()
    post.name = controller.get_userid()
    post.title = title
    post.content_body = content

    try:
        db_session.add(post)
        db_session.commit()
    except:
        db_session.rollback()

    return redirect("/bbs/" + board_id)

@bp.route("/<board_id>/<int:post_id>/delete", methods=['GET'])
def delete(board_id, post_id):
    post = Board.query.filter(Board.boardId == board_id, Board.id == post_id).first()

    if post is None:
        return redirect(fl.url_for("bbs.bbs_list", board_id=board_id))

    controller = UserController(db=db_session)
    success = False

    if post.member_idx == controller.get_userid():
        success = True

    if success == False:
        return alert_and_redirect("본인이 쓴글만 지울수 있습니다", url=fl.url_for("bbs.bbs_list", board_id=board_id))

    try:
        db_session.delete(post)
        db_session.commit()
    except:
        db_session.rollback()
        return "에러"

    return redirect(fl.url_for("bbs.bbs_list", board_id=board_id))
