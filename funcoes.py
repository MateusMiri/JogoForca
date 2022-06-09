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
    print('Esta letra está presente na Palavra!\n')
    print('Palavra: {}' .format(chuteInicial.upper()))
    input('Pressione Enter para Continuar...')
    limparTela()

def incorreto(chuteInicial, erros):
    limparTela()
    print('Esta letra não está presente na Palavra!\n')
    print('Palavra: {}' .format(chuteInicial.upper()))
    desenhoForca(erros)
    input('Pressione Enter para Continuar...')
    limparTela()


def criarArquivo():
    arquivo = open("historico.txt","w")
    arquivo.close()

def competidorVencedor(desafiante, competidor, palavraChave):
    print('{} ganhou!!!' .format(competidor))
    print('{} perdeu!!!\n' .format(desafiante))
    arquivo = open("historico.txt","a")
    arquivo.write('---' * 7 + '\n')
    arquivo.write('Palavra Chave: {}\n' .format(palavraChave))
    arquivo.write('Vencedor: Competidor {}\n' .format(competidor))
    arquivo.write('Perdedor: Desafiante {}\n' .format(desafiante))
    arquivo.write('---' * 7 + '\n')
    arquivo.close()
    input('Pressione ENTER para continuar...')
    limparTela()

def desafianteVencedor(desafiante, competidor, palavraChave):
    print('{} ganhou!!!' .format(desafiante))
    print('{} perdeu!!!\n' .format(competidor))   
    arquivo = open("historico.txt","a")
    arquivo.write('---' * 7 + '\n')
    arquivo.write('Palavra Chave: {}\n' .format(palavraChave))
    arquivo.write('Vencedor: Desafiante {}\n' .format(desafiante))
    arquivo.write('Perdedor: Competidor {}\n' .format(competidor))
    arquivo.write('---' * 7 + '\n')
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
        print('\nNão há histórico de Partidas Disponível!\n')
        input('Pressione ENTER para continuar...')
        limparTela()

def exibirLetrasChutadas(letrasChutadas):
    if len(letrasChutadas) > 0:
        mensagem = 'Letras Chutadas:'
        print(mensagem, ''.join(letrasChutadas), '\n')
