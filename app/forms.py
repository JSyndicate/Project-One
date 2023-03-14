from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired, FileField

class Add_New_Property_Form(FlaskForm):
    Type = StringField('Type')
    Photo = FileField('Choose a Photo', validators=[FileRequired(), FileAllowed(['jpg','png'])])
    Title_of_Property = StringField('Title_of_Property', validators=[InputRequired()])
    Number_of_Bedrooms = StringField('Number_of_Bedrooms', validators=[InputRequired()])
    Number_of_Bathrooms = StringField('Number_of_Bathrooms', validators=[InputRequired()])
    Location = StringField('Location', validators=[InputRequired()])
    Price = StringField('Price', validators=[InputRequired()])
    Description = StringField('Description', validators=[InputRequired()])