from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Temporary database configuration, should be moved to a separate file or read from environment variables
user = "admin_user"
password = "admin_pass"
ip = "localhost"
db_name = "ioproject"

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{ip}/{db_name}'
db = SQLAlchemy(app)


from api.routes import hello  # noqa
from api.routes import note  # noqa
