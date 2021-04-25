import re
class claseAlumno:
    __nom = ''
    __ape = ''
    __reg = ''
    __nota = 0.0
    def __init__(self, nom, ape, reg, nota):    #se crea el objeto alumno y se validan los datos
        if(re.match('^[(a-z)]{3,30}$', nom.lower())):
            if(re.match('^[(a-z)]{2,30}$', ape.lower())):
                if(re.match('^[(0-9)]{5}$', reg)):
                    if(nota>=0 and nota<=10):
                        self.__nom = nom
                        self.__ape = ape
                        self.__reg = reg
                        self.__nota = nota
                    else:   #si la nota es incorrecta
                        print('ERROR: nota del alumno es incorrecto')
                else:   #si el n° de registro es incorrecto
                    print('ERROR: n° de registro es incorrecto')
            else:   #si el apellido es incorrecto
                print('ERROR: apellido del alumno es incorrecto')
        else:   #si el nombre es incorrecto
            print('ERROR: nombre del alumno es inválido')
    def mostrar(self):
        print('{}\t{}\t{}\t{}'.format(self.__nom, self.__ape, self.__reg, self.__nota))
    def getNota(self):
        return self.__nota
    def getApe(self):
        return self.__ape
    def getNom(self):
        return self.__nom
