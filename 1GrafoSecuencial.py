import numpy as np

class Grafo:
    def __init__(self, v, e):
        self.__V = v
        self.__E = e
        self.__n = len(v)
        self.__matriz = np.zeros((self.__n, self.__n), dtype=int)

        for (v1, v2) in e:
            i = self.__V.index(v1)
            j = self.__V.index(v2)
            self.__matriz[i, j] = 1
            self.__matriz[j, i] = 1

    def mostrar(self):
        print(self.__matriz)

    def adyacentes(self, nodo):
        adyacentes = []
        j = self.__V.index(nodo)
        for i in range(self.__n):
            if self.__matriz[i, j] == 1:
                adyacentes.append(self.__V[i])
        return adyacentes
    
    def listaCamino(self, nodo):
        camino = []
        i = self.__V.index(nodo)
        for j, valor in enumerate(self.__matriz[i]):
            if valor == 1:
                camino.append(self.__V[j])  # Cambié v[j] por self.__V[j]
        return camino

    def encontrar_camino(self, u, v, visitados, camino):
        visitados.add(u)
        camino.append(u)

        if u == v:
            return camino

        for nodo in self.listaCamino(u):
            if nodo not in visitados:
                resultado = self.encontrar_camino(nodo, v, visitados, camino)
                if resultado:
                    return resultado
                
    def es_conexo(self):
        for i in range(self.__n):
            for j in range(i + 1, self.__n):
                u = self.__V[i]
                v = self.__V[j]
                camino = self.encontrar_camino(u, v, set(), [])
                if not camino:
                    return False
        
        return True
    
    def es_aciclico(self):
        visitados = set()
        en_proceso = set()
        
        def tiene_ciclo(nodo):
            if nodo in en_proceso:
                return True
            if nodo in visitados:
                return False
            
            visitados.add(nodo)
            en_proceso.add(nodo)
            
            for vecino in self.adyacentes(nodo):
                if tiene_ciclo(vecino):
                    return True
            
            en_proceso.remove(nodo)
            return False
        
        for nodo in self.__V:
            if tiene_ciclo(nodo):
                return False  # Se encontró un ciclo
        
        return True  # No se encontraron ciclos
    
    def REA(self, nodo_inicial):
        visitados = set()

        def recorrido_en_profundidad(nodo):
            if nodo not in visitados:
                visitados.add(nodo)
                print(nodo)  # Puedes cambiar esto para realizar alguna acción en lugar de imprimir el nodo

                for vecino in self.adyacentes(nodo):
                    if vecino not in visitados:
                        recorrido_en_profundidad(vecino)

        recorrido_en_profundidad(nodo_inicial)

    
    def REP(self, nodo_inicial):
        visitados = set()
        pila = [nodo_inicial]

        while pila:
            nodo = pila.pop()
            if nodo not in visitados:
                visitados.add(nodo)
                print(nodo)  # Puedes realizar alguna acción en lugar de imprimir el nodo

                for vecino in self.adyacentes(nodo):
                    if vecino not in visitados:
                        pila.append(vecino)



if __name__ == "__main__":
    v = ['v1', 'v2', 'v3', 'v4', 'v5']
    e = [('v1', 'v2'), ('v1', 'v3'), ('v1', 'v4'), ('v2', 'v5'), ('v3', 'v5'), ('v3', 'v4'), ('v4', 'v5')]
    grafo = Grafo(v, e)
    grafo.mostrar()

    '''nodo = input("Ingresar nodo: ")
    lista = grafo.adyacentes(nodo)
    print(f"Nodos adyacentes a {nodo} son: {lista}")'''

    '''u = input("Ingresar nodo u: ")
    v = input("Ingresar nodo v: ")
    camino = grafo.encontrar_camino(u, v, set(), [])
    if camino:
        print(f"Camino desde {u} a {v}: {camino}")
    else:
        print(f"No hay camino desde {u} a {v}")'''

    conexo = grafo.es_conexo()
    if conexo:
        print("El grafo es conexo")
    else:
        print("El grafo no es conexo")

    aciclico=grafo.es_aciclico()
    if aciclico:
        print("El grafo es aciclico")
    else:
        print("El grafo es ciclico")

    nodo=input("Ingresar nodo inicial: ")
    grafo.REA(nodo)

    nodo=input("Ingresar nodo inicial: ")
    grafo.REP(nodo)

   

    




