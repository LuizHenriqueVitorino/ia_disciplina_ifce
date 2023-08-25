"""
    3 - Dado 2 pontos em um espaço: A(12, 10, 2, 23) e B(11, 21, 4, 8).
    Implemente a distancia de Chebyshev entre estes dois pontos?
"""

A = [12,10,2,23]
B = [11,21,4,8]

def distanciaChebyshev(V1, V2):
    """
        Função que calcula a distância de Chebyshev entre dois vetores V1 e V2.
        Estes vetores precisam ter entradas numéricas e devem ser do mesmo tamanho.

        :param V1: array
        :param V2: array

        :return distancia
    """
    elementos = []
    try:
        for a in range(len(V1)):
            elementos.append(abs(V1[a]-V2[a]))
            
        distancia = max(elementos)
    except:
        return "Erro na operação. Verifique se os vetores são do mesmo tamanho!"
    else:
        return distancia
    
print(distanciaChebyshev(A,B))