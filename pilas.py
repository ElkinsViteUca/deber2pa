class Pila:                
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size=tamanio
     
    def empty(self):
        # if self.tope == 0:
        #     return True
        # else:
        #     return False
        return self.tope == 0
    
    def push(self,dato):
        self.size=int(self.size)
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Pila está Llena")
   
    def Bo(self):
        if self.empty():
            return print("Lista Vacia")    
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return print("El valor eliminado es: ",top)
            
    def longitud(self):
        return self.tope
        
    def show(self):
        if self.empty():
            print("La Lista está vacia")
        else:      
            print("","Pila"," "*5,"Posición")
            for pos,top in enumerate(self.lista):
                print([top]," "*(9-len(top)),pos)
                # print("[{}] {:9}".format(top,pos))              
            # for tope in range(self.tope-1,-1,-1):
            #     print("[{}]".format(self.lista[tope]))    
    
    def buscar(self,buscado):
        if self.empty():
            print("La Pila está vacía")
        else:
            la=False
            for pos,ele in enumerate(self.lista):
                if ele==buscado:
                    la=True
                    break
            if la==True:
                print("El número que ingresó se encuentra en la posición: {}".format(pos+1))
            else:
                print("El número que ingresó no se encuentra en la Pila")
   

# Menu
# 1) Lista
#     1) push    ingres numero(4)
#     2) pop
#     3) show
#     4) eliminar ingrese la posicon a eliminar(2)
#     5) insertar
#     6) buscar
# 2) pilas
#     1) push
#     2) pop
#     3) show
#     4) buscar
#     5) lingitud

# 3) colas
#     1) push
#     2) pop
#     3) show
#     4) buscar
#     5) lingitud