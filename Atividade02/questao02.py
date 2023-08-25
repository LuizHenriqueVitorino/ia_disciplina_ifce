"""
2 - Dado 2 pontos em um espaço: A(12, 10) e B(11, 21). 
Implemente a distancia euclidiana entre estes dois pontos?
"""
import math

A = [12,10]
B = [11,21]

def distanciaEuclidiana(V1, V2):
    """
        Função que calcula a distância Euclidiana entre dois pontos V1 e V2.
        Estes vetores precisam ter entradas numéricas e devem ser do mesmo tamanho.
        
        :param V1: array
        :param V2: array

        :return distancia
    """
    radicando = 0
    try:
        for a in range(len(V1)):
            radicando += abs(V1[a]-V2[a])**2
            
        distancia = math.sqrt(radicando)
    except:
        return "Erro na operação. Verifique se os vetores são do mesmo tamanho!"
    else:
        return distancia
    
print(distanciaEuclidiana(A,B))