from flask import (
    abort, request, Blueprint, render_template, flash, redirect, url_for,
    session)
from flask_login import login_user

from application.forms import LoginForm, RegisterForm
from application.services import login_service, register_service
from application.utils import User, TokenDecode


auth= Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        response = login_service(
            params={
                'email': form.email.data,
                'password': form.password.data}
        )
        if response.status_code == 200:
            auth_token = response.json()['token']
            print('Token: ', auth_token)
            payload = TokenDecode.decode_auth_token(auth_token)
            print('Payload: ', payload)
            session['identity'] = dict()
            session['identity'].update(payload)
            user = User(email=payload['identity'])
            login_user(user)
            flash('Login requested for user {}, remember_me={}'.format(
                form.email.data, form.remember_me.data))
            return redirect(url_for('default.index'))
        else:
            flash(response.json()['message'])
    return render_template('login.html', title='Sign In', form=form)


@auth.route('/logout', methods=['POST'])
def logout():
    flash('Logout')
    return redirect(url_for('default.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        result = register_service(
            params={
                'username': form.username.data,
                'email': form.email.data,
                'password': form.password.data}
        )
        flash('Register requested for user {}'.format(form.email.data))
        return redirect(url_for('default.index'))
    return render_template('register.html', title='Sign Up', form=form)