from flask import Flask, request, abort, make_response, flash, jsonify,\
make_response, redirect, request, url_for, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/", methods = ["GET"])
@cache.cached(timeout=10)
def index():


    return render_template("layouts/main.html")


if __name__ == "__main__":
    app.run()

