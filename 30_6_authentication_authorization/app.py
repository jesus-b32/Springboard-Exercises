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
    # form = TweetForm()
    # all_tweets = Tweet.query.all()
    # if form.validate_on_submit():
    #     text = form.text.data
    #     new_tweet = Tweet(text=text, user_id=session['user_id'])
    #     db.session.add(new_tweet)
    #     db.session.commit()
    #     flash('Tweet Created!', 'success')
    #     return redirect('/tweets')

    # return render_template("tweets.html", form=form, tweets=all_tweets)
    return render_template('user_info.html', user=user,
                           feedbacks=feedbacks)


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


@app.route('/logout')
def logout_user():
    """
    Clear any information from the session and redirect to /
    """
    session.pop('username')
    flash("Goodbye!", "info")
    return redirect('/')



# @app.route('/tweets/<int:id>', methods=["POST"])
# def delete_tweet(id):
#     """Delete tweet"""
#     if 'user_id' not in session:
#         flash("Please login first!", "danger")
#         return redirect('/login')
#     tweet = Tweet.query.get_or_404(id)
#     if tweet.user_id == session['user_id']:
#         db.session.delete(tweet)
#         db.session.commit()
#         flash("Tweet deleted!", "info")
#         return redirect('/tweets')
#     flash("You don't have permission to do that!", "danger")
#     return redirect('/tweets')
