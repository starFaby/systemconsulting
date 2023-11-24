from flask import render_template as render, request, flash, redirect, url_for
from src.admin.services.adminServiceCategoria import AdminServiceCategoria
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from src.admin.model.adminModelCategoria import ModelCategoria


class AdminControllerCategoria:

    def onGetAdminControllerCategoriaList(page):
        try:
            page = page
            categorias = AdminServiceCategoria.ongetAdminServiceCategoria(page)
            if categorias != []:
                if request.method == 'POST' and 'tag' in request.form:
                    tag = request.form["tag"]
                    search = "%{}%".format(tag)
                    categorias = AdminServiceCategoria.ongetAdminServiceCategoriaName(search, page)
                    return render("admin/adminCategoria.html", categorias=categorias, tag = tag)
                else:
                    flash('Categorias Listadas', category='success')
                    return render("admin/adminCategoria.html", categorias=categorias)
            else:
                flash('No existe categorias', category='success')
                return render("admin/adminCategoria.html", categorias=categorias)
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
        
    def onGetControllerAdminCategoriaSave():

        pfspcrcatenombre = request.form['txtNombre']
        pfspcrcateimage = request.form['txtImage']
        pfspcrcatedetalle = request.form['txtDetalle']
        pfspcrcateestado = request.form['selectEstado']
        pfspcrcatecreatedat = datetime.now()

        if pfspcrcatenombre != '' and pfspcrcateimage != '' and pfspcrcatedetalle != '' and pfspcrcateestado != 'Elija...' and pfspcrcatecreatedat != '':
            AdminServiceCategoria.onGetAdminServiceCategoriaSave(pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat)
            flash('Guardado Correctamente', category='success')
            return redirect(url_for('racc.onGetAdminControllerCategoriaList'))
        else:
            flash('LLene los campos completos porfabor', category='success')
            return redirect(url_for('racc.onGetAdminControllerCategoriaList'))          

    def onGetControllerAdminCategoriaUpdate(id):
        categoria = AdminServiceCategoria.onGetAdminServiceCategoriaUpdateSelect(id)
        if request.method == 'POST':
            pfspcrcatenombre = request.form['txtNombre']
            pfspcrcateimage = request.form['txtImage']
            pfspcrcatedetalle = request.form['txtDetalle']
            pfspcrcateestado = request.form['selectEstado']
            pfspcrcatecreatedat = datetime.now()
            if pfspcrcatenombre != '' and pfspcrcateimage != '' and pfspcrcatedetalle != '' and pfspcrcateestado != 'Elija...':
                adServCat = AdminServiceCategoria.onGetAdminServiceCategoriaUpdate(id, pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat)
                if adServCat == True:
                    flash('Datos Actualizados', category='success')
                    return redirect(url_for('racc.onGetAdminControllerCategoriaList'))
                else:
                    flash('Campos vacios llene porfabor', category='success')
                    return redirect(url_for('racc.onGetAdminControllerCategoriaList'))
            else:
                    flash('Campos vacios llene porfabor', category='success')
                    return redirect(url_for('racc.onGetAdminControllerCategoriaList'))

        return render("modal/modalAdminCateUpdate.html", categoria = categoria)   

    def onGetControllerAdminCategoriaDelete(id):
        pfspcrcateestado = 0
        if pfspcrcateestado != '':
            categoria = AdminServiceCategoria.onGetAdminServiceCategoriaDelete(id, pfspcrcateestado)     
            if categoria == True:
                flash('Datos Actualizados', category='success')
                return redirect(url_for('racc.onGetAdminControllerCategoriaList'))
            else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('racc.onGetAdminControllerCategoriaList'))
        else:
                flash('Campos vacios llene porfabor', category='success')
                return redirect(url_for('racc.onGetAdminControllerCategoriaList'))
            
