import os
from dotenv import load_dotenv
from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog import commands
from blog.views.auth import auth_app, login_manager

app = Flask(__name__)
load_dotenv()

# Configs
cfg_name = os.environ.get("CONFIG_NAME")
app.config.from_object(f"blog.config.{cfg_name}")
login_manager.init_app(app)


# Database
db.init_app(app)
app.cli.add_command(commands.init_db)
app.cli.add_command(commands.create_users)

# Blueprints
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")


# Views
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet/<name>/")
def greet_name(name: str):
    return f"Hello, {name}"
