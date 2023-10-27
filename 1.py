import numpy as np

class grafo:
    __matriz=[]
    def __init__(self, v,e):
        self.__V=v
        self.__E=e
        self.__n=len(v)
        self.__matriz=np.zeros((self.__n,self.__n), dtype=int)

        for (v1,v2) in e:
            i=v.index(v1)
            j=v.index(v2)
            self.__matriz[i,j]=1
            self.__matriz[j,i]=1
    
    def mostrar(self):
        print(self.__matriz)

    def adyacentes(self,nodo):
        adyacentes=[]
        i=self.__V.index(nodo)
        for j, valor in enumerate(self.__matriz[i]):
            if valor==1:
                adyacentes.append(v[j])
        return adyacentes

    def encontrar_camino(self, v1, v5, visitados, camino):
        visitados.add(v1)
        camino.append(v1)
        
        if v1 == v5:
            return camino
        
        for nodo in self.adyacentes(v1):
            if nodo not in visitados:
                resultado = self.encontrar_camino(nodo, v5, visitados, camino)
                if resultado:
                    return resultado
        
        camino.pop()
        return None
        
                        

if __name__ == "__main__":
    v = ['v1', 'v2', 'v3', 'v4', 'v5']
    e = [('v1', 'v2'), ('v1', 'v4'), ('v2', 'v5'), ('v3', 'v5'), ('v4', 'v5')]
    matriz = grafo(v, e)
    matriz.mostrar()
    '''nodo = input("Ingresar nodo: ")
    lista = matriz.adyacentes(nodo)
    print(f"Nodos adyacentes a {nodo} son: {lista}")'''
    
    v1 = input("Ingresar nodo u: ")
    v5 = input("Ingresar nodo v: ")
    camino = matriz.encontrar_camino(v1, v5, set(), [])
    if camino:
        print(f"Camino desde {v1} a {v5}: {camino}")
    else:
        print(f"No hay camino desde {v1} a {v5}")


