from . import ModelMixin
from . import timestamp
from . import db


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    avatar = db.Column(db.String())
    created_time = db.Column(db.Integer)

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.avatar = form.get('avatar',
                               'http://vip.cocode.cc/uploads/avatar/default.png')
        self.created_time = timestamp()

    def valid(self):
        user = User.query.filter_by(username=self.username).first()
        if user is not None:
            return False
        return len(self.username) > 2 and len(self.password) > 2

    def validate_login(self, u):
        return (u is not None and u.username == self.username and u.password == self.password)

    def change_passwod(self, password):
        if len(password) > 2:
            self.password = password
            self.save()
            return True
        else:
            return False

    def change_avatar(self, avatar):
        if len(avatar) > 2:
            self.avatar = avatar
            self.save()
            return True
        else:
            return False
