from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    group = db.Column(db.String(50), unique=True, nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Group(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False)
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("Database and tables created successfully!")
