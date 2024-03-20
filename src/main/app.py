from flask import Flask, request
from .flask_adapter import AdaptControllerToFlask
from .factories.add_shelve_controller_factory import makeAddShelveController
from .factories.add_book_controller_factory import makeAddBookController
from .factories.internal_server_error_proxy_factory import makeInternalServerErrorProxy

app = Flask(__name__)

@app.route("/shelves", methods=["POST"])
def AddShelve():
    return AdaptControllerToFlask(makeInternalServerErrorProxy(makeAddShelveController()), request)

@app.route("/books", methods=["POST"])
def AddBook():
    return AdaptControllerToFlask(makeInternalServerErrorProxy(makeAddBookController()), request)
