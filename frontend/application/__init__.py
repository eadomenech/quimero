from datetime import datetime

from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler

from application.utils import User


toolbar = DebugToolbarExtension()
login_manager = LoginManager()

def not_found_error(error):
    return render_template('404.html'), 404

def create_app(config):
    """Application setup"""
    app = Flask(__name__, instance_relative_config=False)
    
    # load the config
    app.config.from_object(config)

    # set up extensions
    toolbar.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # load some plugins, modules or blueprints
        from application.views.default import default
        from application.views.auth import auth

        # registrar los blueprints
        app.register_blueprint(default)
        app.register_blueprint(auth)

        login_manager.login_view = 'auth.login'

        app.register_error_handler(404, not_found_error)

        if not app.debug:
            if app.config['MAIL_SERVER']:
                auth = None
                if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                    auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
                secure = None
                if app.config['MAIL_USE_TLS']:
                    secure = ()
                mail_handler = SMTPHandler(
                    mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                    fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                    toaddrs=app.config['ADMINS'], subject='Quimero Frontend Failure',
                    credentials=auth, secure=secure)
                mail_handler.setLevel(logging.ERROR)
                app.logger.addHandler(mail_handler)
        
        @login_manager.user_loader
        def load_user(user_email):
            if 'identity' not in session:
                return None
            # check expiration
            idt = session['identity']
            expires = datetime.utcfromtimestamp(idt['exp'])
            app.logger.debug("Expires on {}".format(expires))
            app.logger.debug("now is {}".format(datetime.utcnow()))
            expires_seconds = (expires - datetime.utcnow()).total_seconds()
            if expires_seconds < 0:
                return None

            user = User(
                email=user_email, username=idt['user_claims']['username'])

            return user


    return app
