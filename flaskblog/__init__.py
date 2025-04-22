from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

# create the database connection
db = SQLAlchemy()
# register Bcrypt with the app
bcrypt = Bcrypt()
# register LoginManager with the app 
login_manager = LoginManager()

# the page where a user goes in case of unauthorized access
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# config for emails
mail = Mail()


def create_app(Config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config_class)

    # initialize all the extensions
    db.__init__(app)
    bcrypt.__init__(app)
    login_manager.__init__(app)
    mail.__init__(app)

   
    # register all the blueprints
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts 
    from flaskblog.main.routes import main 
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app 