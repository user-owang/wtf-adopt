"""Pet adoption application."""

from flask import Flask, request, redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somethinginthashkdgkhs2341'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
with app.app_context():
    db.create_all()

debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
  """shows all pets in db"""
  pets = Pet.query.all()
  return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
  """add a new pet to the db"""
  form = AddPetForm()
  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    img_url = form.img_url.data
    age = form.age.data
    notes = form.notes.data
    optionals = [img_url,age,notes]
    for input in optionals:
      if input != "":
        input = None

    new_pet = Pet(name=name, species=species, img_url=img_url, age=age, notes=notes)
    
    db.session.add(new_pet)
    db.session.commit()
    return redirect('/')
  else:   
    return render_template('add_pet.html', form = form)
  
@app.route('/<int:id>', methods = ['GET','POST'])
def show_details(id):
  """Shows pet details and edits notes, img or status"""
  pet = Pet.query.get_or_404(id)
  form = EditPetForm(obj=pet)
  if form.validate_on_submit():
    pet.img_url = form.img_url.data if form.img_url.data != '' else None
    pet.notes = form.notes.data if form.notes.data != '' else None
    pet.status = form.status.data
    
    db.session.commit()
    return redirect('/')
  else:
    return render_template('pet_details.html', form=form, pet=pet)
