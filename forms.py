from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetsForm(FlaskForm):
    """Form for adding Pets"""

    species_choices = ['cat', 'dog', 'porcupine']

    name = StringField("Pet name",
                        validators=[InputRequired(message="Name cannot be blank")])
    
    species = StringField("Pet species",
                           validators=[
                               InputRequired(message="Species cannot be blank"),
                               AnyOf(species_choices, message="We are only accepting pet species of 'cat', 'dog' and 'porcupine'")
                               ])
    
    photo_url = StringField("Link photo of pet", 
                            validators=[Optional(), URL(message="Invalid URL")])
    
    age = FloatField("Pet age in years",
                      validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30 years of age.")])
    
    notes = StringField("any notes?", 
                        validators=[Optional()])
