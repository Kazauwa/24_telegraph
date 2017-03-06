import os

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('CSRF_TOKEN')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_LOCATION = os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI = os.path.join('sqlite:////', DATABASE_LOCATION.lstrip('/'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
