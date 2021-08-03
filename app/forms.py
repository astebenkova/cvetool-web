from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import InputRequired, Regexp


class ImageForm(FlaskForm):
    image = StringField("Image", [InputRequired("Please, enter an image name")])
    processors = SelectMultipleField("Processors", choices=[("PaclairProcessor", "PaclairProcessor"),
                                                            ("LabelProcessor", "LabelProcessor"),
                                                            ("LanguagePackagesProcessor", "LanguagePackagesProcessor"),
                                                            ("Clairv4Processor", "Clairv4Processor")],
                                     default=["PaclairProcessor", "LabelProcessor", "LanguagePackagesProcessor"])
    representers = SelectField("Representers", choices=[("DetailedHTML", "DetailedHTML"),
                                                        ("HumanMirrored", "HumanMirrored")], default="HumanMirrored")
    submit = SubmitField("Run scan")
