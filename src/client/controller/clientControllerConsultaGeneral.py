from flask import render_template as render, request, flash, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from src.client.services.clientServiceConsultaGeneral import ClientServiceConsultaGeneral

class ClientControllerConsultaGeneral:

    def onGetClientControllerConsultaGeneralList():
        try:
            consgeneList = ClientServiceConsultaGeneral.ongetClientServiceConsultaGeneral()
            if consgeneList != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    consgeneList = ClientServiceConsultaGeneral.ongetClientServiceConsultaGeneralName(search)
                    return render("client/ClientConsultaGeneralView.html", consgeneList=consgeneList, tag = tag)
                else:
                    flash('Categorias Listadas', category='success')
                    return render("client/ClientConsultaGeneralView.html", consgeneList=consgeneList)
            else:
                flash('No existe categorias', category='success')
                return render("client/ClientConsultaGeneralView.html", consgeneList=consgeneList)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)