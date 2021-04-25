import os
from Manejador import claseManejador
class claseMenu:
    __manejador = None
    def __init__(self, manejador = claseManejador()):
        self.__manejador = manejador
    def opcion(self, op):
        if(op == 1):    #crea las listas de alumnos aprobados y desaprobados
            self.__manejador.crearListaAprob()
            self.__manejador.crearListaDesaprob()
        elif(op == 2):  #añade alumno/s a la lista
            band = False
            i = 0
            print('----AÑADIR ALUMNO----\n\n(coloque Si o No al final del ingreso de datos)\n'
                  'Ingrese los datos del alumno:')
            while not band:
                i+=1
                print('ALUMNO: {}'.format(i))
                nom = str(input('Nombre: '))
                ape = str(input('Apellido: '))
                reg = str(input('N° de registro: '))
                nota = float(input('Nota: '))
                self.__manejador.añadirAlumno(nom, ape, reg, nota)
                if(str(input('¿Finalizar?: ')).lower() == 'si'):
                    band = True
        elif(op == 3):  #borra un alumno de las listas
            print('----BORRAR ALUMNO----\n\nRECOMENDACIÓN: Apellido-Nombre')
            self.__manejador.removeAlumno(str(input('Apellido y Nombre: ')))
        elif(op == 4):  #ordena las listas
            self.__manejador.ordenar()
        elif (op == 5): #invierte las listas
            os.system('cls')
            print('----INVERTIR LISTAS----\n1. Invertir la lista de alumnos gral\n2. Invertir la lista de alumnos'
                  'aprobados\n3. Invertir la lista de alumnos desaprobados')
            op = int(input('Opción: '))
            self.__manejador.reverse(op)
        elif(op == 6):  #imprime el contenido de las listas
            print('\nLISTA DE ALUMNOS:\n')
            self.__manejador.printLista()
            print('\nLISTA DE ALUMNOS APROBADOS:\n')
            self.__manejador.printAprob()
            print('\nLISTA DE ALUMNOS DESAPROBADOS:\n')
            self.__manejador.printDesaprob()
            os.system("pause")
        elif(op == 7):
            print('DATO: finalizando...')
        else:
            print('ERROR: opción inválida')