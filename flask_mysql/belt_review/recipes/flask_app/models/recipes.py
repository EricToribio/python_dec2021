from flask_app.config.mysqlconnection import connectToMySQL
# import the function that will return an instance of a connection
from flask_app import DB,flash
# model the class after the friend table from our database
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.under_30_min = data['under_30_min']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    def __repr__(self):
        return f"< name: {self.name}, id:{self.id} > "
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of friends
        recipes = []
        # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    @classmethod
    def add_recipe(cls,data):
        query = """INSERT INTO recipes (name,under_30_min,description,instructions,date_made) 
                    VALUE (%(name)s,%(under_30_min)s,%(description)s,%(instructions)s,%(date_made)s );"""

        results = connectToMySQL(DB).query_db(query,data)
        return results
    @classmethod
    def get_one(cls,**data):
        query = """SELECT * FROM recipes 
                    WHERE id = %(id)s;"""
        results = connectToMySQL(DB).query_db(query,data)
        
        return results[0]

    @classmethod
    def update_recipe(cls,data):
        query = """UPDATE recipes SET name=%(name)s,under_30_min=%(under_30_min)s,
        description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s
                    WHERE id = %(id)s;"""

        results = connectToMySQL(DB).query_db(query,data)

    @classmethod
    def destroy(cls,**data):
        query = """DELETE FROM recipes
                    WHERE id = %(id)s"""

        results = connectToMySQL(DB).query_db(query,data)


    @staticmethod
    def recipe_validate(data):
        is_valid = True
        if len(data['name']) < 3 or len(data['instructions']) < 3 or len(data['description']) < 3:
            flash('Name , Instructions , Description all must be at least 3 characters long')
            is_valid= False
        if data['under_30_min'] == "Is Recipe under 30 Minutes" :
            flash('Please choose if recipe is under 30 minutes to make')
            is_valid = False
        if data['date_made'] == "" :
            flash('Enter in the date the recipe was made on')
            is_valid = False
        return is_valid  

            
