from flask import Flask, session,flash
from flask_bcrypt import Bcrypt


app = Flask(__name__)
DB = "recipes_schema" # add schema name
bcrypt = Bcrypt(app)
app.secret_key = "supersecrect"