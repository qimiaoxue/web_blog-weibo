from models.blogcomment import BlogComment
from models.todo import Todo
from routes import *
import json
from routes.user import current_user
from models.weibo import Weibo


main = Blueprint('api', __name__)


def api_response(success, data=None, message=''):
    r = {
        'success': success,
        'data': data,
        'message': message
    }
    return json.dumps(r, ensure_ascii=False)


@main.route('/todo/add', methods=['POST'])
def add():
    #form = request.form
    form = request.get_json()
    t = Todo(form)
    print('form', form)
    if t.valid():
        t.save()
        return api_response(True, data=t.json())
    else:
        return api_response(False, message=t.error_message())


@main.route('/todo/update/<int:id>', methods=['POST'])
def update(id):
    #form = request.form
    form = request.get_json()
    t = Todo.query.get(id)
    t1 = Todo(form)
    if t1.valid():
        t.update(form)
        return api_response(True, data=t.json())
    else:
        return api_response(False, message=t1.error_message())


@main.route('/todo/delete/<int:id>')
def delete(id):
    t = Todo.query.get(id)
    t.delete()
    return api_response(True, data=t.json())


@main.route('/blog/comment/add', methods=['POST'])
def comment_add():
    #form = request.form
    form = request.get_json()
    c = BlogComment(form)
    u = current_user()
    c.name = u.username
    print('form', form)
    if c.valid():
        c.save()
        return api_response(True, data=c.json())
    else:
        return api_response(False, message=c.error_message())


@main.route('/weibo/add', methods=['POST'])
def weibo_add():
    #form = request.form
    print('weiboadd')
    form = request.get_json()
    print('form', form)
    w = Weibo(form)
    u = current_user()
    w.name = u.username
    print('form', form)
    if w.valid():
        w.save()
        return api_response(True, data=w.json())
    else:
        return api_response(False, message=w.error_message())


@main.route('/weibo/delete/<int:weibo_id>')
def weibo_delete(weibo_id):
    w = Weibo.query.get(weibo_id)
    w.delete()
    return api_response(True, data=w.json())


@main.route('/weibo/comment/add', methods=['POST'])
def weibo_comment_add():
    #form = request.form
    form = request.get_json()
    c = Comment(form)
    u = current_user()
    c.name = u.username
    print('form', form)
    if c.valid():
        c.save()
        return api_response(True, data=c.json())
    else:
        return api_response(False, message=c.error_message())
