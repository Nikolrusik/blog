from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("username", [validators.DataRequired()],)
    email = StringField(
        "Email address",
        [
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6, max=200),
        ],
        filters=[lambda data: data and data.lower()],
    )


class RegistrationForm(UserBaseForm):
    password = PasswordField(
        "New password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm", message="Password must match")
        ],
    )
    confirm = PasswordField("Repeat password")
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()])
    password = StringField("password", [validators.DataRequired()])
    submit = SubmitField('Login')
