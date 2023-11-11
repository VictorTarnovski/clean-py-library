from flask import Flask, request
from .flask_adapter import AdaptControllerToFlask
from .factories.add_shelve_controller_factory import makeAddShelveController
from .factories.add_book_controller_factory import makeAddBookController

app = Flask(__name__)


@app.route("/shelves", methods=["POST"])
def AddShelve():
    return AdaptControllerToFlask(makeAddShelveController(), request)

@app.route("/books", methods=["POST"])
def AddBook():
    return AdaptControllerToFlask(makeAddBookController(), request)