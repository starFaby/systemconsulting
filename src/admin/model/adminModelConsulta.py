class ModelConsulta():
    def __init__(self, pfspcrconsultid,  pfspcrconsultseccion, pfspcrconsultnum, pfspcrconsultnombre, pfspcrconsultimage, pfspcrconsultdetalle, pfspcrconsulturl, pfspcrconsultestado, pfspcrconsultcreatedat, pfspcrcateid):

        self.pfspcrconsultid = pfspcrconsultid
        self.pfspcrconsultseccion = pfspcrconsultseccion
        self.pfspcrconsultnum = pfspcrconsultnum
        self.pfspcrconsultnombre = pfspcrconsultnombre
        self.pfspcrconsultimage = pfspcrconsultimage
        self.pfspcrconsultdetalle = pfspcrconsultdetalle
        self.pfspcrconsulturl = pfspcrconsulturl
        self.pfspcrconsultestado = pfspcrconsultestado
        self.pfspcrconsultcreatedat = pfspcrconsultcreatedat
        self.pfspcrcateid = pfspcrcateid

    # get y set pfspcrconsultid
    def getpfspcrconsultid(self):
        return self.pfspcrconsultid
    
    def setpfspcrconsultid(self, pfspcrconsultid):
        self.pfspcrconsultid = pfspcrconsultid


    # get y set pfspcrconsultseccion
    def getpfspcrconsultseccion(self):
        return self.pfspcrconsultseccion
    
    def setpfspcrconsultseccion(self, pfspcrconsultseccion):
        pfspcrconsultseccion = pfspcrconsultseccion
    
    # get y set pfspcrconsultnum
    def getpfspcrconsultnum(self):
        return self.pfspcrconsultnum
    
    def setpfspcrconsultnum(self, pfspcrconsultnum):
        self.pfspcrconsultnum = pfspcrconsultnum
    
    #get y set pfspcrconsultnombre
    def getpfspcrconsultnombre(self):
        return self.pfspcrconsultnombre
    
    def setpfspcrconsultnombre(self, pfspcrconsultnombre):
        self.pfspcrconsultnombre = pfspcrconsultnombre

    #get y set pfspcrconsultimage
    def getpfspcrconsultimage(self):
        return self.pfspcrconsultimage
    
    def setpfspcrconsultimage(self, pfspcrconsultimage):
        self.pfspcrconsultimage = pfspcrconsultimage

    # get y set  pfspcrconsultdetalle
    def getpfspcrconsultdetalle(self):
        return self.pfspcrconsultdetalle
    
    def setpfspcrconsultdetalle(self, pfspcrconsultdetalle):
        self.pfspcrconsultdetalle = pfspcrconsultdetalle



    #get y set pfspcrconsulturl
    def getpfspcrconsulturl(self):
        return self.pfspcrconsulturl 
    
    def setpfspcrconsulturl(self):
        return self.pfspcrconsulturl
    
    #get y set pfspcrconsulturl
    def getpfspcrconsulturl(self):
        return self.pfspcrconsulturl
    
    def setpfspcrconsulturl(self, pfspcrconsulturl):
        self.pfspcrconsulturl = pfspcrconsulturl

    #get y set pfspcrconsultestado
    def getpfspcrconsultestado(self):
        return self.pfspcrconsultestado
    
    def setpfspcrconsultestado(self, pfspcrconsultestado):
        self.pfspcrconsultestado = pfspcrconsultestado

    #get y set pfspcrconsultcreatedat
    def getpfspcrconsultcreatedat(self):
        return self.pfspcrconsultcreatedat
    
    def setpfspcrconsultcreatedat(self, pfspcrconsultcreatedat):
        self.pfspcrconsultcreatedat = pfspcrconsultcreatedat

    # get y set pfspcrcateid
    def getpfspcrcateid(self):
        return self.pfspcrcateid
    
    def setpfspcrcateid(self , pfspcrcateid):
        self.pfspcrcateid = pfspcrcateid

    def LoginInJason(self):

        return {
            'pfspcrconsultid' : self.pfspcrconsultid,
            'pfspcrconsultseccion' : self.pfspcrconsultseccion,
            'pfspcrconsultnum' : self.pfspcrconsultnum,
            'pfspcrconsultnombre' : self.pfspcrconsultnombre,
            'pfspcrconsultimage' : self.pfspcrconsultimage,
            'pfspcrconsultdetalle' : self.pfspcrconsultdetalle,
            'pfspcrconsulturl' : self.pfspcrconsulturl,
            'pfspcrconsultestado' : self.pfspcrconsultestado,
            'pfspcrconsultcreatedat' : self.pfspcrconsultcreatedat,
            'pfspcrcateid' : self.pfspcrcateid
            }
    
        