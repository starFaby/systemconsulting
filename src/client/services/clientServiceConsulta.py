from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class ClientServiceConsulta:
    
    @classmethod
    def ongetClientServiceConsulta(self, idCat):
        try:
            consultaList = Consulta.query.filter(Consulta.pfspcrconsultestado == 1).filter(Consulta.pfspcrcateid == idCat)
            return consultaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    