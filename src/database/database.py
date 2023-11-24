from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#---------------------------
#drop database flaskmysql
#create database flaskmysql
#---------------------------

#----------------------------
#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='pfsusers'

    pfsusersid = db.Column(db.Integer, primary_key=True)
    pfsuserscedula = db.Column(db.String(80), nullable=False)
    pfsusersnombres = db.Column(db.String(80), nullable=False)
    pfsusersapellidos = db.Column(db.String(80), nullable=False)
    pfsusersusername = db.Column(db.String(30), nullable=False)
    pfsusersemail = db.Column(db.String(120), nullable=False)
    pfsuserspassword = db.Column(db.String(250), nullable=True)
    pfsusersdireccion = db.Column(db.String(100), nullable=True)
    pfsuserscellphone = db.Column(db.String(25), nullable=False)
    pfsusersphone = db.Column(db.String(20), nullable=False)
    pfsusersisadmin = db.Column(db.Boolean, default=False)
    pfsusersavatar = db.Column(db.String(250), nullable=True)
    pfsusersestado = db.Column(db.String(1), nullable=True)
    pfsuserscreatedat = db.Column(db.Date, nullable=True) 

    def onGetSetPassword(self, pfsuserspassword):
        self.pfsuserspassword = generate_password_hash(pfsuserspassword)

    def onGetCheckPassword(self, pfsuserspassword):
        return check_password_hash(self.pfsuserspassword, pfsuserspassword)

    def __init__(self, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion,  pfsuserscellphone, pfsusersphone, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat):
        self.pfsuserscedula = pfsuserscedula
        self.pfsusersnombres = pfsusersnombres
        self.pfsusersapellidos = pfsusersapellidos
        self.pfsusersusername = pfsusersusername
        self.pfsusersemail = pfsusersemail
        self.pfsuserspassword = pfsuserspassword 
        self.pfsusersdireccion = pfsusersdireccion 
        self.pfsuserscellphone = pfsuserscellphone
        self.pfsusersphone = pfsusersphone
        self.pfsusersisadmin = pfsusersisadmin
        self.pfsusersavatar = pfsusersavatar
        self.pfsusersestado = pfsusersestado
        self.pfsuserscreatedat = pfsuserscreatedat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsusersid', 'pfsuserscedula', 'pfsusersnombres', 'pfsusersapellidos', 'pfsusersusername', 'pfsusersemail', 'pfsuserspassword', 'pfsusersdireccion',  'pfsuserscellphone', 'pfsusersphone', 'pfsusersisadmin', 'pfsusersavatar', 'pfsusersestado', 'pfsuserscreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

#-----------------------------------------------------------
#---------------CATEGORIA----------------------------------
#----------------------------------------------------------

class Categoria(db.Model):
    __tablename__='pfspcrcategorias'

    pfspcrcateid = db.Column(db.Integer, primary_key=True)
    pfspcrcatenombre = db.Column(db.String(120), nullable=False)
    pfspcrcateimage = db.Column(db.String(300), nullable=False)
    pfspcrcatedetalle = db.Column(db.String(300), nullable=False)
    pfspcrcateestado = db.Column(db.String(1), nullable=True)
    pfspcrcatecreatedat = db.Column(db.String(11), nullable=True) 


    def __init__(self, pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle , pfspcrcateestado, pfspcrcatecreatedat):
        self.pfspcrcatenombre = pfspcrcatenombre
        self.pfspcrcateimage = pfspcrcateimage
        self.pfspcrcatedetalle = pfspcrcatedetalle
        self.pfspcrcateestado = pfspcrcateestado
        self.pfspcrcatecreatedat = pfspcrcatecreatedat

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('pfspcrcateid','pfspcrcatenombre', 'pfspcrcateimage', 'pfspcrcatedetalle', 'pfspcrcateestado', 'pfspcrcatecreatedat')

categoriaSchema = CategoriaSchema()
categoriaSchema = CategoriaSchema(many=True)

