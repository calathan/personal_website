from flask import Flask, render_template, request, jsonify
from datetime import date

app = Flask(__name__)

### HTML WEB PAGES ###
@app.route("/")
def hello_world():
    today = todays_date()
    return render_template("index.html", the_date = today)
    
@app.route("/about")
def about_me():
    return  render_template("about_me.html")
    
@app.route("/links")
def links():
    return  render_template("links.html")
    
    
def todays_date():
    today = date.today()
    str_date = today.strftime("%B %d, %Y")
    return "Today's date is " + str_date
    
    
### ### ### ### ### ### ### ### ### API PORTION ### ### ### ### ### ### ### ### ###
app.config['DEBUG'] = True

drivers = [
    {'id': 0,
     'name': 'Lewis Hamilton',
     'born': '1985',
     'team': 'Mercedes AMG Petronas',
     'points': '180'},
    {'id': 1,
     'name': 'Max Verstappen',
     'born': '1997',
     'team': 'Red Bull Racing',
     'points': '366'},
    {'id': 2,
     'name': 'Lando Norris',
     'born': '1999',
     'team': 'McLaren',
     'points': '101'}
     ]

@app.route("/api", methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1> <p>This site is a proptotype API for things.</p>"
    
    
@app.route("/api/v1/resources/drivers/all", methods=['GET'])
def api_all():
    return jsonify(drivers)
    
    
@app.route("/api/v1/resources/drivers", methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please spcify an id."
        
    results = []
    
    for driver in drivers:
        if driver['id'] == id:
                results.append(driver)
        else:
            results = "ID NOT FOUND"
                
    return jsonify(results)