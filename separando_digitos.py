'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

numero = int(input("Digite um número inteiro no intervalo de 0 a 9999: "))
numero_str = str(numero)

milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 1000) % 100) // 10
unidade = ((numero % 1000) % 100) % 10

print('--- Modo numeral ---')
print("Analisando o número", numero)
print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)

milhar_str = numero_str[-4:-3]
centena_str = numero_str[-3:-2]
dezena_str = numero_str[-2:-1]
unidade_str = numero_str[-1]

print('\n--- Modo string ---')
print("Analisando o número", numero)
print('Unidade:', unidade_str)
print('Dezena:', dezena_str)
print('Centena:', centena_str)
print('Milhar:', milhar_str)
