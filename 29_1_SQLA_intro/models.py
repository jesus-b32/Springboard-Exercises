"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """users"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(20), #use Text instead of String() next time for no character lemgth limit
                     nullable=False,
                     unique=False)
    last_name = db.Column(db.String(20),
                     nullable=False,
                     unique=False)
    image_url = db.Column(db.String(500), nullable=False)
    
    @property
    def full_name(self):
    
        """Return the full name of a user
        """
        u = self # current user
        
        return f"{u.first_name} {u.last_name}"
