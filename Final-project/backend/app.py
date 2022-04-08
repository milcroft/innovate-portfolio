import sys

from flask import Flask, Blueprint, render_template, url_for, redirect
from flask_flatpages import FlatPages
from flask_frozen import Freezer

# a 'blueprint' of website structures
views = Blueprint(__name__, "views")

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('index.html', pages=pages)


@app.route('/<path:path>.html')
def page(path):
    print("View function activated!")
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@freezer.register_generator
def pagelist():
    for page in pages:
        yield url_for('page', path=page.path)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', pages=pages)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=5001)
