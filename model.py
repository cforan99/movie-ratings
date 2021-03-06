"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
import datetime

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "Users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)

class Movie(db.Model):
    """Movie to be rated"""

    __tablename__ = "Movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(64), nullable=True)
    released_at = db.Column(db.DateTime, nullable=True)
    imdb_url = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Movie movie_id=%s title=%s>" % (self.movie_id, self.title)

class Rating(db.Model):
    """Ratings from users for movies."""

    __tablename__ = "Ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('Movies.movie_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'),nullable=False)
    score = db.Column(db.Integer, nullable=False)

    movie = db.relationship('Movie', backref=db.backref('ratings'))
    user = db.relationship('User', backref=db.backref('ratings'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating rating_id: %i movie_id: %i user_id: %i>" % (self.rating_id, self.movie_id, self.user_id)


# TODO: Define relationships and foreign keys
# Consider using db.ForeignKey('movie_id') - https://pythonhosted.org/Flask-SQLAlchemy/models.html


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ratings.db'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
