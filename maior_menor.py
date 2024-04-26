'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
from math import inf
maior = -inf
menor = inf

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número: "))

if x > maior:
    maior = x
if y > maior:
    maior = y
if z > maior:
    maior = z
if x < menor:
    menor = x
if y < menor:
    menor = y
if z < menor:
    menor = z

print(f'O maior é {maior} e o menor é {menor}')