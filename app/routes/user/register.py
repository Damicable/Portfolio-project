from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check password validation
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('user/page-register.html')

        # Check password length
        if len(password) < 6:
            flash('Password must be at least six characters long.',  'danger')
            return render_template('user/page-register.html')

        # Hash password
        password_hash = generate_password_hash(password)

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please use a different email.',  'danger')
            return render_template('user/page-register.html')

        # Create a new user
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the dashboard after successful registration
        flash('Registration Successful. Welcome to your dashboard',  'success')
        return redirect(url_for('dashboard'))

    return render_template('user/page-register.html')
