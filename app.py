from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

#App DB Configurations
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///flask.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Initializing SQLAlchemy
db = SQLAlchemy(app)

#Initialize Flask Migrate
migrate = Migrate(app, db)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    review = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    
    
@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)