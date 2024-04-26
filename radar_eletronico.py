'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por 
cada Km acima do limite.
'''
velocidade_carro = int(input("Qual é a velocidade atual do carro? "))
if velocidade_carro > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80 km/h.")
    print(f'Você deve pagar uma multa de R$ {(velocidade_carro - 80) * 7:.2f}!')
print("Tenha um bom dia! Dirija com segurança")
