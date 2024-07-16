#!/usr/bin/python3
"""
Contains form class for creating a bug report
"""


from flask_wtf import FlaskForm
from wtforms import FileField, TextAreaField, SelectField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError


def file_size_limit(max_size):
    """Sets the maximum size of a file that can be uploaded"""
    def _file_size_limit(form, field):
        if field.data and hasattr(field.data, "stream"):
            field.data.stream.seek(0, 2)
            file_size = field.data.stream.tell()
            if file_size > max_size:
                raise ValidationError(f"File size must be less than {max_size / (1024 * 1024):.2f} MB")
            field.data.stream.seek(0)
    return _file_size_limit


class BugForm(FlaskForm):
    name = StringField("Bug Name", validators=[DataRequired(), Length(max=60)])
    description = TextAreaField("Description", validators=[Length(max=1028)])
    product = StringField("Product Name", validators=[DataRequired()])
    category = SelectField(
        "Category",
        choices=[
            ("Network", "Network"),
            ("Performace", "Performance"),
            ("Sound", "Sound"),
            ("Data Integrity", "Data integrity"),
            ("Security", "Security"),
            ("Backend", "Backend"),
            ("Usability", "Usability"),
            ("Crash", "Crash")
        ],
        validators=[DataRequired()]
    )
    severity = SelectField(
        "Severity",
        choices=[
            ("Critical", "Critical"),
            ("High", "High"),
            ("Medium", "Medium"),
            ("Low", "Low")
        ],
        validators=[DataRequired()]
    )
    attachment = FileField(
        "Bug Video/Image",
        validators=[file_size_limit(2 * 1024 * 1024)]
    )

    submit = SubmitField("Report")


class UpvoteForm(FlaskForm):
    submit = SubmitField("Upvote")