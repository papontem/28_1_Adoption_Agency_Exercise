from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetsForm(FlaskForm):
    """Form for adding Pets"""

    species_choices = ['cat', 'dog', 'porcupine']

    name = StringField("Pet Name",
                        validators=[InputRequired(message="Name cannot be blank")])
    
    species = StringField("Pet Species",
                           validators=[
                               InputRequired(message="Species cannot be blank"),
                               AnyOf(species_choices, message="We are only accepting pet species of 'cat', 'dog' and 'porcupine'")
                               ])
    
    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL(message="Invalid URL")])
    
    age = FloatField("Pet Age",
                      validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30 years of age.")])
    
    notes = StringField("Notes", 
                        validators=[Optional()])
    
    available = BooleanField("Available?",validators=[Optional()])


# ADD AN EDIT FORM 
class EditPetsForm(FlaskForm):
    """Form for editing Pets"""

    photo_url = StringField("Photo URL", 
                            validators=[Optional(), URL(message="Invalid URL")])
    
    notes = StringField("Notes", 
                        validators=[Optional()])
    
    available = BooleanField("Available?",validators=[Optional()])