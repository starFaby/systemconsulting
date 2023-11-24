from flask import Blueprint
from src.client.controller.clientControllerConsultaGeneral import ClientControllerConsultaGeneral
crcg= Blueprint('crcg', __name__)
crcg.route('/crcg', methods=['GET', 'POST'])(ClientControllerConsultaGeneral.onGetClientControllerConsultaGeneralList)