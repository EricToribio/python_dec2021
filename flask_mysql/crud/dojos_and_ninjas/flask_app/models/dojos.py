
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas
DB = "dojos_and_ninjas_schema"

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    def __repr__(self):
        return f"< name: {self.name}, id:{self.id} > "
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        
        results = connectToMySQL(DB).query_db(query)

        all_dojos = []
        
        for dojo in results:
            all_dojos.append( cls(dojo) )
        return all_dojos
    @classmethod
    def add_dojo(cls,data):
        query = """INSERT INTO dojos (name) 
                    VALUE (%(name)s);"""

        results = connectToMySQL(DB).query_db(query,data)
        
    @classmethod
    def get_one(cls,data):
        query = """SELECT * FROM dojos 
                    LEFT JOIN ninjas On dojo_id=dojos.id
                    WHERE dojos.id = %(id)s;"""
        results = connectToMySQL(DB).query_db(query,data)
        dojo = cls(results[0])
        dojo.ninjas = []
        for row in results:
            ninja_data={
                **row,
                "id":row['ninjas.id'],
                "created_at":row['ninjas.created_at'],
                "updated_at":row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninjas.Ninja(ninja_data))
        
        return dojo

    @classmethod
    def edit(cls,data):
        query = """UPDATE users SET name= %(name)s, updated_at=NOW()
                    WHERE id = %(id)s;"""

        results = connectToMySQL(DB).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = """DELETE FROM dojos
                    WHERE id = %(id)s"""

        results = connectToMySQL(DB).query_db(query,data)

            
