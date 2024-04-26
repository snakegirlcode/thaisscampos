'''
Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input("Digite quanto você recebe atualmente: R$ "))
novo_salario = 1.15 * salario
print(f'Atualmente você recebe R$ {salario:.2f}')
print(f'Seu novo salário com 15% de aumento será de R$ {novo_salario:.2f}')