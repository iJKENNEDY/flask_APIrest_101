from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from models import User 
from models import db

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False) 
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())




def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

#CREATE DATABASE users;
#
@app.route('/api/v1/users/', methods=['POST'])

def create_user():
    json = request.get_json(force=True)

    if json.get('username') is None:
        return jsonify({'message':'Bad request'}), 400

    user = User.create(json['username'])
    return jsonify({'user':user.json()})


@classmethod
def create(cls, username):
    user = User(username=usernme)
    return user.save()

def save(self):
    try:
        db.session.add(self)
        db.session.commit()
        return self
    except:
        return False 

#serializar el objeto::: 
def json(self):
    return{
        'id': self.id,
        'username': self.username
        'created_at': self.created_at
    }


#obtenemos a los usuarios::: 
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = [user.json() for user in User.query.all()]
    return jsonify({'users':users})

@app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'User does not exxists'})

    return jsonify({'user':user.json()})

    json = request.get_json(force=True)
    if json.get('username') is None:
        return jsonify({'message': 'Bad request'}), 400

    user.username = json['username']
    user.update()

    return jsonify({'user': user.json()})

    user.update()
    return jsonify({'user': user.json()})


def update(self):
    self.save() 

@app.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'User does not exists'}), 404
    user.delete()
    return jsonify({'user': user.json() })

def delete(self):
    try:
        db.session.delete(self)
        db.session.commit()
        return True
    except:
        return False


def decorator_name(function):
    def wrap(*args, **kwargs):
        return function(*args, **kwargs)

    wrap.__name__ = function.__name__
    return wrap