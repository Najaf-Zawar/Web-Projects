from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from  flask_mail import Mail
from flaskApp.config import config



#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Added from Stackoverflow not needed till
db = SQLAlchemy()
# app.app_context().push()   # Added from Stackoverflow Write this in cmd by importing app and db 
bcrypt = Bcrypt()
login_manager= LoginManager()
login_manager.login_view = 'users.Login'
login_manager.login_message_category = 'info'


mail = Mail()




def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    from flaskApp.users.routes import users
    from flaskApp.posts.routes import posts
    from flaskApp.main.routes import main
    from flaskApp.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    return app
