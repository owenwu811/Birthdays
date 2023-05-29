import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db") #flask is connecting to sqllite database using connection string, which then begins populating user values into this birthdays table
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        #request.form parses the user's form data. Get is a built in dictinoary method in Python that returns the value of the specified key
        name = request.form.get("name") #request.form is a dictionary-like object in flask that contains data from HTTP Post request consisting of key, value pairs with the key being the name of the user and values being the values submitted by the user
        day = request.form.get("day")
        month = request.form.get("month")
        db.execute("INSERT INTO birthdays(name, month, day) VALUES(?, ?, ?)", name, month, day) #db.execute is a method in flask that let's you insert a new row into the birthdays table in the birthdays.db database, in this case. ? are used as placeholders and also to prevent sql injection attacks by sanitizing data before it is inserted into the database
        return redirect("/")
    else:
        # TODO: Display the entries in the database on index.html
        birthday = db.execute("SELECT * FROM BIRTHDAYS") #db.execute is querying data from birthdays table and saving all rows into empty list variable called birthday
        #bithdays is just creating a list that queries data from the built in sqllite database that is used to store information the users submit via forms
        return render_template("index.html", birthdays=birthday) #we pass birthday list into the render_template function so that Flask can use Jinja2 to generate HTML that displays the data from the birthdays list in a table on the webpage

    
    #note that db.execute can be found in docs here: https://cs50.readthedocs.io/libraries/cs50/python/
    
