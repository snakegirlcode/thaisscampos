'''
Faça um programa que leia um ângulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo_graus = float(input("Digite um ângulo: "))
angulo_rad = math.radians(angulo_graus)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
print(f'O seno de {angulo_graus} é {seno:.2f}')
print(f'O cosseno de {angulo_graus} é {cosseno:.2f}')
print(f'A tangente de {angulo_graus} é {tangente:.2f}')
