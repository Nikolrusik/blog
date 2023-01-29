from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog import commands

app = Flask(__name__)


# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.cli.add_command(commands.init_db)
app.cli.add_command(commands.create_users)

# Blueprints
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")


# Views
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet/<name>/")
def greet_name(name: str):
    return f"Hello, {name}"
