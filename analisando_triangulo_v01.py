'''
Desenvolva um programa que leia o comprimento de três retas e diga ao 
usuário se elas podem ou não formar um triângulo.
'''
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
lado_1 = float(input("Digite o comprimento da primeira reta: "))
lado_2 = float(input("Digite o comprimento da segunda reta: "))
lado_3 = float(input("Digite o comprimento da terceira reta: "))

# if lado_2 < lado_1 and lado_3 < lado_1:
#     print('É possível formar um triangulo')if lado_2 + lado_3 > lado_1 else print('Não é possível formar um triangulo com essas medidas')

# if lado_1 < lado_2 and lado_3 < lado_2:
#     print('É possível formar um triangulo') if lado_1 + lado_3 > lado_2 else print('Não é possível formar um triangulo com essas medidas')

# if lado_2 < lado_3 and lado_1 < lado_3:
#     print('É possível formar um triangulo') if lado_1 + lado_2 > lado_3 else print('Não é possível formar um triangulo com essas medidas')

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('É possível formar um triangulo com essas medidas')
else:
    print('Não é possível formar um triangulo com essas medidas')