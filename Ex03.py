# Crie um algoritmo que permita ao usuário selecionar qual estrutura deseja utilizar:
# 1. Ordenar a lista do Exercício 1 (busca binária). 2. Atender os clientes do Exercício 2 (FIFO).3. Retirar os carros do Exercício 3 (LIFO).

def exercicio1():
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

def exercicio2():
    fila = []
    
    # Entrada de dados com for 
    n = int(input("Quantos clientes deseja adicionar? ")) # n = número de clientes
    for i in range(n):
        cliente = input(f"Nome do cliente {i+1}: ")
        fila.append(cliente) # Adiciona o cliente na lista com o append
    
    print("\nOrdem de chegada:", fila)
    print("\nIniciando atendimento: ")
    
    while fila: # Enquanto houver clientes na fila
        atendido = fila.pop(0) # Remove o primeiro cliente da fila
        print(f"\nAtendendo: {atendido}") # 
        print("Fila atual:", fila)
    
    print("\nTodos os clientes foram atendidos!")

def exercicio3():
    estacionamento = []
    contador = 1  

    while contador <= 4: # while para ter 10 entradas de carro no estacionamento 
        modelo = input(f"Digite o nome do carro: ")
        estacionamento.append(modelo)  # Adiciona no final 
        contador += 1 

    print("\nOrdem de entrada dos carros:", estacionamento)

    # LIFO: último a entrar é o primeiro a sair
    while estacionamento:  # Enquanto houver carros no estacionamento
        modelo_sai = estacionamento.pop()  # Sai o último carro 
        print(f"Saiu: {modelo_sai} | Carros restantes: {estacionamento}") # print do status do estacionamento e de saida
    
    print("\nEstacionamento vazio!")

# Menu Principal
def main():
    while True:
        print("MENU PRINCIPAL")
        print("1. Busca Binária (Lista Ordenada)")
        print("2. Atendimento FIFO (Clientes)")
        print("3. Retirada LIFO (modelos)")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == "1":
            exercicio1()
        elif opcao == "2":
            exercicio2()
        elif opcao == "3":
            exercicio3()
        elif opcao == "4":
            print("\nPrograma encerrado. Até mais!")
            break
        else:
            print("\nOpção inválida! Digite um número entre 1 e 4.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()

    