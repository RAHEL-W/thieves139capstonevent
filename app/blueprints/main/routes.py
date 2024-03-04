from flask import render_template, redirect, url_for, flash
from . import main
from app.models import User,db
from flask_login import login_required, current_user

@main.route('/')
def home():
   return render_template('home.html')

@main.route('/connect')
@login_required
def connect():
   users = User.query.filter(User.id != current_user.id)
   return render_template('connect.html', users=users)


@main.route('/follow/<user_id>')
@login_required
def follow(user_id):
   user = User.query.get(user_id)
   current_user.following.append(user)
   db.session.commit()
   flash(f'successfully followed {user.username}', 'info')
   return redirect(url_for('main.connect'))



@main.route('/unfollow/<user_id>')
@login_required
def unfollow(user_id):
   user = User.query.get(user_id)
   current_user.following.remove(user)
   db.session.commit()
   flash(f'successfully unfollowed {user.username}', 'warning')
   return redirect(url_for('main.connect'))
