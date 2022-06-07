import os
from funcoes import verificarChute, correto, incorreto, competidorVencedor, desafianteVencedor, lerArquivo, limparTela, criarArquivo
from desenhos import desenhoForca, mensagemPerdedor, mensagemVencedor

while True:

    limparTela()

    erros = 0
    dicasRestantes = 3
    letrasJogadas = []
    letrasPossiveis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letrasChutadas = []

    print('Bem vindo ao Jogo da Forca!!!\n')
    print('(1) Novo Jogo')
    print('(2) Histórico de Partidas')
    print('(3) Sair\n')
    while True:
        try:
            opInicio = int(input('Digite como deseja prosseguir: '))
            if opInicio == 1:
                limparTela()
                break
            elif opInicio == 2:
                lerArquivo()
            elif opInicio == 3:
                quit()
        except:
            print('Opção Inválida')

    desafiante = input('Digite o nome do Desafiante: ')
    competidor = input('Digite o nome do Competidor: ')
    limparTela()

    palavraChave = str(input('Digite a Palavra Chave do jogo: '))
    chuteInicial = '_ ' * len(palavraChave)
    limparTela()


    dicas = []
    dicas.append(input('Digite a primeira dica: '))
    dicas.append(input('Digite a segunda dica: '))
    dicas.append(input('Digite a terceira dica: '))

    limparTela()

    while erros != 6 and chuteInicial != palavraChave:
        desenhoForca(erros)
        print('Palavra: {}' .format(chuteInicial.upper()))
        print('Você possui {} dicas restantes!' .format(dicasRestantes))
        print('\n(1) Jogar')
        print('(2) Solicitar Dica')
        print('(3) Histórico de Partidas\n')
        while True:
            try:
                op = int(input('Digite como deseja prosseguir: '))
                break
            except:
                print('Opção Inválida!')
                input('Pressione Enter para Continuar...')
            limparTela()
        
        if op == 1:

            while True:
                mensagem = 'Letras Chutadas:'
                print(mensagem, letrasChutadas, '\n')
                letra = input('Digite a letra ou a palavra que deseja chutar (sem os acentos): ')
                if len(letra) == 1 and letra not in letrasPossiveis:
                    print('Caractere inválido!')
                elif letra in letrasChutadas:
                    print('Você já chutou essa letra!')
                else:   
                    break
            
                
            if len(letra) > 1:
                if letra == palavraChave:
                    chuteInicial = letra
                    break
                else:
                    print('A palavra não está correta!')
                    erros += 1
                    desenhoForca(erros)
            else:
                letrasChutadas.append(letra)
                condicaoAcerto, chuteInicial = verificarChute(palavraChave, letra, letrasChutadas)

                if condicaoAcerto:
                    correto(chuteInicial)  
                else:
                    incorreto(chuteInicial)
                    erros += 1
                    desenhoForca(erros)
                    input('Pressione Enter para Continuar...')
                    limparTela()

        if op == 2:
            if dicasRestantes > 0:
                print('Sua dica é:', dicas[-(dicasRestantes)])
                dicasRestantes -= 1
            else:
                print('Você não possui mais dicas restantes!')

            while True:
                mensagem = 'Letras Chutadas:'
                print(mensagem, letrasChutadas, '\n')
                letra = input('Digite a letra ou a palavra que deseja chutar (sem os acentos): ')
                if len(letra) == 1 and letra not in letrasPossiveis:
                    print('Caractere inválido!')
                elif letra in letrasChutadas:
                    print('Você já chutou essa letra!')
                else:   
                    break

            if len(letra) > 1:
                if letra == palavraChave:
                    chuteInicial = letra
                    break
                else:
                    print('A palavra não está correta!')
                    erros += 1
                    desenhoForca(erros)
            else:
                letrasChutadas.append(letra)
                condicaoAcerto, chuteInicial = verificarChute(palavraChave, letra, letrasChutadas)

                if condicaoAcerto:
                    correto(chuteInicial)  
                else:
                    incorreto(chuteInicial)
                    erros += 1
                    desenhoForca(erros)
                    input('Pressione Enter para Continuar...')
                    limparTela()

        elif op == 3:
            lerArquivo()

        elif op != 1 and op != 2 and op != 3:
            print('Opção Inválida!')
            input('Pressione Enter para Continuar...')
            limparTela()

    if chuteInicial == palavraChave:
        mensagemVencedor()
        try:
            competidorVencedor(desafiante, competidor, palavraChave)
        except:
            criarArquivo()
            competidorVencedor(desafiante, competidor, palavraChave)

    elif erros == 6:
        mensagemPerdedor(palavraChave)
        try:
            desafianteVencedor(desafiante, competidor, palavraChave)
        except:
            criarArquivo()
            desafianteVencedor(desafiante, competidor, palavraChave)