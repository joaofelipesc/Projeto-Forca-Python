# DS 23 - VESPERTINO
#RA 23319
# JOÃO FELIPE SILVA COROMBERK




import random, time
palavra = ""
palavrasPossiveis = []
def Menu():
    print("========================[MENU DO JOGADOR]======================")
    print("SELECIONE O TEMA DO JOGO: ")
    print("1- Cores")
    print("2- Animais Selvagens")
    print("3- Eletrônicos")
    print("4- Times de futebol")
    print("5- Bairros de Campinas")
    print("6- Linguagens de programação")
    print("7- Encerrar Programa")
    escolha = int(input("Digite a opção: "))
    
    if escolha == 1:
        print("O tema selecionado foi Cores")
        Tema1()
    elif escolha == 2:
        print("O tema selecionado foi Animais Selvagens")
        Tema2()
    elif escolha == 3:
        print("O tema selecionado foi Eletrônicos")
        Tema3()
    elif escolha == 4:
        print("O tema selecionado foi Times de futebol")
        Tema4()
    elif escolha == 5:
        print("O tema selecionado foi Bairros de Campinas")
        Tema5()
    elif escolha == 6:
        print("O tema selecionado foi Linguagens de programação")
        Tema6()
    elif escolha == 7:
        print("Encerrando programa.")
        exit()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("Opção inválida")
        time.sleep(0.8)
        print("\x1b[2J\x1b[1;1H")
        return Menu()

def Menu2(palavra, palavrasPossiveis):
    print("\x1b[2J\x1b[1;1H")
    print("========================[MENU DO JOGADOR]======================")
    print("SELECIONE O NIVEL DA FORCA:")
    print("1- NÍVEL 1 (6 TENTATIVAS SEM TEMPORIZADOR)")
    print("2- NÍVEL 2 (6 TENTATIVAS E 1 MINUTO)")
    print("3- VOLTAR AO MENU ANTERIOR")
    print("4- SAIR")
    escolha = input("Selecione sua opção: ")
    if escolha == "1":
        ModoMedio(palavra, palavrasPossiveis)
        return
    elif escolha == "2":
        ModoDificil(palavra, palavrasPossiveis)
        return
    elif escolha == "3":
        print("\x1b[2J\x1b[1;1H")
        Menu()
        return
    elif escolha == "4":
        print("\x1b[2J\x1b[1;1H")
        print("Encerrando")
        exit()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("Opção inválida")
        time.sleep(0.8)
        print("\x1b[2J\x1b[1;1H")
        return Menu2(palavra,palavrasPossiveis)
    
def Tema1(): 
    palavrasPossiveis = ["AMARELO","ROXO","PRETO","VERDE","MARROM"]
    palavra = SortearPalavra(palavrasPossiveis)
    Menu2(palavra, palavrasPossiveis)

def Tema2():
    palavrasPossiveis = ["TIGRE","ELEFANTE","LEOPARDO","ZEBRA"]
    palavra = SortearPalavra(palavrasPossiveis)
    Menu2(palavra, palavrasPossiveis)
    

def Tema3():
    palavrasPossiveis = ["GELADEIRA","TELEVISAO","VIDEOGAME","ROTEADOR"]
    palavra = SortearPalavra(palavrasPossiveis)
    Menu2(palavra, palavrasPossiveis)

def Tema4():
    palavrasPossiveis = ["FLAMENGO","CORINTHIANS","PALMEIRAS","SANTOS"]
    palavra = SortearPalavra(palavrasPossiveis)
    Menu2(palavra, palavrasPossiveis) 
def Tema5():
    palavrasPossiveis = ["CAMBUÍ","TAQUARAL","BOTAFOGO","GUANABARA"]
    palavra = SortearPalavra(palavrasPossiveis)
    Menu2(palavra, palavrasPossiveis) 
