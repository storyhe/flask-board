import flask as fl
from functools import wraps

def redirect(url=None):
    if url is None:
        return ''
    return '<script>location.href=" ' + url + '";</script>';

def alert_and_redirect(alert="", url=None):
    if url is None:
        return ''
    return '<script>alert("' + alert + '");location.href=" ' + url + '";</script>';


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if fl.session['userId'] is None:
            return redirect(fl.url_for('member.login'))
        return f(*args, **kwargs)
    return decorated_function