from flask import Flask ,session
from flask_bcrypt import Bcrypt


app = Flask(__name__)
DB = "user_login_schema"
bcrypt = Bcrypt(app)
app.secret_key = "supersecrect"