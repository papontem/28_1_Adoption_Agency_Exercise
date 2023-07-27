" Models for Adoption Agencys Pets"
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

# MODELS BELOW:
# All models should subclass db.Model

class Pet(db.Model):
    """ Pet. """
    # creating pets table list
    __tablename__ = "pets"

    # Columns
    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name      = db.Column(db.String(100), nullable=False)
    species   = db.Column(db.String(100), nullable=False)
    age       = db.Column(db.Integer)
    available = db.Column(db.Boolean, nullable=False, default=True)
    notes     = db.Column(db.Text)
    photo_url = db.Column(db.Text)

    # # Table Relations
    # TODO: None ATM, in the future maybe
    
    # Methods

    def __repr__(self):
        p = self
        return f"""<Pet id#={p.id} | name={p.name} | species={p.species} |  age={p.age} |
        available={p.available} | notes={p.notes} | photo_prl={p.photo_url} >""" 