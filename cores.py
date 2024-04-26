'''
para representar cores \033[style;text;backm
depois do colchete: primeiro termo é o style o segundo é texto e o terceiro é background
style: 0 - none; 1 = negrito; 4 - underline; 7 - negativo
texto: 37 - branco, 31 - vermelho, 32 - verde, 33 - amarelo, 34 - azul, 35- magenta
        36 - ciano, 30 - cinza
background: as mesmas cores do texto só que começando do 40 até o 47
'''

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'

restaura_cor_original = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'

fundo_preto = '\033[40m'
fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'
fundo_magenta = '\033[45m'
fundo_ciano = '\033[46m'
fundo_branco = '\033[47m'

print('{}Bem-Vindo ao VsCode{}'.format(vermelho, restaura_cor_original))