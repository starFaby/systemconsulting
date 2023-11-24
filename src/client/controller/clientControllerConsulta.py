from flask import render_template as render, request, flash, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from src.client.services.clientServiceConsulta import ClientServiceConsulta

class ClientControllerConsulta:

    def onGetClientControllerConsultaList(idCat):
        try:
            consulta = ClientServiceConsulta.ongetClientServiceConsulta(idCat)
            if consulta != []:
                flash('Consultas Listadas', category='success')
                return render("client/ClientConsultaView.html", consulta=consulta)
            else:
                flash('No existe Consultas', category='success')
                return render("client/ClientConsultaView.html", consulta=consulta)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)