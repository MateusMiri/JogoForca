import os
def desenhoForca(erros):
    forca = """
    ____
        |
        |
        -"""

    vazio = """


    """

    cabeca = """
        O
    """

    tronco = """
        O
        |
    """

    bracoEsquerdo = """
        O
       /|
    """

    bracoDireito = """
        O
       /|\\
    """
    pernaEsquerda = """
        O
       /|\\
       /   
    """

    pernaDireita = """
        O
       /|\\
       / \\  
    """

    chanceBoneco = [
        vazio, 
        cabeca, 
        tronco, 
        bracoEsquerdo, 
        bracoDireito, 
        pernaEsquerda,
        pernaDireita,
    ]


    print(forca+chanceBoneco[erros])

    
def mensagemVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print('')

def mensagemPerdedor(palavraChave):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraChave.upper()))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print('')

