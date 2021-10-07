from flask.helpers import total_seconds
import pandas as pd 
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import json
import plotly
import plotly.express as px



# data = data.to_json()
# json_ = []
# for i in data.index:
#     row_=data.loc[i].to_json()
#     json_.append(row_)



################################################
#Database Setup
################################################
url = 'postgresql://postgres:fev403@localhost:5432/sql_db'

################################################
#Flask Setup
################################################
app = Flask(__name__,static_folder='static/css')

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class complete_db(db.Model):
    rank = db.Column(db.Integer)
    city = db.Column(db.String, primary_key=True)
    state_id = db.Column(db.String)
    census_2020 = db.Column(db.Integer)
    census_2010= db.Column(db.Integer)
    change = db.Column(db.Float)
    state_name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    costofliving = db.Column(db.Float)
    localpurchasingpower= db.Column(db.Float)
    groceries = db.Column(db.Float)
    rent = db.Column(db.Float)
    restaurant = db.Column(db.Float)
    f500_average_rank = db.Column(db.Integer)
    f500_total_companies = db.Column(db.Integer)
    f500_total_employees = db.Column(db.Integer)
    f500_total_revenue = db.Column(db.Integer)
    f500_total_profit = db.Column(db.Float)
    total_venues = db.Column(db.Integer)
    total_superbowls = db.Column(db.Integer)

db.create_all()



#create route that renders index.html template

#Query the database and send the jsonified results
@app.route('/')
def city():
    cities = complete_db.query.all()
    return render_template("index.html", cities=cities)

@app.route('/table')
def db():
    cities = complete_db.query.all()
    return render_template("table.html", cities=cities)

@app.route('/chart1')
def chart1():
    csv_path = "static/data/complete_db.csv"

    
    df = pd.read_csv(csv_path, encoding="utf-8")


    fig = px.bar(df, x="state_name", y= "change", color="city")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Population Change from 2010 to 2020"
    description = """
    This chart represents a ten year record of population change in 384 major cities in the United States.
    """
    
    return render_template('chart1.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart2')
def chart2():
    csv_path = "static/data/complete_db_drop_null.csv"
    df = pd.read_csv(csv_path, encoding="utf-8")


    fig = px.line(df, x="city", y=["costofliving","localpurchasingpower","groceries","rent", "restaurant"])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Family Finances"
    description = """
    This chart illustrates the cost of living, local purchasing power, cost of groceries, price of rent and restaurant rates for major cities in the United States.
    """
    return render_template('chart1.html', graphJSON=graphJSON, header=header,description=description)


@app.route('/map',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'pk.eyJ1IjoidG91c3NhaTM3IiwiYSI6ImNrdWdybXF3MjI2eTgycW56YmRma291MDkifQ.jyWjx_9fTCFsaVyatqwDjA'

  return render_template('map.html',
        mapbox_access_token=mapbox_access_token)


if __name__ == "__main__":
    app.run(debug=True)