'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
metro = float(input("Digite um valor em metros: "))
milimetro = 1000 * metro
centimetro = 100 * metro
print(f'{metro} m tem {milimetro:.0f} mm e {centimetro:.0f} cm')