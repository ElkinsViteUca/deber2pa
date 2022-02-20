class Lista:
    def __init__(self,dato=[]):
        self.lista=dato
    
    def push(self,dato):
        self.lista.append(dato)
        
    def Borrar(self):
        if self.empty():
            print("No hay elementos en la lista")
        else:
            dato=self.lista.pop()
            return dato
    
    def eliminarElementos(self,pos):
        if self.empty():
            print("La lista está vacía")
        elif pos<0 or pos>=len(self.lista):
            return print("No existe esa posición en la lista")
        else:
            self.lista=self.lista[0:pos]+self.lista[pos+1:]
            return print(self.lista[pos])
    # def eliminarElementos(self,pos):
    #     if pos<0 or pos>=len(self.lista):
    #         return print("No existe ese valor en la lista")
    #     else:
    #         listaA=[]
    #         for ind in range(0,pos):
    #             listaA+=[self.lista[ind]]
    #         for ind in range(pos+1,len(self.lista)):
    #             listaA+=[self.lista[ind]]
    #         self.lista=listaA
    #         return self.lista
        
    def Mostrar(self):
        if self.empty():
            print("Lista vacia")
        else:  
            print("lista"," "*5,"Posicion")                
            for pos, ele in enumerate(self.lista):
                print("[{:}] {:9}".format(ele,pos))
                
    def ingresarElemento(self,pos,elem):
        pos=int(pos)
        if pos < 0 or pos > (len(self.lista)+1):
               return print("Posición incorrecta")
        else:    
            self.lista.insert(pos,elem)
            print("El elemento insertado fue: '{}' en la posición: {}".format(elem,pos))
        return
                
    
    def empty(self):
        # if self.tope == 0:
        #     return True
        # else:
        #     return False
        return len(self.lista) == 0
    
    def buscarElemento(self,buscado):
        # print("Buscar un número en una lista")
        if self.empty():
            print("Lista vacia")
        else:
            op=False
            for pos,ele in enumerate(self.lista):
                if ele==buscado:
                    op=True
                    break
            if op==True:
                print("El dato ingresado se encuentra en la posición: {}".format(pos+1))
                #print("El valor que ingreso se encuentra en la posicion: {}".format(pos+1))
            else:
                print("El dato ingresado no se encuentra en la lista")
    
numeros=Lista()
# numeros.push("Daniel")
# numeros.push("Yadi")
# numeros.push("Ana")
# numeros.Borrar("1")
#["Daniel","Yadi","Ana"]
# print(numeros.pop())
# print(numeros.pop())
#print(numeros.lista)