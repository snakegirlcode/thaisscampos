'''
Escreva um programa que faça o computador “pensar” em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
escolhido pelo computador. O programa deverá escrever na tela se o 
usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

numero_secreto = randint(0,5)

nome = input('Digite seu nome: ')
print('-=-'*20)
print('Bem-vindo ao jogo da adivinhação,', nome)
print('-=-'*20)
print('Pensando em número aleatório...')
sleep(3)
print('Pronto! Agora tente adivinhar o número que pensei')
numero_usuario = int(input('Digite um número: '))
print('Processando...')
sleep(2)
if numero_usuario == numero_secreto:
    print('Parabéns, você acertou')
else:
    print('Você errou, o número secreto era', numero_secreto)