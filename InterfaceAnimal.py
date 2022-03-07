import os
from Animal import * 
class MenuAnimal():

    def __init__(self):
        self.Animal = Animal()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        a = 10;
        while a != 0:
            self.cls()
            print("¿Que Quieres Hacer\nC) Insertar Animal \nR) Mostrar Animales\nU) Actualizar Animal\nD) Eliminar Animal\n0) Salir")

            op = input("Respuesta: ")

            if op.upper() == "C": 
                self.menuCreate()
            elif op.upper() == "R":
                a = 10;
                while a != 0:
                    self.cls()
                    print("Opcion Mostrar Animales\n1) Mostar Por Id\n2) Mostrar Todos Los Animales\b0) Salir")
                    R = input("Respuesta: ")
                    if R.upper() == "1":
                        self.menuFind()
                    elif R.upper() == "2":
                        
                        self.menuAll()
                    elif R == "0":
                        break
                    else:
                        input("Respuesta Incorrecta... Velve A Intentar")
            elif op.upper() == "U":
                
                self.menuModificar()
            elif op.upper() == "D": 
                
                self.menuEliminar()
            elif op == "0": 
                self.cls()
                break
            else: 
                self.cls()
                input("Opcion Invalidad... Preciona Tecla Para Volver")
        

    def menuCreate(self):
        name = input("Nombre: ")
        type = input("Tipo: ") 
        age = input("Edad: ")
        gender = input("Genero: ")
        self.Animal.CreateAnimal(name, type, age, gender)

    def menuFind(self):
        name = input("Nombre: ")
        self.Animal.LeerAnimal(name)

    def menuAll(self):
        self.Animal.LeerAnimales()

    def menuEliminar(self):
        self.Animal.EliminarAnimal()

    def menuModificar(self):
        self.Animal.ModificarAnimal()
