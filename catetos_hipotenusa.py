'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
import math
oposto = float(input("Digite a medida do cateto oposto: "))
adjacente = float(input("Digite a medida do cateto adjacente: "))
hipotenusa = math.hypot(oposto, adjacente)
print(f'O triangulo retângulo de lados {oposto} cm e {adjacente} cm tem hipotenusa medindo {hipotenusa:.2f} cm')