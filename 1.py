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

        camino.pop()
        return None

if __name__ == "__main__":
    v = ['v1', 'v2', 'v3', 'v4', 'v5']
    e = [('v1', 'v2'), ('v1', 'v4'), ('v2', 'v5'), ('v3', 'v5'), ('v4', 'v5')]
    grafo_instancia = Grafo(v, e)
    grafo_instancia.mostrar()
    nodo = input("Ingresar nodo: ")
    lista = grafo_instancia.adyacentes(nodo)
    print(f"Nodos adyacentes a {nodo} son: {lista}")

    u = input("Ingresar nodo u: ")
    v = input("Ingresar nodo v: ")
    camino = grafo_instancia.encontrar_camino(u, v, set(), [])
    if camino:
        print(f"Camino desde {u} a {v}: {camino}")
    else:
        print(f"No hay camino desde {u} a {v}")


    u = input("Ingresar nodo u: ")
    v = input("Ingresar nodo v: ")
    camino = grafo_instancia.encontrar_camino(u, v, set(), [])
    if camino:
        print(f"Camino desde {u} a {v}: {camino}")
    else:
        print(f"No hay camino desde {u} a {v}")



