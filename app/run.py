from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/contactform")
def contactform():
    return render_template("contactform.html")


if __name__ == "__main__":
    app.run(debug=True)
