from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db

from models.todo import Todo
from models.user import User
from models.blog import Blog
from models.blogcomment import BlogComment
from models.weibo import Weibo
from models.comment import Comment

from routes.todo import main as routes_todo
from routes.api import main as routes_api
from routes.user import main as routes_user
from routes.blog import main as routes_blog
from routes.weibo import main as routes_weibo

app = Flask(__name__)
db_path = 'todo.sqlite'
manager = Manager(app)


def register_routes(app):
    app.register_blueprint(routes_todo, url_prefix='/todo')
    app.register_blueprint(routes_user)
    app.register_blueprint(routes_api, url_prefix='/api')
    app.register_blueprint(routes_blog, url_prefix='/blog')
    app.register_blueprint(routes_weibo)


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


@manager.command
def server():
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
