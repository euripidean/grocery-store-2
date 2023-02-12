from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

from grocery_app.models import ItemCategory, GroceryStore

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Store Title', validators = [DataRequired()])
    address = StringField('Store Address', validators = [DataRequired()])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Item Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo (URL)', validators=[DataRequired()])
    store = QuerySelectField('Store', query_factory= lambda: GroceryStore.query, get_label='title', allow_blank=False)
    submit = SubmitField('Submit')
