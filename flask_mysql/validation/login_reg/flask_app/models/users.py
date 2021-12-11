from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt, DB, session
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @property
    def full_name(self):
        
        return f'{self.first_name} {self.last_name}'
    def __repr__(self):
        return f"< first name: {self.first_name}, id:{self.id} > "
    # Now we use class methods to query our database
    
    
    @classmethod
    def add_user(cls,data):
        query = """INSERT INTO users (first_name,last_name,email,password) 
                    VALUE (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        
        user_data = {
            **data,
            'password':bcrypt.generate_password_hash(data['password'])
        }
        print(user_data)
        results = connectToMySQL(DB).query_db(query,user_data)
        return results
    @classmethod
    def get_one(cls,**data):
        query = """SELECT * FROM users 
                    WHERE email = %(email)s;"""
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            return cls(results[0])

    @staticmethod
    def validate_new_user(data):
        is_valid = True
        user = User.get_one(email=data['email'])
        if  user:
            flash('Please sign in email already has account')
            is_valid = False
            return is_valid
        if len(data['first_name']) < 2:
            flash('Please Enter valid First Name')
            is_valid = False
        if len(data['last_name']) < 3:
            flash('Please Enter valid Last Name')
            is_valid = False
        if len(data['password']) < 6:
            flash('Password must be at least 6 characters long')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Passwords do Not match')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Please enter valid Email')
            is_valid = False
        return is_valid

    
        


    



   

            
