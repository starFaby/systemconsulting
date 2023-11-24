from flask import render_template as render, request, flash
from src.admin.services.adminServiceUsers import AdminServiceUser
from sqlalchemy.exc import SQLAlchemyError


class AdminControllerUser:

    def onGetAdminControllerUserList(page):
        try:
            page = page
            users = AdminServiceUser.ongetAdminServiceUser(page)
            if users != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    users = AdminServiceUser.ongetAdminServiceUserName(search, page)
                    return render("admin/adminUsers.html", users=users, tag = tag)
                else:
                    flash('Usuarios Listadas', category='success')
                    return render("admin/adminUsers.html", users=users)
            else:
                flash('No existe Usuarios', category='success')
                return render("admin/adminUsers.html", users=users)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')