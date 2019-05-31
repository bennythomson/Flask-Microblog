from flask import Flask, render_template, request, flash, redirect, g, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "ejogowjglo23987890"
db = SQLAlchemy(app)


import blog.views
