from flask import Flask, render_template, flash, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, testing_data

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///wtforms_exercise"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
debug = DebugToolbarExtension(app)

connect_db(app)
# with app.app_context():
#     testing_data()
    

@app.route("/")
def homepage():
    """Show homepage with pet list."""
    
    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        
        # pet = Pet(name = name,
        #           species = species,
        #           photo_url = photo_url,
        #           age = age,
        #           notes = notes)
        
        #alternative way of extracting field data shown above
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        pet = Pet(**data)
        
        db.session.add(pet)
        db.session.commit()

        return redirect(url_for('homepage'))

    else:
        return render_template("add_pet.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show pet edit form and handle edit."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect(url_for('homepage'))

    else:
        return render_template("edit.html", form=form, pet=pet)
