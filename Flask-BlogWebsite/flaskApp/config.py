import os

class config:
    SECRET_KEY = '4822add8094fe14cc2fd7f52a99b7a99'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_USERNAME = os.environ.get('EMAIL_PASS')

    # MAIL_SERVER='smtp.gmail.com'  
    # MAIL_PORT= 465  
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_USERNAME = os.environ.get('EMAIL_PASS')  
    # MAIL_USE_TLS = False  
    # MAIL_USE_SSL = True  