def Tema6():
    palavrasPossiveis = ["PYTHON","JAVA","JAVASCRIPT","CSS","HTML"]
    palavra = SortearPalavra(palavrasPossiveis)
    Menu2(palavra, palavrasPossiveis) 


def SortearPalavra(palavrasPossiveis):
    palavra = random.choice(palavrasPossiveis)
    return palavra

def PerdeuModoMd(palavra, palavrasPossiveis):
    print("\x1b[2J\x1b[1;1H")
    print("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")
    print("Você perdeu o jogo!")
    print("Acabaram as tentativas!:( Você perdeu o jogo")
    print(f"A palavra era {palavra}")
    print("1- Repetir Tema e Modo de Jogo")
    print("2-Voltar ao Menu Principal")
    print("3-Mudar o Modo de jogo")
    print("4-Sair")
    escolha = int(input("Selecione sua Opção: "))

    if escolha == 1:
        palavra = SortearPalavra(palavrasPossiveis)
        ModoMedio(palavra, palavrasPossiveis)
    elif escolha == 2:
        Menu()
    elif escolha == 3:
        palavra = SortearPalavra(palavrasPossiveis)
        Menu2(palavra, palavrasPossiveis)
    elif escolha == 4:
        exit()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("Opção inválida")
        time.sleep(0.8)
        print("\x1b[2J\x1b[1;1H")
        return PerdeuModoMd(palavra,palavrasPossiveis)
        


def PerdeuModoDf(palavra, palavrasPossiveis):
    print("\x1b[2J\x1b[1;1H")
    print("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")
    print("Você perdeu o jogo!")
    print("O tempo ou as tentativas se esgotaram! :( Você perdeu o jogo")
    print(f"A palavra era {palavra}")
    print("1- Repetir Tema e Modo de Jogo")
    print("2-Voltar ao Menu Principal")
    print("3-Mudar o Modo de jogo")
    print("4-Sair")
    escolha = int(input("Selecione sua Opção: "))

    if escolha == 1:
        palavra = SortearPalavra(palavrasPossiveis)
        ModoDificil(palavra, palavrasPossiveis)
    elif escolha == 2:
        Menu()
    elif escolha == 3:
        palavra = SortearPalavra(palavrasPossiveis)
        Menu2(palavra, palavrasPossiveis)
    elif escolha == 4:
        exit()
    else:
        print("\x1b[2J\x1b[1;1H")
        print("Opção inválida")
        time.sleep(0.8)
        print("\x1b[2J\x1b[1;1H")
        return PerdeuModoDf(palavra,palavrasPossiveis)


def MenuFimMdMedio(palavrasPossiveis):
    while True:
        print("1-Jogar Novamente")
        print("2-Mudar Dificuldade")
        print("3-Menu Principal")
        print("4-Sair do jogo")
        p = int(input("Selecione a opção: "))

        if p == 1:
            print("\x1b[2J\x1b[1;1H")
            palavra = SortearPalavra(palavrasPossiveis)
            ModoMedio(palavra, palavrasPossiveis)
            break
        elif p == 2:
            print("\x1b[2J\x1b[1;1H")
            palavra = SortearPalavra(palavrasPossiveis)
            Menu2(palavra, palavrasPossiveis)
            break
        elif p == 3:
            print("\x1b[2J\x1b[1;1H")
            Menu()
            break
        elif p == 4:
            exit()
            break
        else:
            print("\x1b[2J\x1b[1;1H")
            print("Opção inválida")
            time.sleep(0.8)
            print("\x1b[2J\x1b[1;1H")
            return MenuFimMdMedio(palavrasPossiveis)


