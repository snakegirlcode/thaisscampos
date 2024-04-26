'''
Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = altura * largura

print(f'Sua parede tem uma área de {area:.3f} m²')

litro_tinta = round(area / 2)

print(f'Para {area:.2f} m² será necessario {litro_tinta} L de tinta')