'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''
km = float(input("Quantos km você dirigiu? "))
dias = int(input("Por quantos dias você alugou o carro? "))
preco_dias = dias * 60
preco_km = 0.15 * km
total = preco_dias + preco_km
print(f'Você usou o carro por {dias} dia(s). Custo por dia: R$ {preco_dias:.2f}')
print(f'Você dirigiu {km} km(s). O custo por km rodado é R$ {preco_km:.2f}')
print(f'O preço total a pagar é R$ {total:.2f}')