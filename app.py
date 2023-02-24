from flask import Flask, render_template
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
    
    
### API PORTION ###
app.config['DEBUG'] = True

@app.route("/api", methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1> <p>This site is a proptotype API for things.</p>"