#----------------------------
#----------CONSULTA----------
#--------------------------
class Consulta(db.Model):
    __tablename__='pfspcrconsulta'

    pfspcrconsultid = db.Column(db.Integer, primary_key=True)
    pfspcrconsultseccion = db.Column(db.String(30), nullable=False)
    pfspcrconsultnum = db.Column(db.String(20), nullable=False)
    pfspcrconsultnombre = db.Column(db.String(80), nullable=False)
    pfspcrconsultimage = db.Column(db.String(300), nullable=False)
    pfspcrconsultdetalle = db.Column(db.String(300), nullable=False)
    pfspcrconsulturl = db.Column(db.String(300), nullable=False) #int
    pfspcrconsultestado = db.Column(db.String(1), nullable=True)
    pfspcrconsultcreatedat = db.Column(db.String(11), nullable=True) 

    pfspcrcateid = db.Column(db.Integer, db.ForeignKey('pfspcrcategorias.pfspcrcateid',ondelete='CASCADE'), nullable=False)
    pfspcrcategoria = db.relationship('Categoria',backref=db.backref('pfspcrconsulta',lazy=True))


    def __init__(self, pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid):
        self.pfspcrconsultseccion = pfspcrconsultseccion
        self.pfspcrconsultnum = pfspcrconsultnum
        self.pfspcrconsultnombre = pfspcrconsultnombre
        self.pfspcrconsultimage = pfspcrconsultimage
        self.pfspcrconsultdetalle = pfspcrconsultdetalle
        self.pfspcrconsulturl = pfspcrconsulturl
        self.pfspcrconsultestado = pfspcrconsultestado
        self.pfspcrconsultcreatedat = pfspcrconsultcreatedat
        self.pfspcrcateid = pfspcrcateid
class ConsultaSchema(ma.Schema):
    class Meta:
        fields = ('pfspcrconsultid', 'pfspcrconsultseccion', 'pfspcrconsultnum', 'pfspcrconsultnombre', 'pfspcrconsultimage', 'pfspcrconsultdetalle', 'pfspcrconsulturl', 'pfspcrconsultestado', 'pfspcrconsultcreatedat', 'pfspcrcateid')

consultaSchema = ConsultaSchema()
consultaSchema = ConsultaSchema(many=True)

#----------------------------
#----------visita----------
#--------------------------

class Visita(db.Model):
    __tablename__='pfspcrvisita'

    pfspcrvisitid = db.Column(db.Integer, primary_key=True)
    pfspcrvisitnum = db.Column(db.String(120), nullable=False)
    pfspcrvisitestado = db.Column(db.String(1), nullable=True)
    pfspcrvisitcreatedat = db.Column(db.String(11), nullable=True) 


    pfsuserid = db.Column(db.Integer, db.ForeignKey('pfsusers.pfsusersid',ondelete='CASCADE'), nullable=False)
    pfsuser = db.relationship('User',backref=db.backref('pfspcrvisita',lazy=True))

    pfspcrconsultid = db.Column(db.Integer, db.ForeignKey('pfspcrconsulta.pfspcrconsultid',ondelete='CASCADE'), nullable=False)
    pfspcrconsult = db.relationship('Consulta',backref=db.backref('pfspcrvisita',lazy=True))


    def __init__(self, pfspcrvisitnum, pfspcrvisitestado, pfspcrvisitcreatedat , pfsuserid, pfspcrconsultid):
        self.pfspcrvisitnum = pfspcrvisitnum
        self.pfspcrvisitestado = pfspcrvisitestado
        self.pfspcrvisitcreatedat = pfspcrvisitcreatedat
        self.pfsuserid = pfsuserid
        self.pfspcrconsultid = pfspcrconsultid

class VisitaSchema(ma.Schema):
    class Meta:
        fields = ('pfspcrvisitid', 'pfspcrvisitnum', 'pfspcrvisitestado', 'pfspcrvisitcreatedat' , 'pfsuserid', 'pfspcrconsultid')

visitaSchema = VisitaSchema()
visitaSchema = VisitaSchema(many=True)
