from flask import redirect,render_template,url_for, request, flash 
from . import post
from .forms import CreateEventPost, CreatePost
from flask_login import login_required, current_user
from app.models import EventPost, db, Post


@post.route('/create_event_post', methods=['GET', 'POST'])
@login_required
def create_event_post():
    form = CreateEventPost()

    if request.method == 'POST' and form.validate_on_submit:
        img_url = form.img_url.data
        caption = form.caption.data
        location = form.location.data
        user_id = current_user.id
        
        new_event_post = EventPost(img_url=img_url, caption=caption, location=location, user_id=user_id)
        new_event_post.save()
        flash('Successfully posted event', 'success')
        return redirect(url_for('main.home'))

    else:
        return render_template('create_event_post.html', form=form)
    


@post.route('/event')   
def event():
    events = EventPost.query.all()
    return render_template('event.html', events=events)


# @post.route('/edit_event_post/<post_id>', methods=['GET','POST'])
# def edit_event_post(post_id):
#     eventpost = EventPost.query.get(post_id) 
#     form= CreateEventPost
#     if request.method == 'POST' and form.validate_on_submit:
#         return redirect(url_for('post.create_event_post'))
#     else:
#      return render_template('edit_event_post.html', form=form, eventpost=eventpost)


@post.route('/edit_event_post/<post_id>', methods=['GET', 'POST'])
@login_required
def edit_event_post(post_id):
    eventpost = EventPost.query.get(post_id) 
    form = CreateEventPost(obj=eventpost)  # Instantiate the form with eventpost data
    if eventpost and eventpost.user_id == current_user.id:
        if request.method == 'POST' and form.validate_on_submit():
            eventpost.img_url = form.img_url.data
            eventpost.caption = form.caption.data
            eventpost.location = form.location.data

            eventpost.save()
            flash('successfully updataed post', 'info')
            return redirect(url_for('post.event'))  
        else:

         return render_template('edit_event_post.html', form=form, eventpost=eventpost)
        
    else:
        flash('this post it doesn\'t belong to you','danger')
        return redirect(url_for('post.event'))    
    




@post.route('/delete_event_post/<post_id>')  
@login_required
def delete_event_post(post_id):
    eventpost = EventPost.query.get(post_id) 
    if eventpost and eventpost.user_id == current_user.id:
        db.session.delete(eventpost)
        db.session.commit()
        flash('event post is succefully deleted', 'danger')
        return redirect(url_for('post.event'))
    else:
        flash('this post it doesn\'t belong to you','danger')
        return redirect(url_for('post.event')) 
    








@post.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = CreatePost()

    if request.method == 'POST' and form.validate_on_submit:
        img_url = form.img_url.data
        caption = form.caption.data
        location = form.location.data
        user_id = current_user.id
        
        new_post = Post(img_url=img_url, caption=caption, location=location, user_id=user_id)
        new_post.save()
        flash('Successfully created new post ', 'success')
        return redirect(url_for('main.home'))

    else:
        return render_template('create_post.html', form=form)
    



@post.route('/feed')   
def feed():
    posts = Post.query.all()
    return render_template('feed.html', posts=posts)






@post.route('/edit_post/<post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get(post_id) 
    form = CreatePost(obj=post)  # Instantiate the form with eventpost data
    if post and post.user_id == current_user.id:
        if request.method == 'POST' and form.validate_on_submit():
            post.img_url = form.img_url.data
            post.caption = form.caption.data
            post.location = form.location.data

            post.save()
            flash('successfully updataed post', 'info')
            return redirect(url_for('post.feed'))  
        else:

         return render_template('edit_post.html', form=form, post=post)
        
    else:
        flash('this post it doesn\'t belong to you','danger')
        return redirect(url_for('post.feed'))    
    




@post.route('/delete_post/<post_id>')  
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id) 
    if post and post.user_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
        flash(' post is succefully deleted', 'danger')
        return redirect(url_for('post.feed'))
    else:
        flash('this post it doesn\'t belong to you','danger')
        return redirect(url_for('post.feed')) 
    
