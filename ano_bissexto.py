'''
 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import date

ano = int(input("Digite um ano (0 para analisar o ano atual): "))
if ano == 0:
    ano = date.today().year
if ano % 100 == 0:
    bissexto = True if ano % 400 == 0 else False

elif ano % 4 == 0:
    bissexto = True

else:
    bissexto = False

print(f'O ano de {ano} é bissexto') if bissexto is True else print(f'O ano de {ano} não é bissexto')
    