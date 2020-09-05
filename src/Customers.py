from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///chinook.db') #La ruta depende de donde tengas almacenada la base de datos
app = Flask(__name__)
api = Api(app)

class Customers(Resource):
	def get(self):
		conn = db_connect.connect() # Conexión a la Base de Datos
        query = conn.execute("select * from customers")  # Esta línea ejecuta un query y retorna un json como resultado
        return {'customers': [i[0] for i in query.cursor.fetchall()]}  # Se obtiene la primera columna que es EmployeeId

