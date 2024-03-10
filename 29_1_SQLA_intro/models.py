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
    first_name = db.Column(db.Text,
                     nullable=False,
                     unique=False)
    last_name = db.Column(db.Text,
                     nullable=False,
                     unique=False)
    image_url = db.Column(db.Text, nullable=False)
    
    @property
    def full_name(self):
    
        """Return the full name of a user
        """
        u = self # current user
        
        return f"{u.first_name} {u.last_name}"



class Post(db.Model):
    """posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text,
                     nullable=False,
                     unique=False)
    content = db.Column(db.Text,
                     nullable=False,
                     unique=False)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)