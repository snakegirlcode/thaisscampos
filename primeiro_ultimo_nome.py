'''
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome_completo = input('Digite seu nome completo: ').title()
separar_nome = nome_completo.split()
primeiro_nome = separar_nome[0]
ultimo_nome = separar_nome[-1]

print('Muito prazer em te conhecer!')
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')