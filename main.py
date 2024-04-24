import os, sys, pathlib
PROJECT_DIR = os.path.join(pathlib.Path(__file__).parent)
sys.path.append(os.path.join(PROJECT_DIR, "config.py"))
sys.path.append(os.path.join(PROJECT_DIR, "models"))
sys.path.append(os.path.join(PROJECT_DIR, "projects.py"))
sys.path.append(os.path.join(PROJECT_DIR, "schoology.py"))
from schoology import group
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "https://computer-science-club.moncheeto.repl.co"

@app.route("/")
def index():
	return render_template("home.html", group=group)

@app.route("/updates")
def updates():
	return render_template("updates.html", group=group)

@app.route("/discussions")
def discussions():
	return render_template("discussions.html", group=group)

@app.route("/projects", methods = ["GET", "POST"])
def projects():
	return render_template("projects.html", group=group)

@app.route("/members")
def members():
	return render_template("members.html", group=group)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)
