from models.user import User
from models.weibo import Weibo

from routes import *
from routes.user import current_user


main = Blueprint('weibo', __name__)


@main.route('/weibo')
def index():
    u = current_user()
    if u is None:
        abort(404)
    weibo_list = Weibo.query.order_by(Weibo.id.desc()).all()
    for w in weibo_list:
        w.comment = w.comments()
        for i in w.comment:
            i.avatar = i.get_avatar()
        w.comments_num = len(w.comment)
        w.avatar = w.get_avatar()
    return render_template('weibo_index.html', weibos=weibo_list)
