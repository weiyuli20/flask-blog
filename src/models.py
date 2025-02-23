from src import db
from datetime import datetime

#Flask-SQLAlchemy自动设置类名为小写来作为对应表的名称
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),index=True,unique=True )
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',backref='author',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = dn=db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow) #使用UTC时间
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)