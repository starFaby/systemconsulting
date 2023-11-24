from flask import render_template as render, request, flash, redirect, url_for
from src.admin.services.adminServiceConsulta import AdminServiceConsulta
from src.admin.services.adminServiceCategoria import AdminServiceCategoria
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime


class AdminControllerConsulta:

    def onGetAdminControllerConsultaList(page):
        try:
            page = page
            consulta = AdminServiceConsulta.ongetAdminServiceConsulta(page)
            categorias = AdminServiceCategoria.onGetAdminServiceCategoriaAll()
            if consulta != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    consulta = AdminServiceConsulta.ongetAdminServiceConsultaName(search, page)
                    return render("admin/adminConsulta.html",categorias = categorias, consulta=consulta, tag = tag)
                else:
                    flash('Consultas Listadas', category='success')
                    return render("admin/adminConsulta.html",categorias = categorias, consulta=consulta)
            else:
                flash('No existe consultas', category='success')
                return render("admin/adminConsulta.html",categorias=categorias, consulta=consulta)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
        
    def onGetControllerAdminConsultaSave():

        pfspcrconsultseccion = request.form['txtSeccion'] 
        pfspcrconsultnum = request.form['txtNum']
        pfspcrconsultnombre = request.form['txtNombre']
        pfspcrconsultimage = request.form['txtImage']
        pfspcrconsultdetalle = request.form['txtDetalle']
        pfspcrconsulturl = request.form['txtUrl']
        pfspcrconsultestado = request.form['selectEstado']
        pfspcrconsultcreatedat = datetime.now()
        pfspcrcateid = request.form['selectCategoria']

        if pfspcrconsultseccion != '' and pfspcrconsultnum != '' and pfspcrconsultnombre != '' and pfspcrconsultimage != '' and pfspcrconsultdetalle != '' and pfspcrconsulturl != '' and pfspcrconsultestado != 'Elija...' and pfspcrconsultcreatedat != '' and pfspcrcateid != '' :
            AdminServiceConsulta.onGetAdminServiceConsultaSave(pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid)
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('racco.onGetAdminControllerConsultaList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            print("Datos vacios")
            return redirect(url_for('racco.onGetAdminControllerConsultaList'))          

    def onGetControllerAdminConsultaUpdate(id):
        consulta = AdminServiceConsulta.onGetAdminServiceConsultUpdateSelect(id)
        categorias = AdminServiceCategoria.onGetAdminServiceCategoriaAll()
        if request.method == 'POST':
            pfspcrconsultseccion = request.form['txtSeccion'] 
            pfspcrconsultnum = request.form['txtNum']
            pfspcrconsultnombre = request.form['txtNombre']
            pfspcrconsultimage = request.form['txtImage']
            pfspcrconsultdetalle = request.form['txtDetalle']
            pfspcrconsulturl = request.form['txtUrl']
            pfspcrconsultestado = request.form['selectEstado']
            pfspcrconsultcreatedat = datetime.now()
            pfspcrcateid = request.form['selectCategoria']
            if pfspcrconsultseccion != '' and pfspcrconsultnum != '' and pfspcrconsultnombre != '' and pfspcrconsultimage != '' and pfspcrconsultdetalle != '' and pfspcrconsulturl != '' and pfspcrconsultestado != 'Elija...' and pfspcrconsultcreatedat != '' and pfspcrcateid != '' :
                adServConsult = AdminServiceConsulta.onGetAdminServiceConsultUpdate(id, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid)
                if adServConsult == True:
                    flash('Datos Actualizados', category='success')
                    return redirect(url_for('racco.onGetAdminControllerConsultaList'))
                else:
                    flash('Campos vacios llene porfabor', category='success')
                    return redirect(url_for('racco.onGetAdminControllerConsultaList'))
            else:
                    flash('Campos vacios llene porfabor', category='success')
                    return redirect(url_for('racco.onGetAdminControllerConsultaList'))

        return render("modal/modalAdminConsultUpdate.html", consulta = consulta, categorias = categorias)   

    def onGetControllerAdminConsultaDelete(id):
        pfspcrconsultseccion = ''
        pfspcrconsultnum = ''
        pfspcrconsultnombre = ''
        pfspcrconsultimage = ''
        pfspcrconsultdetalle = ''
        pfspcrconsulturl = ''
        pfspcrconsultestado = 0
        pfspcrconsultcreatedat = ''
        pfspcrcateid = ''
        if pfspcrconsultseccion == '' and pfspcrconsultnum == '' and pfspcrconsultnombre == '' and pfspcrconsultimage == '' and pfspcrconsultdetalle == '' and pfspcrconsulturl == '' and pfspcrconsultestado != '' and pfspcrconsultcreatedat == '' and pfspcrcateid == '' :
            consulta = AdminServiceConsulta.onGetAdminServiceConsultaDelete(id, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid)     
            if consulta == True:
                flash('Datos Actualizados', category='success')
                return redirect(url_for('racco.onGetAdminControllerConsultaList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('racco.onGetAdminControllerConsultaList'))
        else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('racco.onGetAdminControllerConsultaList'))
            
