from flask_app.config.mysqlconnection import connectToMySQL
# import the function that will return an instance of a connection
DB = "dojos_and_ninjas_schema"
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dojo_id = data['dojo_id']
        self.name = data['name']
        



    def __repr__(self):
        return f"< first name: {self.first_name}, id:{self.id}, name: {self.name} > "
    # Now we use class methods to query our database
    
    @classmethod
    def add_ninja(cls,data):
        query = """INSERT INTO ninjas (first_name,last_name,dojo_id) 
                    VALUE (%(first_name)s,%(last_name)s,%(dojo_id)s );"""

        results = connectToMySQL(DB).query_db(query,data)
        return results
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM ninjas 
                    WHERE id = %(id)s;"""
        results = connectToMySQL(DB).query_db(query,data)
        
        return results[0]

    @classmethod
    def edit(cls,data):
        query = """UPDATE ninjas SET first_name= %(first_name)s,last_name= %(last_name)s,dojo_id=%(dojo_id)s
                    WHERE id = %(id)s;"""

        results = connectToMySQL(DB).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = """DELETE FROM ninjas
                    WHERE id = %(id)s"""

        results = connectToMySQL(DB).query_db(query,data)

            
