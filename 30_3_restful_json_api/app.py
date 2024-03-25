"""Flask app for Cupcakes"""
from flask import Flask, render_template, flash, redirect, render_template, url_for, jsonify, request
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from seed import seeding_data

# from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
# debug = DebugToolbarExtension(app)

connect_db(app)
# with app.app_context():
#     seeding_data()
    

# @app.route("/")
# def homepage():
#     """Show homepage with pet list."""
    
#     pets = Pet.query.all()

#     return render_template("homepage.html", pets=pets)


@app.route("/api/cupcakes")
def list_cupcakes():
    """Get data about all cupcakes. 
    Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}.
    The values should come from each cupcake instance.
    """

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Get data about a single cupcake. 
    Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}. 
    This should raise a 404 if the cupcake cannot be found.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.serialize())


@app.route("/api/cupcakes", methods=['POST'])
def add_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request. 
    Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
    """
    cupcake = Cupcake(flavor=request.json['flavor'],
                          size=request.json['size'],
                          rating=request.json['rating'],
                          image=request.json['image'] or None)

    db.session.add(cupcake)
    db.session.commit()
    
    response_json = jsonify(cupcake = cupcake.serialize())

    return (response_json, 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Update a cupcake with the id passed in the URL and flavor, size, rating and image data from the body of the request. 
    You can always assume that the entire cupcake object will be passed to the backend. 
    This should raise a 404 if the cupcake cannot be found. 
    Respond with JSON of the newly-updated cupcake, like this: {cupcake: {id, flavor, size, rating,image}}.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    cupcake.flavor = request.json.get('flavor')
    cupcake.size = request.json.get('size')
    cupcake.rating = request.json.get('rating')
    cupcake.image = request.json.get('image')
    db.session.commit()
    
    return jsonify(cupcake = cupcake.serialize())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """This should raise a 404 if the cupcake cannot be found.
Delete cupcake with the id passed in the URL. Respond with JSON like {message: "Deleted"}.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message='Deleted')