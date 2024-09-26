import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request  
    
# Configure application
app = Flask(__name__)

# Configure a secret key
app.secret_key = os.urandom(24)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

# Ensure the user get the lastest version from the server every request they send
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

        # Add the user's entry into the database
        name = request.form.get("name")
        if not name:
            return redirect("/")

        day = request.form.get("day")
        if not day:
            return redirect("/")
        try:
            day = int(day)
        except ValueError:
            return redirect("/")
        if day < 0 or day > 31:
            return redirect("/")

        month = request.form.get("month")
        if not month:
            return redirect("/")
        try:
            month = int(month)
        except ValueError:
            return redirect("/")

        if month < 0 or month > 12:
            return redirect("/")

        # Insert into database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        
        # Notify the user with the flash message
        flash(f"{name}'s birthday is successfully added!")

        return redirect("/")

    else:

        # Display the entries in the database on index.html

        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)
