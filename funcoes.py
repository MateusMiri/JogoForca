import os
from desenhos import desenhoForca
def limparTela():
    os.system('cls')

def verificarChute(palavraChave, letra, letrasChutadas):
    chute = ''
    condicaoAcerto = False
    if letra in palavraChave:
        condicaoAcerto = True
    for i in palavraChave:
        if i in letrasChutadas:
            chute += i
        else:
            chute += '_'
    chuteInicial = chute
    return condicaoAcerto, chuteInicial


def correto(chuteInicial):
    limparTela()
    print('Esta letra está presente na Palavra!')
    print('Palavra: {}' .format(chuteInicial.upper()))
    input('Pressione Enter para Continuar...')
    limparTela()

def incorreto(chuteInicial):
    limparTela()
    print('Esta letra não está presente na Palavra!')
    print('Palavra:' .format(chuteInicial.upper()))

def criarArquivo():
    arquivo = open("historico.txt","w")
    arquivo.close()

def competidorVencedor(desafiante, competidor, palavraChave):
    print('{} ganhou!!!' .format(competidor))
    print('{} perdeu!!!' .format(desafiante))
    arquivo = open("historico.txt","a")
    arquivo.write('Palavra Chave: {}\n' .format(palavraChave))
    arquivo.write('Vencedor: Competidor {}\n' .format(competidor))
    arquivo.write('Perdedor: Desafiante {}\n' .format(desafiante))
    arquivo.close()
    input('Pressione ENTER para continuar...')
    limparTela()

def desafianteVencedor(desafiante, competidor, palavraChave):
    print('{} ganhou!!!' .format(desafiante))
    print('{} perdeu!!!\n' .format(competidor))   
    arquivo = open("historico.txt","a")
    arquivo.write('Palavra Chave: {}\n' .format(palavraChave))
    arquivo.write('Vencedor: Desafiante {}\n' .format(desafiante))
    arquivo.write('Perdedor: Competidor {}\n' .format(competidor))
    arquivo.close()
    input('Pressione ENTER para continuar...')
    limparTela()

def lerArquivo():
    try:
        arquivo = open("historico.txt","r")
        conteudo = arquivo.read()
        arquivo.close()
        print(conteudo)
    except:
        print('Não há histórico de Partidas Disponível!')

