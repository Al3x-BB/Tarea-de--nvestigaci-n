from Alumno import claseAlumno
import csv
class claseManejador:
    __lista = []    #lista de alumnos de la materia
    __listaAprob = []   #lista de alumnos aprobados
    __listaDesaprob = []    #lista de alumnos desaprobados
    __archivo = None    #archivo csv
    def __init__(self, lista = [], archivo = open('Lista de Alumnos.csv'), listaA = [], listaD = []):
        self.__lista = lista
        self.__listaAprob = listaA
        self.__listaDesaprob = listaD
        self.__archivo = archivo
    def crearListaArchivo(self):    #crea la lista de alumnos de la materia
        reader = csv.reader(self.__archivo, delimiter = ';')
        band = True
        for fila in reader:
            if(band == True):
                band = False
            else:
                unAlumno = claseAlumno(str(fila[0]), str(fila[1]), str(fila[2]), float(fila[3]))
                self.__lista.append(unAlumno)
    def crearListaAprob(self):  #crea la lista de alumnos aprobados ordenados por apellido
        for i in range(len(self.__lista)):
            if(float(self.__lista[i].getNota() >= 7)):
                self.__listaAprob.append(self.__lista[i])   #agrega el alumno aprobado a la nueva lista
    def crearListaDesaprob(self):   #crea la lista de alumnos desaprobados
        for i in range(len(self.__lista)):
            if(float(self.__lista[i].getNota() < 7)):
                self.__listaDesaprob.append(self.__lista[i])  #agrega el alumno desaprobado a la nueva lista
    def ordenar(self):
        for i in range(len(self.__lista) - 2):  #se ordena la lista general
            min = i
            for j in range(i + 1, len(self.__lista) - 1):
                if(str(self.__lista[j].getApe()) < str(self.__lista[min].getApe())):
                    min = j
            aux = self.__lista[i]
            self.__lista[i] = self.__lista[min]
            self.__lista[min] = aux
        for i in range(len(self.__listaAprob) - 2): #se ordena la lista de DESAPROBADOS por apellido
            min = i
            for j in range(i + 1, len(self.__listaAprob) - 1):
                if (str(self.__listaAprob[j].getApe()) < str(self.__listaAprob[min].getApe())):
                    min = j
            aux = self.__listaAprob[i]
            self.__listaAprob[i] = self.__listaAprob[min]
            self.__listaAprob[min] = aux
        for i in range(len(self.__listaDesaprob) - 2):  # se ordena la lista de DESAPROBADOS por apellido
            min = i
            for j in range(i + 1, len(self.__listaDesaprob) - 1):
                if (str(self.__listaDesaprob[j].getApe()) < str(self.__listaDesaprob[min].getApe())):
                    min = j
            aux = self.__listaDesaprob[i]
            self.__listaDesaprob[i] = self.__listaDesaprob[min]
            self.__listaDesaprob[min] = aux
    def printLista(self):   #muestra la lista completa
        for i in range(len(self.__lista)):
            self.__lista[i].mostrar()
    def printAprob(self):   #muestra la lista de alumnos aprobados
        for i in range(len(self.__listaAprob)):
            self.__listaAprob[i].mostrar()
    def printDesaprob(self):    #muestra la lista de alumnos desaprbados
        for i in range(len(self.__listaDesaprob)):
            self.__listaDesaprob[i].mostrar()
    def añadirAlumno(self, nom, ape, reg, nota):
        unAlumno = claseAlumno(nom, ape, reg, nota)
        self.__lista.append(unAlumno)
    def removeAlumno(self, alum):
        band = [0,0,0]
        pos = [0,0,0]
        i = 0
        while(i < len(self.__lista) and band[0] == 0):  #busca el alumno en la lista general
            alumInLista = self.__lista[i].getApe() + '-' + self.__lista[i].getNom()
            if(alum == alumInLista):
                band[0] = 1
                pos[0] = i
            i+=1
        i = 0
        while(i < len(self.__listaAprob) and band[1] == 0): #busca el alumno en la lista de aprobados
            alumInLista = self.__listaAprob[i].getApe() + '-' + self.__listaAprob[i].getNom()
            if(alum == alumInLista):
                band[1] = 1
                pos[1] = i
            i+=1
        i = 0
        while(i < len(self.__listaDesaprob) and band[2] == 0):  #busca el alumno en la lista de desaprobados
            alumInLista = self.__listaDesaprob[i].getApe() + '-' + self.__listaDesaprob[i].getNom()
            if(alum == alumInLista):
                band[2] = 1
                pos[2] = i
            i+=1

        if (band == [1,1,0] or band == [1,0,1]):    #se elimina el alumno en las dos listas posibles
            print('DATO: alumno encontrado')
            if(band == [1,1,0]):
                self.__lista.pop(pos[0])
                self.__listaAprob.pop(pos[1])
            elif(band == [1,0,1]):
                self.__lista.pop(pos[0])
                self.__listaDesaprob.pop(pos[2])
        else:
            print('ERROR: alumno no encontrado')
    def reverse(self, op):  #invierte las listas
        if(op == 1):
            self.__lista.reverse()
        elif(op == 2):
            self.__listaAprob.reverse()
        elif(op == 3):
            self.__listaDesaprob.reverse()
        else:
            print('ERROR: opción no válida')