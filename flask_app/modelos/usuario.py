from flask_app.config.mysqlconnection import connectToMySQL

class Usuarios:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def seleccionar(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('usuarioscr').query_db(query)
        usuarios =[]
        for usuario in results:
            usuarios.append( usuario )
        return usuarios
    
    @classmethod
    def guardar(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, updated_at, created_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('usuarioscr').query_db(query, data)
    
    @classmethod
    def seleccionarUno( cls, data ):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('usuarioscr').query_db(query, data)
        #print("Resultados clsMethod seleccionarUno",results)
        resultados = cls(results[0])
        #print("Resultados clsMethod seleccionarUno guardado en cls", resultados)
        return cls(results[0])   
    
    @classmethod
    def eliminar( cls , data ):
        print("aqui el valor de la data", data)
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL('usuarioscr').query_db(query, data)
        print("aqui el contenido de results", results)
        return results
    

    @classmethod
    def update( cls , data ):
        print(data)
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL('usuarioscr').query_db(query, data)
        #print("respuesta de results", results)
        return results