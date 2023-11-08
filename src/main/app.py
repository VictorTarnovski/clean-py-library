from flask import Flask, request
from .flask_adapter import AdaptControllerToFlask
from .factories.add_shelve_controller_factory import makeAddShelveController

app = Flask(__name__)

#! Shelve Routes


@app.route("/shelves", methods=["POST"])
def AddShelve():
    return AdaptControllerToFlask(makeAddShelveController(), request)
