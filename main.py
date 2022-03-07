import os
from InterfaceAnimal import *

class Main():
    def __init__(self):
        self.InterfaceAnimal = MenuAnimal()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menuPrincipal(self):
        a = 10;
        while a != 0:
            self.cls()
            print("Elige Una Colección")
            print("P) Peronas\n0) Salir")
            a = input("Selecciona una opción: ")
            if (a.upper() == 'P'):
                self.InterfaceAnimal.menu()
            elif (a == '0'):
                break;
            else:
                print("Elige Una Opcion CORRECTA!!!")
                input()

if __name__ == '__main__':
    ip = Main()
    ip.menuPrincipal()