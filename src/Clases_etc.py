from flask  import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class genres(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select GenreId, Name from genres ")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)



class invoices(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select InvoiceId, CustomerId, InvoiceDate, BillingAddress, BillingCity,BillingState,BillingCountry,BillingPostalCode,Total  from invoices;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class invoice_items(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity from invoice_items;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class media_types(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select MediaTypeId, Name from media_types;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class playlist(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select PlaylistId, Name from playlists;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)



class playlist_track(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select PlaylistId, TrackId from playlist_track;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(genres, '/genres')
api.add_resource(invoices, '/invoices')
api.add_resource(invoice_items, '/invoice_items')
api.add_resource(media_types, '/media_types')
api.add_resource(playlist, '/playlist')
api.add_resource(playlist_track, '/list_track')

if __name__ == "__main__":
    app.run(port='5000')