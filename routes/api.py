from models.todo import Todo
from routes import *
import json


main = Blueprint('api', __name__)


@main.route('/todo/add', methods=['POST'])
def add():
    form = request.form
    t = Todo(form)
    print('form', form)
    r = {
        'data': []
    }
    if t.valid():
        t.save()
        r['success'] = True
        r['data'] = t.json()
    else:
        r['success'] = False
        message = t.error_message()
        r['message'] = message
    return json.dumps(r, ensure_ascii=False)


@main.route('/todo/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    t = Todo.query.get(id)
    t1 = Todo(form)
    r = {
        'data': []
    }
    if t1.valid():
        t.update(form)
        r = {
            'success': True,
            'data': t.json(),
        }
    else:
        r = {
            'success': False,
            'message': t1.error_message()
        }
    return json.dumps(r, ensure_ascii=False)


@main.route('/todo/delete/<int:id>')
def delete(id):
    t = Todo.query.get(id)
    t.delete()
    r = {
        'success': True,
        'data': t.json(),
    }
    return json.dumps(r, ensure_ascii=False)
