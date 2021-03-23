from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

from application.forms import LoginForm
from application.services import get_users


default = Blueprint('default', __name__)


@default.route('/')
@default.route('/index')
def index_old():
    user = None
    if current_user.is_authenticated:
        user = current_user
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
        'index.html', title='Home', user=user, posts=posts)


@default.route('/')
@default.route('/index2')
def index():
    return render_template(
        'index2.html', title='Index2')


@default.route('/users')
def users():
    response = get_users()
    return render_template(
        'users.html', title='Users', users=response['data'])
