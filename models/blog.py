from . import ModelMixin
from . import db
from . import timestamp
from models.blogcomment import BlogComment


class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    title = db.Column(db.String())
    name = db.Column(db.String())
    created_time = db.Column(db.String(), default=0)

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.name = form.get('name', '')
        self.created_time = timestamp()
        self.comment = ''
        self.comments_num = 0

    def valid(self):
        return len(self.title) > 0 and len(self.content) > 0

    def comments(self):
        cs = BlogComment.query.filter_by(blog_id=self.id).all()
        return cs
