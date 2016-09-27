from models.todo import Todo
from routes import *


main = Blueprint('todo', __name__)


@main.route('/')
def index():
    ts = Todo.query.all()
    return  render_template('todo_index.html', todo_list=ts)
