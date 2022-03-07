from Conexion import *

class Animal():

    def CreateAnimal(self, Nombre, Tipo, Edad, Genero,):
        x = mycol.insert_one({"name" : Nombre, "Tipo" : Tipo,"Edad" : Edad,"Genero" : Genero})
        return x

    def LeerAnimal(self, Nombre):
        for x in mycol.find({"name": Nombre}):
            print(x)

    def LeerAnimales(self):
        for x in mycol.find():
            print(x)

    def EliminarAnimal(self, Nombre):
        mycol.delete_one({ "name": Nombre })

    def ModificarAnimal(self, oldName, newName):
        myquery = { "name": oldName }
        newvalues = { "$set": { "name": newName } }

        mycol.update_one(myquery, newvalues)

        for x in mycol.find():
            print(x)
