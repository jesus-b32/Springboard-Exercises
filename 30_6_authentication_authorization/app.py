from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User
from forms import RegisterForm
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
    """Show a form that when submitted will register/create a user.
    This form should accept a username, password, email, first_name, and last_name.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        
        # username = form.username.data
        # password = form.password.data
        # email = form.email.data
        # first_name = form.first_name.data
        # last_name = form.last_name.data

        # user = User.register(username,
        #                          password,
        #                          email,
        #                          first_name,
        #                          last_name)
        
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        user = User.register(**data)
        # user = User(**data)
        
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken.  Please pick another')
            return render_template('register.html', form=form)
        # session['user_id'] = user.id
        flash('Welcome! Successfully Created Your Account!', "success")
        return redirect('/register')

    return render_template('register.html', form=form)


# @app.route('/register', methods=['GET', 'POST'])
# def show_tweets():
#     if "user_id" not in session:
#         flash("Please login first!", "danger")
#         return redirect('/')
#     form = TweetForm()
#     all_tweets = Tweet.query.all()
#     if form.validate_on_submit():
#         text = form.text.data
#         new_tweet = Tweet(text=text, user_id=session['user_id'])
#         db.session.add(new_tweet)
#         db.session.commit()
#         flash('Tweet Created!', 'success')
#         return redirect('/tweets')

#     return render_template("tweets.html", form=form, tweets=all_tweets)


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


# @app.route('/login', methods=['GET', 'POST'])
# def login_user():
#     form = UserForm()
#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data

#         user = User.authenticate(username, password)
#         if user:
#             flash(f"Welcome Back, {user.username}!", "primary")
#             session['user_id'] = user.id
#             return redirect('/tweets')
#         else:
#             form.username.errors = ['Invalid username/password.']

#     return render_template('login.html', form=form)


# @app.route('/logout')
# def logout_user():
#     session.pop('user_id')
#     flash("Goodbye!", "info")
#     return redirect('/')
