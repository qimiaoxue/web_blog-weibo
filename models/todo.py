from . import ModelMixin
from . import db
from . import timestamp


class Todo(db.Model, ModelMixin):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String())
    created_time = db.Column(db.Integer)
    update_time = db.Column(db.Integer)

    def __init__(self, form):
        print('chest init', form)
        self.task = form.get('task', '')
        self.created_time = timestamp()

    def update(self, form):
        self.task = form.get('task', '')
        self.save()

    def json(self):
        d = dict(
            id=self.id,
            task=self.task,
            created_time=self.created_time,
        )
        return d

    def valid(self):
        return len(self.task) > 0

    def error_message(self):
        if len(self.task) <= 0:
            return 'task at least need a word'
