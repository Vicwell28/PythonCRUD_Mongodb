import os
from Persona import * 
class MenuPersona():

    def __init__(self):
        self.Persona = Persona()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        a = 10;
        while a != 0:
            self.cls()
            print("¿Que Quieres Hacer\nC) Insertar Persona \nR) Mostrar Personaes\nU) Actualizar Persona\nD) Eliminar Persona\n0) Salir")

            op = input("Respuesta: ")

            if op.upper() == "C": 
                self.menuCreate()
            elif op.upper() == "R":
                a = 10;
                while a != 0:
                    self.cls()
                    print("Opcion Mostrar Personaes\n1) Mostar Por Id\n2) Mostrar Todos Los Personaes\n0) Salir")
                    R = input("Respuesta: ")
                    if R.upper() == "1":
                        self.menuFind()
                        input("Enter Para Continuar...")
                    elif R.upper() == "2":
                        
                        self.menuAll()
                        input("Enter Para Continuar...")
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
        self.Persona.CreatePersona(name, type, age, gender)

    def menuFind(self):
        name = input("Nombre: ")
        self.Persona.LeerPersona(name)

    def menuAll(self):
        self.Persona.LeerPersonaes()

    def menuEliminar(self):
        self.Persona.EliminarPersona()

    def menuModificar(self):
        self.Persona.ModificarPersona()
