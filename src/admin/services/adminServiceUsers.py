from flask import render_template as render
from src.database.database import *
from sqlalchemy.exc import SQLAlchemyError

class AdminServiceUser:
    
    @classmethod
    def ongetAdminServiceUser(self, page):
        try:
            page = page
            pages = 10
            userList = User.query.order_by(User.pfsusersid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            return userList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def ongetAdminServiceUserName(self, search, page):
        try:
            page = page
            pages = 10
            userList = User.query.filter(User.pfsusersnombres.like(search)).paginate(per_page=pages,error_out=False)
            return userList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        