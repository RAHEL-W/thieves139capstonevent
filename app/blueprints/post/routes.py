from flask import redirect,render_template,url_for, request, flash 
from . import post
from .forms import CreateEventPost
from flask_login import login_required, current_user
from app.models import EventPost


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


