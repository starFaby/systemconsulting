from flask import Blueprint
from src.admin.controller.adminControllerCategoria import AdminControllerCategoria
racc= Blueprint('racc', __name__)
racc.route('/racc', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerCategoria.onGetAdminControllerCategoriaList)
racc.route('/racc/<int:page>', methods=['GET', 'POST'])(AdminControllerCategoria.onGetAdminControllerCategoriaList)
racc.route('/raccs', methods=['POST'])(AdminControllerCategoria.onGetControllerAdminCategoriaSave)
racc.route('/updracc/<id>', methods=['GET', 'POST'])(AdminControllerCategoria.onGetControllerAdminCategoriaUpdate)
racc.route('/delracc/<id>', methods=['GET'])(AdminControllerCategoria.onGetControllerAdminCategoriaDelete)

