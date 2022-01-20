import string
import random
import PySimpleGUI as sg

# Definição da interface
sg.theme('GreenTan')

layout = [
    [sg.Input('Chute uma letra',size=(18,0),key='palpite')],
    [sg.Button('Chutar'),sg.Button('Desistir')],
    [sg.Output(size=(39,10))]
]

janela = sg.Window('Adivinhe a palavra!',layout=layout)

# Leitura do arquivo com todas palavras
with open('/home/magnum/Documentos/Python/git/palavras/Lista-de-Palavras.txt','r') as f:
    palavras = f.readlines()

palavras = [i.replace('\n','') for i in palavras]

# Seleção das palavras a serem usadas
selecao_palavras = []
for palavra in palavras:
    if len(palavra) == 5:
        selecao = True
        for c in palavra:
            if c in string.punctuation:
                selecao = False
        if selecao:
            selecao_palavras.append(palavra)

indice = random.randint(0,len(selecao_palavras))
sort_palavra = selecao_palavras[indice]

acertos = 0
oculta = ['_'] * len(selecao_palavras[indice])
print(' '.join(oculta))

# Execução do jogo
try:
    while True:
        evento,valores = janela.Read()
        if evento == 'Chutar':
            err = True
            chute = valores['palpite']
            
            for i in range(0,len(sort_palavra)):
                if chute.upper() == sort_palavra[i]:
                    oculta[i] = chute.upper()
                    acertos += 1
                    err = False
            
            if err == True:
                print(f'A palavra não tem {chute.upper()}!')
            
            print('\n',' '.join(oculta))    
            if acertos == len(selecao_palavras[indice]):
                print('\nParabéns! Você acertou a palavra!')
        
        if evento == 'Desistir':
            print(f'Você desistiu! A palavra era {sort_palavra}.')
            break

        if evento == sg.WIN_CLOSED:
            break
except:
    print('Ocorreu um erro!')

while True:
    evento,valores = janela.Read()
    if evento == sg.WIN_CLOSED:
        break
janela.close()
