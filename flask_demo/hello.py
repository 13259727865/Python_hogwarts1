import flask
from flask import jsonify

from flask_demo.flask_blueprint_demo import demo_router
from flask_demo.log_util import logger

app = flask.Flask(__name__)


@app.route("/user/<int:user>")
def hello(user):
    logger.info(f"hello {user}")
    return f"hello {user}"


@app.route("/userstr/<string:user>")
def strhello(user):
    logger.info(f"hello str{user}")
    return f"hello str {user}"


@app.route("/getuser/<int:id>", methods=["get", "post"])
def get_api(id):
    logger.info(f"hello get{id}")
    reponse = jsonify({"code": 201, "msg": id})
    reponse.set_cookie("session", "werwqeriqoeuhruie")
    reponse.status_code = "202"
    return reponse


if __name__ == '__main__':
    app.register_blueprint(demo_router)
    app.run(debug=True)

