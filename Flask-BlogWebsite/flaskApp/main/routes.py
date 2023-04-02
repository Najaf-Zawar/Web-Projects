from flask import render_template, request, Blueprint
from flaskApp.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def Home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts = posts, title = 'Home')

@main.route("/about")
def About():
    return render_template('about.html', title = 'About')

