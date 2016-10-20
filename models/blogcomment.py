from . import ModelMixin
from . import timestamp
from . import db
from models.user import User


class BlogComment(db.Model, ModelMixin):
    __tablename__ = 'blog_comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String())
    name = db.Column(db.String())
    created_time = db.Column(db.String())
    blog_id = db.Column(db.Integer)

    def __init__(self, form):
        self.comment = form.get('comment', '')
        self.name = form.get('name', '')
        self.blog_id = form.get('blog_id', '')
        self.created_time = timestamp()

    def valid(self):
        return len(self.comment) > 0 and len(self.name) > 0

    def get_avatar(self):
        a = User.query.filter_by(username=self.name).first()
        if a is None:
            return 'http://vip.cocode.cc/uploads/avatar/default.png'
        return a.avatar

    def json(self):
        d = {
            'id': self.id,
            'comment': self.comment,
            'created_time': self.created_time,
            'blog_id': self.blog_id,
            'name': self.name,
            'avatar': self.get_avatar(),
        }
        return d


def main():
    BlogComment()

if __name__ == '__main__':
    main()
