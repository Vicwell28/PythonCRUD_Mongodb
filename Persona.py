from Conexion import *

class Persona():

    def CreatePersona(self, Nombre, Tipo, Edad, Genero,):
        x = mycol.insert_one({"name" : Nombre, "Tipo" : Tipo,"Edad" : Edad,"Genero" : Genero})
        return x

    def LeerPersona(self, Nombre):
        for x in mycol.find({"name": Nombre}):
            print(x)

    def LeerPersonaes(self):
        for x in mycol.find():
            print(x)

    def EliminarPersona(self, Nombre):
        mycol.delete_one({ "name": Nombre })

    def ModificarPersona(self, oldName, newName):
        myquery = { "name": oldName }
        newvalues = { "$set": { "name": newName } }

        mycol.update_one(myquery, newvalues)

        for x in mycol.find():
            print(x)
