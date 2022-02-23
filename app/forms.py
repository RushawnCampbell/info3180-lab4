from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    fileField = FileField('image upload',validators=[DataRequired()])