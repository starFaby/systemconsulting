from flask import Blueprint
from src.admin.controller.adminControllerConsulta import AdminControllerConsulta
racco= Blueprint('racco', __name__)
racco.route('/racco', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerConsulta.onGetAdminControllerConsultaList)
racco.route('/racco/<int:page>', methods=['GET', 'POST'])(AdminControllerConsulta.onGetAdminControllerConsultaList)
racco.route('/raccos', methods=['POST'])(AdminControllerConsulta.onGetControllerAdminConsultaSave)
racco.route('/raccosup/<id>', methods=['GET', 'POST'])(AdminControllerConsulta.onGetControllerAdminConsultaUpdate)
racco.route('/raccosde/<id>', methods=['GET'])(AdminControllerConsulta.onGetControllerAdminConsultaDelete)

