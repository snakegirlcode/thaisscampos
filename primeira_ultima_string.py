'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = input("Digite uma frase: ").upper().strip()
primeira_vez = frase.find('A')
contador_a = frase.count('A')
ultima_vez = frase.rfind('A')
print('Analisando a letra A')
print(f'Aparece a primeira vez no índice {primeira_vez+1}')
print(f'Aparece {contador_a}x na frase')
print(f'Aparece a última vez no índice {ultima_vez+1}')