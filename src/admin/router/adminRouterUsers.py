from flask import Blueprint
from src.admin.controller.adminControllerUser import AdminControllerUser
# admin - categoria - caso
aru= Blueprint('aru', __name__)
aru.route('/aru', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerUser.onGetAdminControllerUserList)
aru.route('/aru/<int:page>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserList)

