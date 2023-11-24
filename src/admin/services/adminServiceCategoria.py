from flask import render_template as render, request
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError
from src.admin.model.adminModelCategoria import ModelCategoria
import datetime

class AdminServiceCategoria:

    @classmethod
    def onGetAdminServiceCategoriaAll(self):
        try:
            categoriaList = Categoria.query.all()
            return categoriaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    @classmethod
    def ongetAdminServiceCategoria(self, page):
        try:
            page = page
            pages = 10
            categoriaList = Categoria.query.order_by(Categoria.pfspcrcateid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return categoriaList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def ongetAdminServiceCategoriaName(self, search, page):
        try:
            page = page
            pages = 10
            categoriaList = Categoria.query.filter(Categoria.pfspcrcatenombre.like(search)).paginate(per_page=pages,error_out=False)
            return categoriaList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')

    @classmethod    
    def onGetAdminServiceCategoriaSave(self, pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat):
        try:
            modelCategoria = ModelCategoria(0,pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat)
            newCategoria = Categoria(pfspcrcatenombre = modelCategoria.getpfspcrcatenombre(), pfspcrcateimage=modelCategoria.getpfspcrcateimage(), pfspcrcatedetalle = modelCategoria.getpfspcrcatedetalle(), pfspcrcateestado = modelCategoria.getpfspcrcateestado(), pfspcrcatecreatedat = modelCategoria.getpfspcrcatecreatedat())
            db.session.add(newCategoria)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceCategoriaUpdateSelect(self, id):
        try:
            categoria = Categoria.query.get(id)
            return categoria
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceCategoriaUpdate(self, id, pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat):
        try:
            categoria = Categoria.query.get(id)
            modelCategoria =  ModelCategoria(0, pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat)
            categoria.pfspcrcatenombre = modelCategoria.getpfspcrcatenombre()
            categoria.pfspcrcateimage = modelCategoria.getpfspcrcateimage()
            categoria.pfspcrcatedetalle = modelCategoria.getpfspcrcatedetalle()
            categoria.pfspcrcateestado = modelCategoria.getpfspcrcateestado()
            if categoria.pfspcrcatenombre != '' and categoria.pfspcrcateimage != '' and categoria.pfspcrcatedetalle != '' and categoria.pfspcrcateestado != 'Elija...':
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceCategoriaDelete(self, id , pfspcrcateestado):
        pfspcrcatenombre = ''
        pfspcrcateimage = ''
        pfspcrcatedetalle = ''
        pfspcrcatecreatedat = ''
        categoria = Categoria.query.get(id)
        if categoria.pfspcrcateid >= 1: 
            modelCategoria = ModelCategoria(id, pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat)
            categoria.pfspcrcateestado = modelCategoria.getpfspcrcateestado()
            db.session.commit()
            return True
        else:
            return False

        
