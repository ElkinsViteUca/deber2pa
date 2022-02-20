class Cola:
    def __init__(self,tamanio=1):
        self.lista = []
        self.size=tamanio
        self.tope=0

    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]  
            self.tope += 1
            return self.lista
        else:
            print("La Cola esta llena")
            
    def pop(self):
        if self.empty():
            return print("La Cola está vacía")
        else:
            top = self.lista [0]
            self.lista = self.lista [1:]
            self.tope -=1  
            return print("el elemento eliminado es:",top)
        
    def show(self):
        if self.empty():
            print("Cola vacia")
        else:
            print("Cola"," "*5,"Posición")
            for pos,top in enumerate(self.lista):
                print("[{}] {:9}".format(top,pos))    
            # for top in range (self.tope):
            #     print("[{}]".format(self.lista[top]))
    
    def longitud(self):
        return self.tope
                    
             
    def empty(self):
        if self.tope== 0:
            return True
        else:
            return False
        
    def buscarPi(self,buscado):
        if self.empty():
            print("La Cola está vacía")
        else:
            la=False
            for pos,ele in enumerate(self.lista):
                if ele==buscado:
                    la=True
                    break
            if la==True:
                print("El número ingresado se encuentra en la posición: {}".format(pos+1))
            else:
                print("El número ingresado no se encuentra en la Pila")


# cola1=Cola (3)
# cola1.push(6)
# cola1.push(2)
# cola1.push(20)

# cola1.show()
# print(cola1.longitud())