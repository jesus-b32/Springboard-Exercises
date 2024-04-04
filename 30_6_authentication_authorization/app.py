from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


connect_db(app)
# with app.app_context():
#     db.drop_all()
#     db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    
    return redirect('/register')
    
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """
    GET:
    Show a form that when submitted will register/create a user.
    This form should accept a username, password, email, first_name, and last_name.
    
    POST:
    Process the registration form by adding a new user.
    Then redirect to /secret
    """
    if "username" in session:
        username = session['username']
        return redirect(f'/users/{username}')
    
    form = RegisterForm()
    if form.validate_on_submit():    
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        user = User.register(**data)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken.  Please pick another')
            return render_template('register.html', form=form)
        session['username'] = user.username
        flash('Welcome! Successfully Created Your Account!', "success")
        return redirect(f'/users/{user.username}')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    """
    GET:
    Show a form that when submitted will login a user.
    This form should accept a username and a password.
    
    POST:
    Process the login form, ensuring the user is authenticated and going to /secret if so.
    """
    if "username" in session:
        username = session['username']
        return redirect(f'/users/{username}')
        
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('login.html', form=form)


@app.route('/users/<username>')
def show_secret(username):
    """
    Show information about the given user. 
    Show all of the feedback that the user has given. 
    For each piece of feedback, display with a link to a form to edit the feedback and a button to delete the feedback. 
    Have a link that sends you to a form to add more feedback and a button to delete the user. 
    Make sure that only the user who is logged in can successfully view this page.
    """
    if "username" not in session:
        flash("Please login first!", "danger")
        return redirect('/')
    user = User.query.get_or_404(username)
    feedbacks = Feedback.query.filter_by(username=username)

    return render_template('user_info.html', user=user,
                           feedbacks=feedbacks)

@app.route('/users/<username>/delete', methods=["POST"])
def delete_user(username):
    """Remove the user from the database and make sure to also delete all of their feedback.
    Clear any user information in the session and redirect to /.
    Make sure that only the user who is logged in can successfully delete their account.
    """
    if 'username' not in session:
        flash("Please login first!", "danger")
        return redirect('/')
    
    user = User.query.get_or_404(username)
    if user.username == session['username']:
        session.pop('username')
        db.session.delete(user)
        db.session.commit()
        
        flash("User deleted!", "info")
        return redirect('/')
    flash("You don't have permission to do that!", "danger")
    return redirect(f'/users/{user.username}')



@app.route('/users/<username>/feedback/add', methods=['GET', 'POST'])
def add_feedback(username):
    """
    GET:
    Display a form to add feedback.
    Make sure that only the user who is logged in can see this form.
    
    POST:
    Add a new piece of feedback and redirect to /users/<username>
    Make sure that only the user who is logged in can successfully add feedback.
    """
    if "username" not in session:
        flash("Please login first!", "danger")
        return redirect('/')
    
    form = FeedbackForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        feedback = Feedback(title=title, content=content, username=username)
        db.session.add(feedback)
        db.session.commit()
        
        return redirect(f'/users/{username}')

    return render_template('feedback.html', form=form)



@app.route('/feedback/<feedback_id>/update', methods=['GET', 'POST'])
def update_feedback(feedback_id):
    """
    GET:
    Display a form to edit feedback.
    Make sure that only the user who has written that feedback can see this form.
    
    POST:
    Update a specific piece of feedback and redirect to /users/<username>
    Make sure that only the user who has written that feedback can update it.
    """
    if "username" not in session:
        flash("Please login first!", "danger")
        return redirect('/')
    
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback.query.get_or_404(feedback_id)
        feedback.title = form.title.data
        feedback.content = form.content.data

        db.session.commit()
        
        return redirect(f'/users/{feedback.username}')

    return render_template('feedback.html', form=form)


@app.route('/feedback/<feedback_id>/delete', methods=["POST"])
def delete_feeback(feedback_id):
    """Delete a specific piece of feedback and redirect to /users/<username>
    Make sure that only the user who has written that feedback can delete it.
    """
    if 'username' not in session:
        flash("Please login first!", "danger")
        return redirect('/')
    
    feedback = Feedback.query.get_or_404(feedback_id)
    if feedback.username == session['username']:
        db.session.delete(feedback)
        db.session.commit()
        
        flash("Feedback deleted!", "info")
        return redirect(f'/users/{feedback.username}')
    flash("You don't have permission to do that!", "danger")
    return redirect(f'/users/{feedback.username}')


@app.route('/logout')
def logout_user():
    """
    Clear any information from the session and redirect to /
    """
    session.pop('username')
    flash("Goodbye!", "info")
    return redirect('/')
