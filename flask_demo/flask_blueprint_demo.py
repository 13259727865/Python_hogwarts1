from flask import jsonify, Blueprint, render_template

from flask_demo.log_util import logger

demo_router = Blueprint(name="BPdemo",import_name=__name__,url_prefix="/app_demo")

@demo_router.route("/list/<int:id>")
def get_api(id):
    logger.info(f"hello get{id}")
    reponse = jsonify({"code": 201, "msg": id})
    reponse.set_cookie("session", "werwqeriqoeuhruie")
    reponse.status_code = "202"
    return reponse

@demo_router.route("get_static")
def get_static():
    return render_template("static.html")