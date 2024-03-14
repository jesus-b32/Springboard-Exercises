"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

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
    
    posts = db.relationship("Post", back_populates="users",cascade="all, delete", passive_deletes=True)
    
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
                     nullable=False)
    content = db.Column(db.Text,
                     nullable=False)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=datetime.datetime.now)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id', ondelete='CASCADE'), #ondelete='CASCADE'
                        nullable=False)
    users = db.relationship('User', back_populates="posts")
    
    @property
    def friendly_date(self):
        """Return better formatted date and time."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")
    

class Tag(db.Model):
    """tags"""

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     unique = True,
                     nullable=False)

    posts = db.relationship(
        'Post',
        secondary="posts_tags",
        cascade="all,delete",
        backref="tags")    
    
    
class PostTag(db.Model):
    """post_tags"""

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer,
                   db.ForeignKey('posts.id'),
                   primary_key=True)
    tag_id = db.Column(db.Integer,
                     db.ForeignKey('tags.id'),
                     primary_key=True)



def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    # Tag.query.delete()
    # Post.query.delete()
    for user in User.query.all():
        db.session.delete(user)    
    # db.session.commit()
    
    # User.query.delete()
    for post in Post.query.all():
        db.session.delete(post)   
    # db.session.commit()
    
    for tag in Tag.query.all():
        db.session.delete(tag)
    
    # Add sample employees and departments
    user1 = User(first_name='John', last_name='Doe', image_url='https://as2.ftcdn.net/v2/jpg/01/24/41/03/1000_F_124410367_M538eQuhp4ItuXE2RVt5m75kODW2nTZz.jpg')
    user2 = User(first_name='Jane', last_name='Smith', image_url='https://media.istockphoto.com/id/528415533/vector/emoticon-with-tears-of-joy.jpg?s=612x612&w=0&k=20&c=zt919iGd1ZSJ2kFU0g676iVKLamUXMSjMD2s-NkV8_c=')
    
    post1 = Post(title='First Post', content='Hello World', user_id=1)
    post2 = Post(title='Second Post', content='Good Morning', user_id=1)
    post3 = Post(title='Third Post', content='Good Night', user_id=2)
    post4 = Post(title='Fourth Post', content='I am tired.', user_id=2)
    
    tag1 = Tag(name='fun')
    tag2 = Tag(name='new')
    tag3 = Tag(name='sad')
    tag4 = Tag(name='cool')

    db.session.add_all([user1, user2, post1, post2, post3, post4, tag1, tag2, tag3, tag4])
    
    db.session.commit()