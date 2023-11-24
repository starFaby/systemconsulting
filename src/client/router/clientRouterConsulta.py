from flask import Blueprint
from src.client.controller.clientControllerConsulta import ClientControllerConsulta
crc= Blueprint('crc', __name__)
crc.route('/crc/<idCat>', methods=['GET'])(ClientControllerConsulta.onGetClientControllerConsultaList)
#caso.route('/newcs', methods=['POST'])(ControllerClientProducto.onGetcontrollerCasoInsert) 