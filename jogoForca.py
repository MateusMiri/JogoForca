import os
from funcoes import verificarChute, correto, incorreto, competidorVencedor, desafianteVencedor, lerArquivo, limparTela, criarArquivo, exibirLetrasChutadas
from desenhos import desenhoForca, mensagemPerdedor, mensagemVencedor

while True:

    limparTela()

    erros = 0
    dicasRestantes = 3
    letrasJogadas = []
    letrasPossiveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letrasChutadas = []

    print('Bem vindo ao Jogo da Forca!!!\n')
    
    while True:
  
        print('(1) Novo Jogo')
        print('(2) Histórico de Partidas')
        print('(3) Sair')
        opInicio = input('\nDigite como deseja prosseguir: ')
        if opInicio == "1":
            limparTela()
            break
        elif opInicio == "2":
            lerArquivo()
        elif opInicio == "3":
            quit()
        else:
            print('Opção Inválida!')
    
    desafiante = input('Digite o nome do Desafiante: ').capitalize()
    competidor = input('Digite o nome do Competidor: ').capitalize()
    limparTela()

    while True:
        verifPalavra = True
        palavraChave = str(input('Digite a Palavra Chave do jogo: ').upper())
        for i in palavraChave:
            if i not in letrasPossiveis:
                verifPalavra = False
        if verifPalavra == False:
            print('A palavra possui Caracteres Inválidos!')
            input('Pressione Enter para Continuar...')
        elif verifPalavra:
            break           
                
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
        print('(2) Solicitar Dica\n')
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
                exibirLetrasChutadas(letrasChutadas)
                letra = input('\nDigite a letra ou a palavra que deseja chutar (sem os acentos): ').upper().strip()
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
                    input('Pressione Enter para Continuar...')
                    limparTela()
            else:
                letrasChutadas.append(letra)
                condicaoAcerto, chuteInicial = verificarChute(palavraChave, letra, letrasChutadas)

                if condicaoAcerto:
                    correto(chuteInicial)  
                else:
                    erros += 1
                    incorreto(chuteInicial, erros)
                    

        elif op == 2:
            if dicasRestantes > 0:
                print('\nSua dica é:', dicas[-(dicasRestantes)])
                dicasRestantes -= 1
            else:
                print('\nVocê não possui mais dicas restantes!\n')

            while True:
                exibirLetrasChutadas(letrasChutadas)
                letra = input('Digite a letra ou a palavra que deseja chutar (sem os acentos): ').upper().strip()
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
                    incorreto(chuteInicial, erros)
                    erros += 1
                    desenhoForca(erros)
                    input('Pressione Enter para Continuar...')
                    limparTela()

        else:
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