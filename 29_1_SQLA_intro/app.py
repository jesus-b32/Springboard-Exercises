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

#debugtoolbar setup
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
debug = DebugToolbarExtension(app)

# Connect to database and create all tables
connect_db(app)
db.create_all()




@app.route("/")
def user_listing():
    """List users and an add user button"""

    users = User.query.all()
    return render_template("list.html", users=users)



@app.route("/new_user")
def new_user_page():
    """Display a create user form."""
    

    return render_template("new_user.html")



@app.route("/new_user", methods=["POST"])
def add_user():
    """Add user and redirect to list of users."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/")


@app.route("/<int:user_id>")
def user_detail(user_id):
    """Show detail info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)


@app.route("/<int:user_id>/edit")
def edit_user_page(user_id):
    """Display edit form for a user."""

    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)


@app.route("/<int:user_id>/edit", methods=['POST'])
def edit_user(user_id):
    """Edit user and redirect to user detail page."""

    user = User.query.get_or_404(user_id)
    return redirect(f"/<int:user_id>")


@app.route("/<int:user_id>/delete")
def delete_user(user_id):
    """Delete a user and redirect to user listing."""

    User.query.get_or_404(user_id).delete()
    db.session.commit()
    
    return redirect(f"/")