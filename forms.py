"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional


class AddPetsForm(FlaskForm):
    """Form for adding Pets"""

    name      = StringField("Pet name"         , validators=[InputRequired(message="Name cannot be blank")])
    species   = StringField("Pet species"      , validators=[InputRequired(message="Species cannot be blank")])
    photo_url = StringField("Link photo of pet", validators=[Optional()])
    age       = FloatField( "Pet age in years" , validators=[Optional()])
    notes     = StringField("any notes?"       , validators=[Optional()])
