# Dada a lista ordenada [3, 5, 7, 8, 11, 14, 15], utilize o algoritmo de busca binária para encontrar o valor 11. 
# Retorne o índice do alvo e mostre o funcionamento do algoritmo passo a passo (a cada iteração).

lista = [3, 5, 7, 8, 11, 14, 15]
alvo = 11

def busca(lista, alvo): #Criei uma função que dentro dela contém a lista e o alvo 
    l, h = 0, len(lista) - 1  # l = 0 indice de inicio da lista , h = 0, len(lista) == o len vai contar quantos numeros tem na lista 7 e - 1 = 6 ultimo indice da lista

    while l <= h:  
        m = (l + h) // 2  # Índice do meio
        print(f"l={l}, h={h}, m={m}, lista[m]={lista[m]}")  # print da busca
        
        if lista[m] == alvo:  
            return m
        elif lista[m] < alvo:  
            l = m + 1
        else:  
            h = m - 1

    return -1  

resultado = busca(lista, alvo)
print(f"O índice do alvo 11 é igual a: {resultado}")
