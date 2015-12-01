from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
	    # Include:
    	# User
    	# Current Date
    	# Mood history
    	# Button to log mood
	return render_template('home.html')