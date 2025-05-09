
from flask import Blueprint,render_template, url_for, flash, redirect,request,abort
from flask_login import login_user,logout_user,current_user,login_required
from flaskblog.posts.forms import PostForm
from flaskblog.models import Post 
from flaskblog import db 


posts = Blueprint('posts',__name__)

@posts.route('/post/new',methods = ['GET','POST'])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        # why current_user and not current_user.id
        post = Post(title = form.title.data,content = form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html',form = form,title="New Post")

@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html',
                           title=post.title,post = post,legend = 'New Post')



@posts.route('/post/<int:post_id>/update',methods = ['GET','POST'])
@login_required
def updatepost(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm() 
    if form.validate_on_submit():
        post.title = form.title.data 
        post.content = form.content.data 
        db.session.commit()
        flash('Your post has been updated!','success')
        return redirect(url_for('posts.post',post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title 
        form.content.data = post.content
    
    return render_template('create_post.html',
                           title="Update post",form=form,legend = 'Update Post')
    

@posts.route('/post/<int:post_id>/delete',methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!','success')
    return redirect(url_for('main.home'))
    