def MenuFimMdDificil(palavrasPossiveis):
    while True:
        print("1-Jogar Novamente")
        print("2-Mudar Dificuldade")
        print("3-Menu Principal")
        print("4-Sair do jogo")
        p = int(input("Selecione a opção: "))
        
        if p == 1:
            print("\x1b[2J\x1b[1;1H")
            palavra = SortearPalavra(palavrasPossiveis)
            ModoDificil(palavra, palavrasPossiveis)
            break
        elif p == 2:
            print("\x1b[2J\x1b[1;1H")
            palavra = SortearPalavra(palavrasPossiveis)
            Menu2(palavra, palavrasPossiveis)
            break
        elif p == 3:
            print("\x1b[2J\x1b[1;1H")
            Menu()
            break
        elif p == 4:
            exit()
            break
        else:
            print("\x1b[2J\x1b[1;1H")
            print("Opção inválida")
            time.sleep(0.8)
            print("\x1b[2J\x1b[1;1H")
            return MenuFimMdDificil(palavrasPossiveis)
        


def ModoMedio(palavra, palavrasPossiveis):
    print("Bem vindo ao Nivel 1 !!")
    print(f"A palavra tem {len(palavra)} letras. ")
    exibicaoex = "_" * len(palavra)
    exibicao = list(exibicaoex)
    palista = list(palavra)
    tentativaerradas = 0
    letraEsc = ""
    listaErros = []
    while True:
        print("\x1b[2J\x1b[1;1H")
        if tentativaerradas == 0:
            print("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
            print("Ainda restam 6 tentativas")
            
        elif tentativaerradas == 1:
           print("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
           print(" Agora te restam 5 tentativas")
        elif tentativaerradas == 2:
            print("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
            print(" Agora te restam 4 tentativas")
        elif tentativaerradas == 3:
            print("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
            print(" Agora te restam 3 tentativas")
        elif tentativaerradas == 4:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
            print(" Agora te restam 2 tentativas")
        elif tentativaerradas == 5:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
            print("Agora te resta 1 tentativa")
        print(exibicao)
        print(f"As letras que você ja digitou e estão:{listaErros}")
        print("Digite a letra que deseja chutar: ")
        print("Digite 0 se quer sortear uma nova palavra")
        print("Digite 1 se quer encerrar o programa ou voltar aos menus")
        letraEsc = input(": ").upper()
        if letraEsc in listaErros:
            print("\x1b[2J\x1b[1;1H")
            print("Essa letra já foi!!!")
            print(f"Tentativas anteriores que não é a palavra ou letras da palavra:{listaErros}")
            time.sleep(1)
        elif letraEsc in exibicao:
            print("\x1b[2J\x1b[1;1H")
            print("Você ja acertou essa letra!!")
            time.sleep(1)
        elif letraEsc == palavra:
            print("\x1b[2J\x1b[1;1H")
            print('''
    ----------------------------------------
                .-=========-.
                \\'-=======-'/
                _|   .=.   |_
               ((|  {{1}}  |))
                \|   /|\\   |/
                 \__ '`' __/
                   _`) (`_
                 _/_______\\_
                /___________\\
    ----------------------------------------
    ''')
            print(f"Você acertou a palavra!!!!{palavra}")
            MenuFimMdMedio(palavrasPossiveis)

        elif letraEsc in palista:
            for i in range(len(palista)):
                    if palista[i] == letraEsc:
                        exibicao[i] = letraEsc
                        print("\x1b[2J\x1b[1;1H")
                        print("Você acertou a letra")
                        time.sleep(0.6)
        elif letraEsc == "0":
            print("\x1b[2J\x1b[1;1H")
            print("Sorteando uma nova palavra...")
            palavra = SortearPalavra(palavrasPossiveis)
            exibicaoex = "_" * len(palavra)
            exibicao = list(exibicaoex)
            palista = list(palavra)
            tentativaerradas = 0
            print("Nova palavra sorteada")
            time.sleep(0.4)
            return ModoMedio(palavra,palavrasPossiveis)
        elif letraEsc == "1":
            j = 1
            while j > 0:
                print("\x1b[2J\x1b[1;1H")
                print("1-Encerrar")
                print("2-Menu Principal")
                print("3-Mudar Dificuldade")
                h = int(input("Opção: "))
                if h == 1:
                    print("\x1b[2J\x1b[1;1H")
                    print("Saindo!")
                    j -=1
                    time.sleep(0.6)
                    exit()
                elif h == 2:
                    print("\x1b[2J\x1b[1;1H")
                    print("Indo ao Menu Principal..")
                    Menu()
                    time.sleep(0.8)
                    print("\x1b[2J\x1b[1;1H")
                    j-=1
                elif h == 3:
                    print("\x1b[2J\x1b[1;1H")
                    print("Indo ao Menu de escolha de dificuldade")
                    time.sleep(0.8)
                    Menu2(palavra,palavrasPossiveis)
                    j-=1
                else:
                    print("\x1b[2J\x1b[1;1H")
                    print("Opção inválida")
                    time.sleep(0.7)
                    print("\x1b[2J\x1b[1;1H")
        elif letraEsc in "23456789":
            print("\x1b[2J\x1b[1;1H")
            print("Digite uma opção válida")
            time.sleep(0.8)

        else:
            print("\x1b[2J\x1b[1;1H")
            print("Você errou!!!! Esta letra não esta na palavra secreta")
            listaErros.append(letraEsc)
            tentativaerradas +=1
            time.sleep(0.8)

        if '_' not in exibicao or tentativaerradas>=6:
            break

    if tentativaerradas >=6:
        PerdeuModoMd(palavra, palavrasPossiveis)

    elif "_" not in exibicao:
        print("\x1b[2J\x1b[1;1H")
        print(f"Você ganhou o jogo!!! Era {palavra}")
        print('''
    ----------------------------------------
                .-=========-.
                \\'-=======-'/
                _|   .=.   |_
               ((|  {{1}}  |))
                \|   /|\\   |/
                 \__ '`' __/
                   _`) (`_
                 _/_______\\_
                /___________\\
    ----------------------------------------
    ''')
        MenuFimMdMedio(palavrasPossiveis)

def ModoDificil(palavra,palavrasPossiveis):
    print("Bem vindo ao Nivel 2")
    print(f"A palavra tem {len(palavra)} letras. ")
    exibicaoex = "_" * len(palavra)
    exibicao = list(exibicaoex)
    palista = list(palavra)
    tentativaerradas = 0
    letraEsc = ""
    listaErros = []
    tempoinicial = time.time()
    while True:
        print("\x1b[2J\x1b[1;1H")
        if time.time() - tempoinicial >=60:
            print("Acabou o tempo!!!!")
            print("Você perdeu o jogo :(")
            PerdeuModoDf(palavra,palavrasPossiveis)
            break
        tempoquefalta = 60 -(time.time() - tempoinicial)
        print(f"FALTAM {int(tempoquefalta)} SEGUNDOS!!")
        if tentativaerradas == 0:
            print("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
            print("Ainda restam 6 tentativas")
            
        elif tentativaerradas == 1:
           print("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
           print(" Agora te restam 5 tentativas")
        elif tentativaerradas == 2:
            print("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
            print(" Agora te restam 4 tentativas")
        elif tentativaerradas == 3:
            print("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
            print(" Agora te restam 3 tentativas")
        elif tentativaerradas == 4:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
            print(" Agora te restam 2 tentativas")
        elif tentativaerradas == 5:
            print("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
            print("Agora te resta 1 tentativa")
        print(exibicao)
        print(f"Tentativas anteriores que não é a palavra ou letras da palavra:{listaErros}")
        print("Digite a letra que deseja chutar: ")
        print("Digite 0 se quer sortear uma nova palavra")
        print("Digite 1 se quer encerrar o programa ou voltar ao menu")
        letraEsc = input(": ").upper()
        if letraEsc in listaErros:
            print("\x1b[2J\x1b[1;1H")
            print("Essa letra já foi!!!")
            print(f"Essas são as letras que você ja colocou e não estão na palavra {listaErros}")
            time.sleep(0.6)
        elif letraEsc in exibicao:
            print("\x1b[2J\x1b[1;1H")
            print("Você ja acertou essa letra!!")
            time.sleep(0.6)
        elif letraEsc == palavra:
            print("\x1b[2J\x1b[1;1H")
            print('''
    ----------------------------------------
                .-=========-.
                \\'-=======-'/
                _|   .=.   |_
               ((|  {{1}}  |))
                \|   /|\\   |/
                 \__ '`' __/
                   _`) (`_
                 _/_______\\_
                /___________\\
    ----------------------------------------
    ''')
            print(f"Você acertou a palavra!!!!{palavra}")
            MenuFimMdDificil(palavrasPossiveis)

        elif letraEsc in palista:
            for i in range(len(palista)):
                    if palista[i] == letraEsc:
                        exibicao[i] = letraEsc
                        print("\x1b[2J\x1b[1;1H")
                        print("Você acertou a letra")
                        time.sleep(0.7)
        elif letraEsc == "0":
            print("\x1b[2J\x1b[1;1H")
            print("Sorteando uma nova palavra...")
            palavra = SortearPalavra(palavrasPossiveis)
            exibicaoex = "_" * len(palavra)
            exibicao = list(exibicaoex)
            palista = list(palavra)
            tentativaerradas = 0
            tempoinicial = time.time()
            print("Nova palavra sorteada")
            time.sleep(0.5)
            return ModoDificil(palavra,palavrasPossiveis)
        elif letraEsc == "1":
            j = 1
            while j > 0:
                print("\x1b[2J\x1b[1;1H")
                print("1-Encerrar")
                print("2-Menu Principal")
                print("3-Mudar Dificuldade")
                h = int(input("Opção: "))
                if h == 1:
                    print("\x1b[2J\x1b[1;1H")
                    print("Saindo!")
                    j -=1
                    time.sleep(0.6)
                    exit()
                elif h == 2:
                    print("\x1b[2J\x1b[1;1H")
                    print("Indo ao Menu Principal..")
                    Menu()
                    time.sleep(0.8)
                    print("\x1b[2J\x1b[1;1H")
                    j-=1
                    print("\x1b[2J\x1b[1;1H")
                elif h == 3:
                    print("\x1b[2J\x1b[1;1H")
                    print("Indo ao Menu de escolha de dificuldade")
                    time.sleep(0.8)
                    Menu2(palavra,palavrasPossiveis)
                    j-=1
                    print("\x1b[2J\x1b[1;1H")
                else:
                    print("\x1b[2J\x1b[1;1H")
                    print("Opção inválida")
                    time.sleep(0.7)
                    print("\x1b[2J\x1b[1;1H")
        elif letraEsc in "23456789":
            print("\x1b[2J\x1b[1;1H")
            print("Digite uma opção válida")
            time.sleep(0.8)
        else:
            print("\x1b[2J\x1b[1;1H")
            print("Você errou!!!! Esta não é a palavra ou alguma letra da palavra!!")
            listaErros.append(letraEsc)
            tentativaerradas +=1
            time.sleep(0.7)

        if '_' not in exibicao or tentativaerradas>=6:
            break

    if tentativaerradas >=6:
        print("\x1b[2J\x1b[1;1H")
        PerdeuModoDf(palavra, palavrasPossiveis)

    elif "_" not in exibicao:
        print("\x1b[2J\x1b[1;1H")
        print(f"Você ganhou o jogo!!! A palavra era {palavra}")
        print('''
    ----------------------------------------
                .-=========-.
                \\'-=======-'/
                _|   .=.   |_
               ((|  {{1}}  |))
                \|   /|\\   |/
                 \__ '`' __/
                   _`) (`_
                 _/_______\\_
                /___________\\
    ----------------------------------------
    ''')
        MenuFimMdDificil(palavrasPossiveis)
        
        
    

    


Menu()