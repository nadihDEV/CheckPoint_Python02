# Crie uma estrutura de entrada para registrar 10 carros (ex.: placas ou modelos). Utilize a estratégia LIFO (Last In, First Out)
# para simular a retirada de um estacionamento, onde o último carro a entrar é o primeiro a sair. Mostre a ordem de entrada e a sequência de saída.

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

