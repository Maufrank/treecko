from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, TextAreaField, SubmitField, PasswordField, DateField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL, InputRequired
import requests

