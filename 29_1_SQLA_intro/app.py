"""Blogly application."""
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User, Post, example_data, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension

# flask app config
app = Flask(__name__)

#SQLA Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = "SECRET!"

# Connect to database and sample data to database
connect_db(app)
with app.app_context():
    # db.create_all()
    example_data()

#debugtoolbar setup
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
debug = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """Show the three most recent posts."""

    posts = Post.query.order_by(Post.created_at.desc()).limit(3).all()
    return render_template("home_page.html", posts=posts)


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
    flash(f"User {user.full_name} added.")

    return redirect("/users")


@app.route("/users/<int:user_id>")
def user_detail(user_id):
    """Show detail info on a single user."""

    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id = user.id)
    
    return render_template("user_detail.html", user=user, posts=posts)


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
    flash(f"User {user.full_name} edited.")   
    
    return redirect("/users")


@app.route("/users/<int:user_id>/delete", methods=['POST'])
def delete_user(user_id):
    """Delete a user and redirect to user listing."""

    user = User.query.get_or_404(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        flash(f"User {user.full_name} deleted.")
    
    return redirect("/users")


##############################################################################
# Posts route


@app.route("/users/<int:user_id>/posts/new")
def new_post_page(user_id):
    """Show form to add a post for that user."""
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    
    return render_template("new_post_form.html", user=user, tags=tags)


@app.route("/users/<int:user_id>/posts/new", methods=['POST'])
def post_form(user_id):
    """Handle add form; add post and redirect to the user detail page."""

    title = request.form['title']
    content = request.form['content']
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    post = Post(title=title, content=content, user_id=user_id, tags=tags)
    db.session.add(post)
    db.session.commit()
    
    flash(f"Post '{post.title}' added.")

    return redirect(f'/users/{user_id}')
    
    
@app.route("/posts/<int:post_id>")
def post_detail(post_id):
    """Show a post. Show buttons to edit and delete the post."""

    post = Post.query.get_or_404(post_id)
    
    return render_template("post_detail.html", post=post)


@app.route("/posts/<int:post_id>/edit")
def edit_post_page(post_id):
    """Show form to edit a post, and to cancel (back to user page)."""

    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    
    return render_template("edit_post.html", post=post, tags=tags)


@app.route("/posts/<int:post_id>/edit", methods=['POST'])
def edit_post(post_id):
    """Handle editing of a post. Redirect back to the post view."""

    post = Post.query.get_or_404(post_id)

    post.title = request.form['title']
    post.content = request.form['content']
    post.user_id = post.user_id
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    post.tags = tags

    db.session.commit()
    flash(f"Post '{post.title}' edited.")

    return redirect(f'/users/{post.user_id}')


@app.route("/posts/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    """Delete the post"""
    post = Post.query.get_or_404(post_id)
    
    if post:
        db.session.delete(post)
        db.session.commit()
        flash(f"Post '{post.title} deleted.")
    
    return redirect(f"/users/{post.user_id}")


##############################################################################
# tags route


@app.route('/tags')
def tag_list():
    """Lists all tags, with links to the tag detail page.
    """
    tags = Tag.query.all()
    return render_template("tag_list.html", tags=tags)


@app.route("/tags/<int:tag_id>")
def tag_detail(tag_id):
    """Show detail about a tag. Have links to edit form and to delete."""

    tag = Tag.query.get_or_404(tag_id)
    
    return render_template("tag_detail.html", tag=tag)


@app.route("/tags/new")
def new_tag_form():
    """Shows a form to add a new tag."""
    
    return render_template("add_tag.html")


@app.route("/tags/new", methods=['POST'])
def new_tag():
    """Process add form, adds tag, and redirect to tag list."""
    
    name = request.form['name']

    tag = Tag(name=name)
    
    db.session.add(tag)
    db.session.commit()
    # flash(f"User {user.full_name} added.")

    return redirect("/tags")


@app.route("/tags/<int:tag_id>/edit")
def edit_tag_form(tag_id):
    """Show edit form for a tag."""

    tag = Tag.query.get_or_404(tag_id)
    
    return render_template("edit_tag.html", tag=tag)

@app.route("/tags/<int:tag_id>/edit", methods=['POST'])
def edit_tag(tag_id):
    """Process edit form, edit tag, and redirects to the tags list."""

    tag = Post.query.get_or_404(tag_id)

    tag.name = request.form['name']

    db.session.commit()
    # flash(f"Post '{post.title}' edited.")

    return redirect('/tags')



@app.route("/tags/<int:tag_id>/delete", methods=['POST'])
def delete_tag(tag_id):
    """Delete the tag"""
    tag = Tag.query.get_or_404(tag_id)
    
    if tag:
        db.session.delete(tag)
        db.session.commit()
        # flash(f"Post '{post.title} deleted.")
    
    return redirect("/tags")