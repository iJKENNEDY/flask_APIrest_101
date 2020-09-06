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

	def post(self):	
	   	conn= db_connect.connect()
	   	first_name = request.json['FirstName']
	   	last_name = request.json['LastName']
	   	company = request.json['Company']
	   	address = request.json['Address']
	   	city = request.json['City']
	   	state = request.json['State']
	   	country = request.json['Country']
	   	postal_code = request.json['PostalCode']
	   	phone = request.json['Phone']
	   	fax = request.json['Fax']
	   	email = request.json['Email']
	   	support_id = request.json['SupportRepId']
	   	query = conn.execute("insert into customers values(null, '{0}','{1}','{2}','{3}','{4}',\
	   							'{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}' )".format(first_name,
	   								last_name, company, address, city, state, country, postal_code, phone,fax,email, support_id))
	   	return  {'status': 'nuevo cliente añadido'}

class CustomerData(Resource):
	def get(self, customerId):
		conn = db_connect.connect()
		query = conn.execute("select * from  customers where CustomerId=%d" % int(customerId))
		result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
		return jsonify(result)


class UpdateCustomer(Resource):
	def put(self, customerId):
		first_name = request.json['FirstName']
		conn = db_connect.connect()
		query = conn.execute("update customers set FirstName='%s' where CustomerId=%s"% (first_name, int(customerId)))
		return {'status':'Cliente borrado con exito'}


class DeleteCustomer(Resource):
	def delete(self, customer_id):
		conn = db_connect.connect()
		query = conn.execute("delete from customers where CustomerId=%d" % int(customer_id))
		return {'status': 'cliente borrado'}


api.add_resource(Customers, '/customers')
api.add_resource(CustomerData, '/customers/<customerId>')
api.add_resource(UpdateCustomer, '/customers/<customerId>')
api.add_resource(DeleteCustomer, '/delete/<customer_id>')

if __name__ == '__main__':
	app.run(port='5000')
