from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Basic config files and creating a flask instance
app = Flask(__name__)
app.config.from_object(Config)


# Load environment variables from .env file
load_dotenv()


# Load secret key from environment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)



from app.routes.user import *

if __name__ == '__main__':
    app.run()


