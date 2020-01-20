from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:hasan@localhost/schoolmanagementsystemdb"

db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)
