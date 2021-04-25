from Manejador import claseManejador
from Menu import claseMenu
import platform
import os
if __name__ == '__main__':
    manejador = claseManejador()
    menu = claseMenu()
    salir = False
    #carga el archivo y lo convierte en listas
    manejador.crearListaArchivo()
    #menu
    while not salir:
        print('----MENU----\n1. Crear lista de alumnos Aprobados y Desaprobados\n2. Añadir alumno'
              '\n3. Borrar alumno\n4. Ordenar listas\n5. Invertir las listas\n6. Mostrar listas\n7. Salir')
        op = int(input('Opción: '))
        os.system('cls')
        menu.opcion(op)
        salir = op == 7