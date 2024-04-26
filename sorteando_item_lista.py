'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na 
tela o nome do escolhido.
'''
import random

aluno_1 = input("Digite o nome do primeiro aluno: ").title()
aluno_2 = input("Digite o nome do segundo aluno: ").title()
aluno_3 = input("Digite o nome do terceiro aluno: ").title()
aluno_4 = input("Digite o nome do quarto aluno: ").title()

alunos = aluno_1, aluno_2, aluno_3, aluno_4

escolha = random.choice(alunos)

print(f'O aluno escolhido foi {escolha}')
