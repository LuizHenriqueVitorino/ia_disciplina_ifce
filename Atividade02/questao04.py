"""
4 - Implemente a seguinte situação: dado um objeto desconhecido X(10, 20),
calcule a distancia euclidiana para os centroides das classes A(12, 18) 
e B(11, 20), com isso classifique em que classe o objeto X faz parte?   
"""
import math

# Coordenadas dos objetos
objetoDesconhecido = (10, 20)
centroideA = (12, 18)
centroideB = (11, 20)

# Função para calcular a distância euclidiana entre dois pontos
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

# Calcula as distâncias euclidianas entre o objeto desconhecido e os centroides
distanciaA = distanciaEuclidiana(objetoDesconhecido, centroideA)
distanciaB = distanciaEuclidiana(objetoDesconhecido, centroideB)

# Classificação com base nas distâncias calculadas
if distanciaA < distanciaB:
    classe = 'A'
else:
    classe = 'B'

print(f"O objeto X pertence à classe {classe}")