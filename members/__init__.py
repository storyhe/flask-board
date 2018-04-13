import flask

app = flask.Flask(__name__)

from members.views import main, bbs, member

app.register_blueprint(main.bp)
app.register_blueprint(bbs.bp)
app.register_blueprint(member.bp)

# 범용 page 404
@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('pages/404.html')