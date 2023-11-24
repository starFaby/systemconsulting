class ModelCategoria():
    def __init__(self, pfspcrcateid, pfspcrcatenombre, pfspcrcateimage, pfspcrcatedetalle, pfspcrcateestado, pfspcrcatecreatedat) -> None:

        self.pfspcrcateid = pfspcrcateid
        self.pfspcrcatenombre = pfspcrcatenombre
        self.pfspcrcateimage = pfspcrcateimage
        self.pfspcrcatedetalle = pfspcrcatedetalle
        self.pfspcrcateestado = pfspcrcateestado
        self.pfspcrcatecreatedat = pfspcrcatecreatedat

    # get y set id
    def getpfspcrcateid(self):
        return self.pfspcrcateid
    
    def setpfspcrcateid(self, pfspcrcateid):
        self.pfspcrcateid = pfspcrcateid

    # get y set pfspcrcatenombre
    def getpfspcrcatenombre(self):
        return self.pfspcrcatenombre
    
    def setpfspcrcatenombre(self, pfspcrcatenombre):
        self.pfspcrcatenombre = pfspcrcatenombre

    # get y set pfspcrcateimage
    def getpfspcrcateimage(self):
        return self.pfspcrcateimage
    
    def setpfspcrcateimage(self, pfspcrcateimage):
        self.pfspcrcateimage = pfspcrcateimage

    # get y set pfspcrcatedetalle
    def getpfspcrcatedetalle(self):
        return self.pfspcrcatedetalle
    
    def setpfspcrcatedetalle(self, pfspcrcatedetalle):
        self.pfspcrcatedetalle = pfspcrcatedetalle

    # get y set pfspcrcateestado
    def getpfspcrcateestado(self):
        return self.pfspcrcateestado
    
    def setpfspcrcateestado(self, pfspcrcateestado):
        self.pfspcrcateestado = pfspcrcateestado

    
    # get y set pfspcrcatecreatedat
    def getpfspcrcatecreatedat(self):
        return self.pfspcrcatecreatedat
    
    def setpfspcrcatecreatedat(self, pfspcrcatecreatedat):
        self.pfspcrcatecreatedat = pfspcrcatecreatedat



    def LoginInJason(self):
        return {
            'pfspcrcateid' : self.pfspcrcateid,
            'pfspcrcatenombre' : self.pfspcrcatenombre,
            'pfspcrcateimage' : self.pfspcrcateimage,
            'pfspcrcatedetalle' : self.pfspcrcatedetalle,
            'pfspcrcateestado' : self.pfspcrcateestado,
            'pfspcrcatecreatedat' : self.pfspcrcatecreatedat,
            }