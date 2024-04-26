'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 
até 200Km e R$0,45 para viagens mais longas.
'''
distancia = float(input("Digite quantos km até o destino: "))

print(f"Você está prestes a fazer uma viagem de {distancia} km")

# if distancia < 200:
#     print(f'O preço da passagem é {distancia * 0.5:.2f}')
# else:
#     print(f'O preço da passagem é R$ {distancia * 0.45:.2f}')

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print(f'E o preco da sua passagem será de R$ {preco:.2f}')

