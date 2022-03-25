########################################
# * FLASK APPLICATION
########################################

# extensions that allow specific extensions.
from flask import Flask, Blueprint, render_template, url_for, redirect

# a 'blueprint' of website structures
views = Blueprint(__name__, "views")

# the website is defined as a flask app and the url prefix is set to '/'
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

########################################
# * APPLICATION PAGES
########################################
# this is how the homepage is accessed
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/python")
def python_page():
    return render_template("python.html", programming_language="Python")


@app.route("/flask")
def flask_page():
    return render_template("flask.html", programming_language="Flask")


@app.route("/bootstrap")
def bootstrap_page():
    return render_template("bootstrap.html", programming_language="Bootstrap")

########################################
# exteranal links


@app.route('/python-docs')
def python_docs():
    return redirect("https://docs.python.org/3/")


@app.route('/flask-docs')
def flask_docs():
    return redirect("https://flask.palletsprojects.com/en/2.0.x/")


@app.route('/bootstrap-docs')
def bootstrap_docs():
    return redirect("https://getbootstrap.com/docs/5.1/getting-started/introduction/")

########################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

########################################

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

########################################

# debugging is activated and the project is set to hosted on port 8000
# (debugging should only be used in testing)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
########################################
