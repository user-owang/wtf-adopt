from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class AddPetForm(FlaskForm):
  """form for adding pets"""
  name = StringField("Name", validators=[InputRequired(message='A pet name is required')])
  species = StringField('Species', validators=[InputRequired('A pet species is required'), AnyOf(values=['cat','dog','porcupine'], message='At this time we only accept cats, dogs or porcupines.')])
  img_url = StringField('Link to photo', validators=[Optional(), URL(message='Please enter a valid URL')])
  age = FloatField('Age', validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 and 30.')])
  notes = StringField('Additional Notes', validators=[Optional()])
  
class EditPetForm(FlaskForm):
  """form to edit pets"""
  notes = StringField('Additional Notes', validators=[Optional()])
  status = BooleanField('Available to Adopt')
  img_url = StringField('Updated Image Link', validators=[Optional(), URL(message='Please enter a valid URL')])