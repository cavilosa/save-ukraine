from flask import Flask, request, abort, make_response, flash, jsonify,\
make_response, redirect, request, url_for
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# cache = Cache(app)
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# app = Flask(__name__)
# cache.init_app(app)

@app.route("/", methods = ["GET"])
@cache.cached(timeout=10)
def index():
    return ("success: True")


if __name__ == "__main__":
    app.run()

