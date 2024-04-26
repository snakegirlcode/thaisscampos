'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
a. O nome com todas as letras maiúsculas e minúsculas.
b. Quantas letras ao todo (sem considerar espaços).
c. Quantas letras tem o primeiro nome.
'''

nome_completo = input("Digite seu nome completo: ")

print("Analisando seu nome...")
print('Seu nome em maiúsculas é', nome_completo.upper())
print('Seu nome em minúsculas é',nome_completo.lower())

nome_separado = nome_completo.split()
#nome_junto_sem_espaço = ''.join(nome_separado)

print(f'Seu nome tem ao todo {len(nome_completo) - nome_completo.count(' ')} letras')
print(f'Seu primeiro nome é {nome_separado[0].title()} e ele tem {len(nome_separado[0])} letras')