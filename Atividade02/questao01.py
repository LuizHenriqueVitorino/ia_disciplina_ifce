'''
    Questão 1 - Dado 2 pontos em um espaço: A(10, 1, 3) e B(4, 5, 4). 
    Implemente a distancia de manhattan entre estes dois pontos?
'''

#   Vetores
A = [10, 1, 3]
B = [4, 5, 4]

def distanciaManhattan(V1, V2):
    """
        Função que calcula a distância entre dois vetores V1 e V2.
        Estes vetores precisam ter entradas numéricas e devem ser do mesmo tamanho.
        
        :param V1: array
        :param V2: array

        :return distancia
    """
    distancia = 0
    try:
        for a in range(len(V1)):
            distancia += abs(V1[a]-V2[a])
    except:
        return "Erro na operação. Verifique se os vetores são do mesmo tamanho!"
    else:
        return distancia

print(distanciaManhattan(A, B))