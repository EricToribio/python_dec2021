from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# import the function that will return an instance of a connection
DB = "dojo_survey_schema"
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    
    # Now we use class methods to query our database
    
    @classmethod
    def add_dojo(cls,data):

        query = """INSERT INTO dojos (name,location,language,comment) 
                    VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"""

        dojo_id = connectToMySQL(DB).query_db(query,data)
        
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM dojos
                WHERE name = %(name)s;"""
        results = connectToMySQL(DB).query_db(query,data)
        dojo = cls(results[0])
        return dojo

    @staticmethod
    def validate_dojo(data):
        is_valid = True
        if len(data['name']) < 4:
            flash('Name must be at least ')
            is_valid = False
        if data['location'] == 'Choose location':
            flash('Please choose a location')
            is_valid = False
        if data['language'] == 'Choose Favorite Language':
            flash('Please choose a Favorite Language')
            is_valid = False
        return is_valid
    
            
