from flask import render_template, url_for, flash, redirect, request
from app.models import User, Election, Candidate, Vote
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from . import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", title="home")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f"Login Unsuccessful", "danger")
            flash(f"Check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account have been updated!')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    #image_file = url_for('static', filename='images/'+ current_user.image_file)
    return render_template('account.html', title='Account', form=form)#this should be in this bracket(, image_file=image_file)



# @app.route("/about", methods=["GET", "POST"])
# def about():
#     return render_template("about.html")

# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     return render_template("contact.html")


@app.route("/create_election", methods=["GET", "POST"])
def create_election():
    return render_template("create_election.html")

