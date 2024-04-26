'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome_completo = input("Digite seu nome completo: ").title()

print('Seu nome tem Silva?', 'Silva' in nome_completo)