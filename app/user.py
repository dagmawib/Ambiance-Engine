from flask import render_template, url_for, redirect, Blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from . import bcrypt, db,login_manager
from .forms import LoginForm, RegistrationForm
from .models import User

user_bp = Blueprint('user', __name__)

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

@user_bp.route('/signup', methods=['GET', 'POST'])
def signUp():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username = form.username.data, password=hashed_password, Fname=form.Fname.data, country=form.country.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user.login'))
    return render_template('signUp.html', form=form)
