from flask import Flask
from flask_script import Manager
from members import app

from members.database import init_db, drop_db

db_manager = Manager()
manager = Manager(app)
manager.add_command('db', db_manager)

@db_manager.command
def init():
    init_db()

@db_manager.command
def reset():
    drop_db()


if __name__ == '__main__':
    app.debug = True
    app.secret_key = "12491252515fasqtas"
    manager.run()
