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
def add_snack():
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


# @app.route("/users/<int:uid>/edit", methods=["GET", "POST"])
# def edit_user(uid):
#     """Show user edit form and handle edit."""

#     user = User.query.get_or_404(uid)
#     form = UserForm(obj=user)

#     if form.validate_on_submit():
#         user.name = form.name.data
#         user.email = form.email.data
#         db.session.commit()
#         flash(f"User {uid} updated!")
#         return redirect(f"/users/{uid}/edit")

#     else:
#         return render_template("user_form.html", form=form)
