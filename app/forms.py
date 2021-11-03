from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SelectField
from wtforms.validators import InputRequired


class ImageForm(FlaskForm):
    image = StringField("Image", [InputRequired("Please, enter an image name")])
    processors = SelectMultipleField("Processors", choices=[("PaclairProcessor", "PaclairProcessor"),
                                                            ("LabelProcessor", "LabelProcessor"),
                                                            ("LanguagePackagesProcessor", "LanguagePackagesProcessor"),
                                                            ("Clairv4Processor", "Clairv4Processor")],
                                     default=["PaclairProcessor", "LabelProcessor", "LanguagePackagesProcessor"])
    representers = SelectField("Representers", choices=[("HumanMirrored", "HumanMirrored"),("Detailed", "Detailed")], default="HumanMirrored")
