from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.admin.model.adminModelConsulta import ModelConsulta
import datetime

class AdminServiceConsulta:
    
    @classmethod
    def ongetAdminServiceConsulta(self, page):
        try:
            page = page
            pages = 10
            consultaList = Consulta.query.order_by(Consulta.pfspcrconsultid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return consultaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def ongetAdminServiceConsultaName(self, search, page):
        try:
            page = page
            pages = 10
            ConsultaList = Consulta.query.filter(Consulta.pfspcrconsultnombre.like(search)).paginate(per_page=pages,error_out=False)
            return ConsultaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)

    @classmethod    
    def onGetAdminServiceConsultaSave(self, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid):
        try:
            modelConsulta = ModelConsulta(0,pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage,
                                        pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid)
            newConsulta = Consulta( pfspcrconsultseccion = modelConsulta.getpfspcrconsultseccion(), 
                                    pfspcrconsultnum = modelConsulta.getpfspcrconsultnum(), 
                                    pfspcrconsultnombre = modelConsulta.getpfspcrconsultnombre(), 
                                    pfspcrconsultimage = modelConsulta.getpfspcrconsultimage(), 
                                    pfspcrconsultdetalle = modelConsulta.getpfspcrconsultdetalle(), 
                                    pfspcrconsulturl = modelConsulta.getpfspcrconsulturl(), 
                                    pfspcrconsultestado = modelConsulta.getpfspcrconsultestado(), 
                                    pfspcrconsultcreatedat = modelConsulta.getpfspcrconsultcreatedat(),
                                    pfspcrcateid = modelConsulta.getpfspcrcateid())
            db.session.add(newConsulta)
            db.session.commit()

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceConsultUpdateSelect(self, id):
        try:
            consulta = Consulta.query.get(id)
            return consulta
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceConsultUpdate(self, id, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid):
        try:
            consulta = Consulta.query.get(id)
            modelConsulta =  ModelConsulta(0, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage,
                                            pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat,
                                            pfspcrcateid)
            consulta.pfspcrconsultseccion = modelConsulta.getpfspcrconsultseccion()
            consulta.pfspcrconsultnum = modelConsulta.getpfspcrconsultnum()
            consulta.pfspcrconsultnombre = modelConsulta.getpfspcrconsultnombre()
            consulta.pfspcrconsultimage = modelConsulta.getpfspcrconsultimage()
            consulta.pfspcrconsultdetalle = modelConsulta.getpfspcrconsultdetalle()
            consulta.pfspcrconsulturl = modelConsulta.getpfspcrconsulturl()
            consulta.pfspcrconsultestado = modelConsulta.getpfspcrconsultestado()
            consulta.pfspcrcateid = modelConsulta.getpfspcrcateid()
            db.session.commit()

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceConsultaDelete(self, id , pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid):
        
        consulta = Consulta.query.get(id)
        if consulta.pfspcrconsultid >= 1:
            modelConsulta = ModelConsulta(id, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid)
            consulta.pfspcrconsultestado = modelConsulta.getpfspcrconsultestado()
            db.session.commit()
            return True
        else:
            return False

        
