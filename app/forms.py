from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import InputRequired, Regexp


class ImageForm(FlaskForm):
    image = StringField("Image", [InputRequired()])
    processors = SelectMultipleField("Processors", choices=[(1, "ALL"), (2, "LabelProcessor"), (3, "PaclairProcessor"), (4, "LanguagePackagesProcessor"), (5, "Clairv4Processor")], default=[1])
    submit = SubmitField("Run scan")
