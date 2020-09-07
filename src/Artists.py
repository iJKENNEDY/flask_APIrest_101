
from flask import Flask, request, jsonify
from flask_restful import  Resource, Api
from sqlalchemy import create_engine

db_connect = create_engine('sqlite: ///chinok.db')
app = Flask(__name__)
api = Api(app)


class Artists(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from artists")
        return {'artists':[i[0] for i in query.cursor.fetchall()]}

    def post(self):
        conn = db_connect.connect()
        nameArtist = request.json['Name']
        query =conn.execute("insert into artists values(null,'{0}')".format(nameArtist))
        return {'status': 'nuevo artista'}

class ArtistsData(Resource):
    def get(self, artistId):
        conn = db_connect.connect()
        query = conn.execute("select * from artists where ArtistId=%d" % (int(artistId)))
        result = {'data':[dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
        return jsonify(result)


class UpdateArtist(Resource):
    def put(self,artistId):
        name = request.json['Name']
        conn = db_connect.connect()
        query = conn.execute("update artists set Name='%s' where ArtistId=%s" % (name, int(artistId)))
        return {'status':'se actualizo al artista'}

class DeleteArtist(Resource):
    def delete(self, artistId):
        conn = db_connect.connect()
        query = conn.execute("delete from artists where ArtistId=%d"% int(artistId))
        return {'status':'artista borrado'}


api.add_resource(Artists, '/artist')
api.add_resource(ArtistsData,'/artist/<artistId>')
api.add_resource(UpdateArtist, '/artist/<artistId>')
api.add_resource(DeleteArtist, '/artist/<artistId>')

if __name__ == '__main__':
    app.run(port='5000')