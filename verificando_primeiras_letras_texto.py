'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''

cidade = input("Digite o nome da sua cidade: ").upper()
cidade_separado = cidade.split()

print('SANTO' in cidade_separado[0])