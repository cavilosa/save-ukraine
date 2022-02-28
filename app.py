from flask import Flask, request, abort, make_response, flash, jsonify,\
make_response, redirect, request, url_for, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/", methods = ["GET"])
@cache.cached(timeout=10)
def index():

    return render_template("layouts/main.html", main = True)


@app.route("/about", methods = ["GET"])
@cache.cached(timeout=10)
def about():

    return render_template("pages/about.html")


@app.route("/donations", methods = ["GET"])
@cache.cached(timeout=10)
def donations():

    return render_template("pages/donations.html")


@app.route("/contacts", methods = ["GET"])
@cache.cached(timeout=10)
def contacts():

    return render_template("pages/contacts.html")


@app.route("/news", methods = ["GET"])
@cache.cached(timeout=10)
def news():

    return render_template("pages/news.html")



if __name__ == "__main__":
    app.run()

