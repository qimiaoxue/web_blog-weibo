from . import ModelMixin
from . import db
from . import timestamp
from models.user import User
from models.comment import Comment


class Weibo(db.Model, ModelMixin):
    __tablename__ = 'weibos'
    id = db.Column(db.Integer, primary_key=True)
    weibo = db.Column(db.String())
    name = db.Column(db.String())
    created_time = db.Column(db.String(), default=0)

    def __init__(self, form):
        print('chest init', form)
        self.weibo = form.get('weibo', '')
        self.created_time = timestamp()
        self.name = form.get('name', '')
        self.comment = ''
        self.comments_num = 0

    def valid(self):
        return len(self.weibo) > 2 and len(self.name) > 0

    def get_avatar(self):
        a = User.query.filter_by(username=self.name).first()
        if a is None:
            return 'http://vip.cocode.cc/uploads/avatar/default.png'
        return a.avatar

    def comments(self):
        cs = Comment.query.filter_by(weibo_id=self.id).all()
        return cs

    def json(self):
        d = dict(
            id=self.id,
            weibo=self.weibo,
            name=self.name,
            comments_num=len(self.comments()),
            avatar=self.get_avatar(),
            created_time=self.created_time,
        )
        return d

    def error_message(self):
        if len(self.weibo) <= 2:
            return 'weibo need three words at least'
