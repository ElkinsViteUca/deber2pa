BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
from colas import Cola
from listas import Lista
from helpers import Helper
from pilas import Pila
import time
import os

def gotoxy(x,y):
    print("%c[%d;%df"% (0x1B,y,x),end=" ")
    
helper = Helper()
lista=[GREEN+"1) Lista","2) Pila","3) Cola","4) Salir"]
opcion=""
while opcion != "4":
    os.system("clear")
    opcion = helper.menu(lista,YELLOW+"Menu Principal")
    if opcion == "1":
        opc1=""
        while opc1 != "7":
            os.system("clear")
            ele=Lista()
            print(YELLOW+"*"*20,"Mantenimento De Lista","*"*20)
            opc1 = helper.menu([GREEN+"1) Push","2) Pop","3) Show","4) Eliminar","5) Insertar","6) Buscar","7) Salir"],"")
            os.system("clear")
            if opc1=="1":
                print(YELLOW+"*"*23,"Push","*"*23)
               # gotoxy(0,2);dato1=int(input(GREEN+"ingrese los elementos que desee que la lista tenga:"))
                
                try:
                        gotoxy(0,2);dato1=int(input(GREEN+"Ingrese los elementos que desee que la lista tenga:"))
                        int(dato1)
                        it_is=True
                        for a in range(dato1):
                            valor=input("Ingrese el elemento:")
                            ele.push(valor)
                        input("Se guardo satisfactoriamente")    
                except ValueError:
                        it_is=False 
                        
            
            if opc1=="2":
                print(YELLOW+"*"*20,"Pop","*"*20)
                dato=ele.Borrar()
                if dato:print(input("El elemento eliminado es:{}".format(dato)))
                else:input("La lista está vacía")
            
            if opc1=="3":
                print(YELLOW+"*"*20,"Show","*"*20)
                ele.Mostrar()
                input("Presione enter para salir")
                
                
            if opc1=="4":
                
                print(YELLOW+"*"*20,"Eliminar por posicion","*"*20)
                try:
                    eli=int(input("Ingrese la posicion que desea eliminar:"))
                    int(eli)
                    it_is=True
                    ele.eliminarElementos(eli)
                    input("Presione enter para salir")
                except ValueError:
                    it_is=False
            
                
            if opc1=="5":
                print(YELLOW+"*"*20,"Ingrese por posición","*"*20)  
                while True:
                    gotoxy(0,2);dato=(input("Ingrese el dato:"))
                    while len(dato)==0:
                        time.sleep(1);gotoxy(17,2);print(" "*59)
                        gotoxy(0,2);dato=(input("Ingrese el dato:"))
                    break    
                try:
                    po=int(input("Ingrese la posición que desea tener el dato:"))   
                    int(po)
                    it_is=True
                    ele.ingresarElemento(po,dato)
                    input("Presione enter para continuar")
                except ValueError:
                        it_is=False
                                
            if opc1=="6":
                print(YELLOW+"*"*20,"Buscar","*"*20)
                gotoxy(0,2);dati=input("Ingrese el dato que desea buscar:")
                while len(dati)==0:
                    time.sleep(1);gotoxy(17,2);print(" "*59)
                    gotoxy(0,2);dati=input("Ingrese el dato que desea buscar:")
                else:
                    ele.buscarElemento(dati)  
                    input("Presionene enter para continuar")     
    
    
    elif opcion=="2":
        os.system("clear")
        gotoxy(0,2);can=input("Ingrese la cantidad de la pila :")
        while can.isnumeric()== False:
            time.sleep(1);gotoxy(32,2);print(" "*59)
            gotoxy(0,2);can=input(GREEN+"Ingrese la cantidad de la pila :")   
        ele1=Pila(can)
        opc1=""  
        while opc1 != "6":
            os.system("clear")
            print(YELLOW+"*"*20,"Mantenimento De Pila","*"*20)
            opc1 = helper.menu([GREEN+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"],"")
            os.system("clear")
            if opc1=="1":   
                print(YELLOW+"*"*20,"Push","*"*20) 
                gotoxy(0,2);dato=str(input("Ingrese el elemento:"))
                while len(dato)==0:
                    time.sleep(1);gotoxy(34,2);print(" "*59)    
                    gotoxy(0,2);dato=str(input("Ingrese el elemento:"))
                else:
                    ele1.push(dato)
                    input("Dato ingresado correctamente")
             
            if opc1=="2":
                print(YELLOW+"*"*20,"Pop","*"*20) 
                ele1.Bo()
                input(RED+"Presione enter para seguir")
                
            if opc1=="3":
                print(YELLOW+"*"*20,"Show","*"*20)
                ele1.show()
                input(RED+"Presione enter para salir")
                
            if opc1=="4":
                print(YELLOW+"*"*20,"Buscar","*"*20)
                gotoxy(0,2);dati=input("Ingrese el dato que desea buscar:")
                while len(dati)==0:
                    time.sleep(1);gotoxy(34,2);print(" "*59)
                    gotoxy(0,2);dati=input("Ingrese el dato que desea buscar:")
                else:
                    ele1.buscar(dati)  
                input("Presione enter para continuar")
                
            if opc1=="5":
                print(YELLOW+"*"*20,"Longitud","*"*20)
                num=ele1.longitud()
                print(input(GREEN+"La longitud de la pila es: {} de {}".format(num,can)))
                
    elif opcion=="3":
        os.system("clear")
        gotoxy(0,2);dad=(input("Ingrese la cantidad de la cola: "))
        while dad.isnumeric()== False:
            time.sleep(1);gotoxy(32,2);print(" "*59)
            gotoxy(0,2);dad=input(GREEN+"Ingrese la cantidad de la cola:")
        ele=Cola(dad)
        opc1="" 
        while opc1!="6": 
            os.system("clear")
            print(YELLOW+"*"*20,"Mantenimento De Cola","*"*20)
            opc1 = helper.menu([GREEN+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"],"")
            os.system("clear")
            if opc1=="1":
                print(YELLOW+"*"*20,"Push","*"*20)
                gotoxy(0,2);valor=(input("Ingrese el elemento:"))
                while len(valor)==0:
                    time.sleep(1);gotoxy(34,2);print(" "*59)    
                    gotoxy(0,2);valor=(input("Ingrese el elemento:"))
                else:
                    ele1.push(valor)
                    input("Presione enter para salir")
            
            if opc1=="2":
                print(YELLOW+"*"*20,"Pop","*"*20)
                ele.pop()
                input(RED+"Presione enter para salir")
                
            if opc1=="3":
                print(YELLOW+"*"*20,"Show","*"*20)
                ele.show()
                input(RED+"Presione enter para salir")
                
            if opc1=="4":
                print(YELLOW+"*"*20,"Buscar","*"*20)
                dati=input("ingrese el dato que desea buscar:")
                gotoxy(0,2);dati=input("Ingrese el dato que desea buscar:")
                while len(dati)==0:
                    time.sleep(1);gotoxy(34,2);print(" "*59)
                    gotoxy(0,2);dati=input("Ingrese el dato que desea buscar:")
                else:
                    ele.buscarPi(dati)  
                    input("Presionene enter para continuar")
                
            if opc1=="5":
                print(YELLOW+"*"*20,"Longitud","*"*20)
                num=ele.longitud()
                print(input(GREEN+"La longitud de la pila es: {} de {}".format(num,dad)))
                
    elif opcion=="4":
        print(RED+"Saliendo...")
        time.sleep(2);gotoxy(12,7);print("pero no contigo mi ciela XD")

time.sleep(2);gotoxy(0,8);print("Gracias")                
time.sleep(1);gotoxy(9,8);print("por")  
time.sleep(1);gotoxy(13,8);print("Visitarnos")
time.sleep(1);gotoxy(25,8);print("<3")   
time.sleep(1)