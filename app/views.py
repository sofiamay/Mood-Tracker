from flask import render_template, flash, redirect, session, url_for, request
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oauth
from .models import User


facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='872766896169946',
    consumer_secret='47248c3813f7833ad586871d3675bffd',
    request_token_params={'scope': 'public_profile, email'},
)

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')


@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
	    # Include:
    	# User
    	# Current Date
    	# Mood history
    	# Button to log mood
	return render_template('index.html')

@app.route('/login')
def facebook_login():
    next_url = request.args.get('next') or url_for('index')
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=next_url,
        _external=True))

@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        # The user likely denied the request
        flash(u'There was a problem logging in.')
        return redirect(next_url)
    session['oauth_token'] = (resp['access_token'], '')
    user_data = facebook.get('/me/?fields=id,email,first_name,last_name').data
    user = User.query.filter(User.email == user_data['email']).first()
    if user is None:
        new_user = User(email=user_data['email'], first_name=user_data['first_name'], last_name=user_data['last_name'])
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
    else:
        login_user(user)
    return redirect(next_url)