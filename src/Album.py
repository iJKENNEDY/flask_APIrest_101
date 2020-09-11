from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Album(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from albums")
        return {'albums': [i[0] for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        title = request.json['Title']
        artistId = request.json['ArtistId']

        query = conn.execute("insert into albums values (null, '{0}','{1}')".format(title, artistId))
        return {'status': 'Nuevo album'}


class AlbumAll(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Title, ArtistId from albums;")
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class AlbumData(Resource):
    def get(self, albumId):
        conn = db_connect.connect()
        query = conn.execute("select * from albums where AlbumId=%d" %int(albumId))
        result = {'data': [dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
        return  jsonify(result)

class UpdateAlbum(Resource):
    def put(self, album_id):
        title = request.json['Title']
        conn = db_connect.connect()
        query = conn.execute("update albums set Title='%s' where AlbumId =%s" % (title,album_id))
        return {'status': 'cambio del titulo'}

class DeleteAlbum(Resource):
    def delete(self, albumId):
        conn = db_connect.connect()
        query = conn.execute("delete from albums where AlbumId=%d " % int(albumId))
        return {'status':'album borrado'}

api.add_resource(Album, '/albums')
api.add_resource(AlbumData, '/albums/<albumId>')
api.add_resource(UpdateAlbum, '/albums/<albumId>')
api.add_resource(DeleteAlbum, '/albums/<albumId>')

if __name__ == '__main__':
    app.run(port='5000')




