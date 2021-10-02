
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)





################################################
#Database Setup
################################################
url = 'postgresql://postgres:Nanakweku321.@localhost:5432/project3'



################################################
#Flask Setup
################################################
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class cost_of_living(db.Model):
    ID = db.Column(db.Integer)
    City = db.Column(db.String, primary_key=True)
    State = db.Column(db.String)
    Cost_of_Living_Index = db.Column(db.Float)
    Local_Purchasing_Power= db.Column(db.Float)
    Groceries_Index = db.Column(db.Float)
    Rent_Index = db.Column(db.Float)
    Restaurant_Price_Index = db.Column(db.Float)

db.create_all()


#create route that renders index.html template

#Query the database and send the jsonified results
@app.route('/')
def city():
    cities = cost_of_living.query.all()
    return render_template("index.html", cities=cities)

if __name__ == "__main__":
    app.run()



