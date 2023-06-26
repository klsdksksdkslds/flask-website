from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("basic-page.html", title="Index page", header="Hello, World")


@app.route("/about/")
def about() -> str:
    return render_template(
        "basic-page.html",
        title="About",
        header="About this site",
        text="this site written in python with framework flask"
    )

