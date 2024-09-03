from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders the login page and handles user authentication.

    If the request method is POST, it retrieves the email and password from the form data,
    checks if the user exists, and validates the password. If successful, the user is logged in 
    and redirected to the home page. If the email or password is incorrect, an error message 
    is flashed.

    Returns:
        A rendered template of the login page with the current user's data if GET request,
        or redirects to the home page if login is successful.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, try again.", category='error')
        else:
            flash("Email does not exist.", category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    """
    Logs out the current user and redirects to the login page.

    This route requires the user to be logged in. After logging out, 
    the user is redirected to the login page.
    
    Returns:
        A redirect to the login page.
    """
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Renders the sign-up page and handles user registration.

    If the request method is POST, it retrieves the user's email, first name, 
    and passwords from the form data. It then validates the input (e.g., email uniqueness, 
    password length) and creates a new user in the database if the input is valid. The user 
    is automatically logged in after a successful sign-up and redirected to the home page. 
    If validation fails, appropriate error messages are flashed.

    Returns:
        A rendered template of the sign-up page with the current user's data if GET request,
        or redirects to the home page if sign-up is successful.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')
            new_user = User(email=email, first_name=first_name, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category="success")
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
