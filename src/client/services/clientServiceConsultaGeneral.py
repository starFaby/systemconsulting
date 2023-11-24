from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class ClientServiceConsultaGeneral:
    
    @classmethod
    def ongetClientServiceConsultaGeneral(self):
        try:
            consgeneList = Consulta.query.filter(Consulta.pfspcrconsultestado == 1)
            return consgeneList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def ongetClientServiceConsultaGeneralName(self, search):
        try:
            consgeneList = Consulta.query.filter(Consulta.pfspcrconsultnombre.like(search)).filter(Consulta.pfspcrconsultestado == 1)
            return consgeneList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)