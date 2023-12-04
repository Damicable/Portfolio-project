from app import app
from flask import render_template



@app.route('/login')
def login_page():
    return render_template('user/page-login.html')