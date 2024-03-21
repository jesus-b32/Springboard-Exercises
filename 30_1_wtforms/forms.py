"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class AddPetForm(FlaskForm):
    """Form for adding/editing friend."""

    name = StringField("Name",
                        validators=[InputRequired()])
    species = SelectField("Specieces",
                          choices=[('dog', 'Dog'), ('cat', 'Cat'), ('porcupine', 'Porcupine')],
                        validators=[InputRequired()])
    photo_url = URLField("Photo URL",
                        validators=[Optional()])
    age = IntegerField("Age",
                        validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes",
                        validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for adding/editing friend."""

    photo_url = URLField("Photo URL",
                        validators=[Optional(), URL()])
    notes = StringField("Notes",
                        validators=[Optional()])
    available = BooleanField("Available",
                        validators=[InputRequired()])