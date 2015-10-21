"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Rating, Movie


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/login-form")
def login_form():
    """Show login form"""

    return render_template("login-form.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Find user in database by their email, check their password, and store
    tuser id in session. Finally, redirect to homepage."""

    email = request.form.get("email")
    password = request.form.get("password")

    # query database to find user with given email

    # if email in db:
    #     if password is correct:
    #         store id in session
    #         redirect to user page
    #     else:
    #         flash error message and redirect to login-form
    # else:
    #     flash error message and stay on login-form


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user-list.html", users=users)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()