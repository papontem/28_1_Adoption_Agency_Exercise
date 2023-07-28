from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetsForm

app = Flask(__name__)
# FLASK SETTINGS
app.config["SECRET_KEY"] = "oh-so-secret"
# FLASK-SQLALCHEMY SETTINGS
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# FLASK-DEBUGTOOLBAR SETTINGS
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app) 

# flask-sqlalchemy init app db
connect_db(app)


@app.route("/")
def homepage():
    """Show homepage links."""

    pets = Pet.query.all()

    return render_template("home.html",pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Pet add form; handle adding."""

    form = AddPetsForm()

    if form.validate_on_submit():
        # form was valid, get its data
        name      = form.name.data
        species   = form.species.data 
        photo_url = form.photo_url.data
        age       = form.age.data
        notes     = form.notes.data
        # create new pet
        new_pet = Pet(name=name, species=species, age=age, notes=notes, photo_url=photo_url)
        db.session.add(new_pet)
        db.session.commit()
        # flash user success
        flash(f"Added a New Pet!", "success")
        # redirect
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_details_pet(pet_id):
    """Show pet details and edit form and handle edit."""

    pet = Pet.query.get_or_404(pet_id)

    form = AddPetsForm(obj=pet)

    # pythons native debugger stalls when hit
    # import pdb
    # pdb.set_trace()


    if form.validate_on_submit():
        # #### TODO: for some reason the form validation keeps failing
        ## data from forms thats prefilled by pet obj in route doesnt get filled if i dont render the field.
        ## validates corrrectly if i display the name and species fields.
        #  (´･_･`) so just ignore whatever name or species user tries to input

        # Edit the pets data
        pet.photo_url = form.photo_url.data
        pet.notes     = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        # flash user success
        flash(f"Pet {pet.id} updated!","success")

        return redirect(f"/")

    else:

        # raise

        return render_template("edit_details_pet_form.html",pet=pet, form=form)
