from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# INIT APP
app = Flask(__name__)

# DATABASE?
app.config.from_object("project.config.Config")

# INIT DB
db = SQLAlchemy(app)

#INIT MARSHMALLOW
ma = Marshmallow(app)


# CLASS/MODEL
class BudgetItem(db.Model):
    __tablename__ = "budget item"

    id = db.Column(db.Integer, primary_key=True)
    item_name= db.Column(db.String(128), unique=True, nullable=False)
    item_cost= db.Column(db.Integer, unique=True, nullable=False)
    total_budget= db.Column(db.Integer, unique=True, nullable=False)
    available_budget= db.Column(db.Integer, unique=True, nullable=False)

    # def __init__(self, email):
    #     self.email = email

