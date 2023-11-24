from flask import Blueprint
from src.client.controller.clientControllerCategoria import ClientControllerCategoria
rccat= Blueprint('rccat', __name__)
rccat.route('/rccat', methods=['GET', 'POST'])(ClientControllerCategoria.onGetClientControllerCategoriaList)