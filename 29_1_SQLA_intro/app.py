"""Blogly application."""
from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

# flask app config
app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET!"

#SQLA Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Connect to database and create all tables
connect_db(app)


#debugtoolbar setup
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
debug = DebugToolbarExtension(app)



@app.route("/")
def homepage():
    """List users and an add user button""" 
    
    return redirect('/users')


@app.route("/users")
def user_list():
    """List users and an add user button."""
    
    users = User.query.order_by(User.last_name, User.first_name).all()
    
    return render_template("user_list.html", users=users)


@app.route("/users/new")
def new_user_page():
    """Display a create a user form."""

    return render_template("add_user.html")



@app.route("/users/new", methods=["POST"])
def add_user():
    """Add user and redirect to list of users."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>")
def user_detail(user_id):
    """Show detail info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("user_detail.html", user=user)


@app.route("/users/<int:user_id>/edit")
def edit_user_page(user_id):
    """Display edit form for a user."""

    user = User.query.get_or_404(user_id)
    
    return render_template("edit_user.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=['POST'])
def edit_user(user_id):
    """Edit user and redirect to user detail page."""
    user = User.query.get_or_404(user_id)
    
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    
    db.session.commit()   
    
    return redirect("/users")


@app.route("/users/<int:user_id>/delete", methods=['POST'])
def delete_user(user_id):
    """Delete a user and redirect to user listing."""

    item_to_delete = User.query.get_or_404(user_id)
    if item_to_delete:
        db.session.delete(item_to_delete)
        db.session.commit()
    
    return redirect("/users")