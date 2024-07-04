from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from models import storage
from models.user import User
from frontend.app import db



class RegisterForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired(), Length(max=30)])
    last_name = StringField("Last name", validators=[DataRequired(), Length(max=30)])
    email = EmailField(
        "Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    contact = StringField("Contact", validators=[DataRequired(), Length(max=15)])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    def validate(self, **kwargs):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = db.session.query(User).filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")
