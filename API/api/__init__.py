import sys
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
api = Api(app)

# Temporary database configuration, should be moved to a separate file
# or read from environment variables
user = "admin_user"
password = "mypassword"
ip = "db"
db_name = "ioproject"

# Switch to the test database if pytest is running.

if "pytest" in sys.modules:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@localhost/{db_name}_test'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{ip}/{db_name}'


# JWT configuration
ACCESS_EXPIRES = timedelta(hours=1)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES

# This is needed to allow custom JWT error responses to be returned.
app.config["PROPAGATE_EXCEPTIONS"] = True

jwt = JWTManager(app)

# Load the callback functions that handle custom JWT error responses.
from api.utilities import auth_loaders  # noqa

db = SQLAlchemy(app)

from api.routes import hello  # noqa
from api.routes import note  # noqa
from api.routes import auth  # noqa
