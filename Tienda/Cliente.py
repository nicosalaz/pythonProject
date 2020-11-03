class Cliente:
    def __init__(self,name,contact,document):
        self.name = name
        self.contact = contact
        self.document = document

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    def getContact(self):
        return self.contact
    def setContact(self,newContact):
        self.contact = newContact
    def getDocument(self):
        return self.document
    def setDocument(self,newDocument):
        self.document = newDocument
    def __str__(self):
        msj = 'Nombre:'+self.name+'- Contacto:'+self.contact