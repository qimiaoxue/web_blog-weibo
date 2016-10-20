from models.blog import Blog
from models.blogcomment import BlogComment
from routes.user import current_user
from routes import *


main = Blueprint('blog', __name__)


@main.route('/')
def index():
    u = current_user()
    if u is None:
        return redirect(url_for('user.login_view'))
    blogs = Blog.query.order_by(Blog.id.desc()).all()
    for i in blogs:
        i.comment = i.comments()
        for j in i.comment:
            j.avatar = j.get_avatar()
        i.comments_num = len(i.comment)
    return render_template('blog_index.html', blogs=blogs)


@main.route('/edit', methods=['POST', 'GET'])
def edit():
    return render_template('blog_add.html')


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    b = Blog(form)
    b.name = 'qimiaoxue'
    if b.valid():
        b.save()
    return redirect(url_for('.index'))


@main.route('/delete/<int:weibo_id>')
def delete(weibo_id):
    w = Blog.query.get(weibo_id)
    w.delete()
    return redirect(url_for('.index'))
