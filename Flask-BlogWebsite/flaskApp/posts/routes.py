from flask import Blueprint, render_template, redirect, url_for, request, abort, flash
from flask_login import current_user, login_required
from flaskApp.models import Post
from flaskApp.posts.forms import PostForm

from flaskApp import db



posts = Blueprint('posts', __name__)

    
@posts.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your Post has been Created", 'success') 
        return redirect(url_for('main.Home')) 
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')
        
@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
    
    
@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit() # No need to Add b/c already in Database
        flash('Your post has been Updated Sucessfully', 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    elif request.method== 'GET':    
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')




@posts.route('/post/<int:post_id>/delete', methods=['GET','POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)    
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been Deleted Sucessfully', 'success')
    return redirect(url_for('main.Home'))

