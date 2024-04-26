'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, 
o aumento é de 15%.
'''

salario = float(input("Digite o valor do seu salário: "))

aumento = salario * 1.10 if salario > 1250 else salario * 1.15

print(f'O seu salario passou de R$ {salario:.2f} para R$ {aumento:.2f}')