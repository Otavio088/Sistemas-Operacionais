import math


def cadastrarProcessos():
    processos = {"Quantidade": 0, "Nome": [], "Tempo": []}

    # Cadastro da quantidade de processos
    quantidade = int(input("Digite a quantidade de processos: "))
    processos["Quantidade"] = quantidade

    # Cadastro de nomes e tempo de cada processo
    nome = list()
    tempo = list()
    for i in range(1, quantidade + 1):
        nome.append(str(input(f"\nDigite o nome do {i}° processo: ")))
        tempo.append(int(input(f"Digite o tempo do {i}° processo: ")))
    processos["Nome"] = nome
    processos["Tempo"] = tempo

    return processos


def FCFS(processos):
    somaTempo = sum(processos["Tempo"])
    espacosCaracteres = 0  # São os caracteres da execucão dos tempos
    espacosAnteriores = 0  # São os espaços em relação ao gráfico, cada espaco do grafico possui 3 caracteres
    espacosPosteriores = 0  # São os espaços depois do tempo de execução

    #Dados dos processos
    dadosTempo = {"TempoEsperaIniciar": [], "TempoMedioEsperaIniciar": 0.0, "TempoProcesso": [],
                  "TempoEsperaFinalizar": [], "TempoTotalProcessador": 0}

    print(f"\nGrafico FCFS:\n{'-' * ((somaTempo * 3) + 7)}")  # Printa a quantidade de '-' conforme a quantidade de tempo dos processos
    for i in range(0, processos["Quantidade"]):
        espacosPosteriores = 0
        print(f"\t{processos['Nome'][i]:>2}|", end="")  # Printa o nome do processo
        espacosAnteriores = espacosCaracteres / 3  # Para fazer a conta de quantos tempos printar antes do tempo do processo

        # Printa os espaços antecedentes do tempo do processo
        for y in range(0, math.trunc(espacosAnteriores)):
            print("  \033[31m|\033[m", end="") #  |

        # Printa os tempos dos processos
        for x in range(0, processos["Tempo"][i]):
            print(" X\033[31m|\033[m", end="")
            espacosCaracteres += 3  # '3' é o espaco de cada tempo ' X|'

        # Printa os '  |' depois do tempo do processo
        for t in range(0, somaTempo - (processos["Tempo"][i] + math.trunc(espacosAnteriores))):
            print("  \033[31m|\033[m", end="")
            espacosPosteriores += 1  # Calcular os espacos posteriores ao tempo do processo
        print()

        # Dados dos processos
        # Calcula o TEMPO DE ESPERA PARA INICIAR
        dadosTempo["TempoEsperaIniciar"].append(math.trunc(espacosAnteriores))  # Tempo de espera para iniciar são os espaços anteriores do tempo do processo

        # Calcula o TEMPO DE ESPERA PARA FINALIZAR CADA PROCESSO
        # Subtrai o TEMPO DE ESPERA PARA INICIAR, o TEMPO DO PROCESSO e os ESPACOS POSTERIORES do TEMPO TOTAL DE PROCESSAMENTO, resultando no tempo de espera para finalizar
        dadosTempo["TempoEsperaFinalizar"].append(somaTempo - dadosTempo["TempoEsperaIniciar"][i] - processos["Tempo"][i] - espacosPosteriores)

    # Printa as linhas '-'
    print("-" * (espacosCaracteres + 7) + "\n      \033[31m|\033[m", end="")
    #  Printa o numero de cada tempo
    for i in range(1, somaTempo + 1):
        print(f"{i:>2}\033[31m|\033[m", end="")

    # Chama a função para printar os dados dos processos
    dadosTempos(dadosTempo, processos)


def SJF(processos):
    # Continua printando na sequencia, o que muda sao os espaços antes do tempo do processo
    # A unica coisa mudada é que ao inves de printar o tempo ja direto, ele printa os espaços dos tempos menores primeiro
    somaTempo = sum(processos["Tempo"])
    espacosCaracteres = 0  # São os caracteres da execução dos tempos
    espacosAnteriores = 0  # São os espaços em relação ao gráfico, cada espaco do grafico possui 3 caracteres
    espacosPosteriores = 0  # São os espaços depois do tempo de execução

    # Dados dos processos
    dadosTempo = {"TempoEsperaIniciar": [], "TempoMedioEsperaIniciar": 0.0, "TempoProcesso": [],
                  "TempoEsperaFinalizar": [], "TempoTotalProcessador": 0}
    print(f"\nGrafico SJF:\n{'-' * ((somaTempo * 3) + 7)}")  # Printa a quantidade de '-' conforme a quantidade de tempo dos processos
    for i in range(0, processos["Quantidade"]):
        espacosPosteriores = 0
        print(f"\t{processos['Nome'][i]:>2}|", end="")  # Printa o nome do processo

        espacosAnteriores = espacosAntecedentes(processos['Tempo'][i], i, processos)  # Calcula os espaços de tempo anteriores do tempo do processo
        # Printa os espaços antecedentes do tempo do processo
        for y in range(0, espacosAnteriores):
            print("  \033[31m|\033[m", end="")  # \033[m é o codigo de cor

        #  Printa os tempos dos processos
        for x in range(0, processos["Tempo"][i]):
            print(" X\033[31m|\033[m", end="")
            espacosCaracteres += 3  # '3' é o espaco de cada tempo ' X|'

        # Printa os '  |' depois do tempo do processo
        for t in range(0, somaTempo - (processos["Tempo"][i] + espacosAnteriores)):
            print("  \033[31m|\033[m", end="")
            espacosPosteriores += 1
        print()

        # Dados dos processos
        # Calcula o TEMPO DE ESPERA PARA INICIAR
        dadosTempo["TempoEsperaIniciar"].append(math.trunc(espacosAnteriores))  # Tempo de espera para iniciar são os espaços anteriores do tempo do processo

        # Calcula o TEMPO DE ESPERA PARA FINALIZAR CADA PROCESSO
        # Subtrai o TEMPO DE ESPERA PARA INICIAR, o TEMPO DO PROCESSO e os ESPACOS POSTERIORES do TEMPO TOTAL DE PROCESSAMENTO, resultando no tempo de espera para finalizar
        dadosTempo["TempoEsperaFinalizar"].append(somaTempo - dadosTempo["TempoEsperaIniciar"][i] - processos["Tempo"][i] - espacosPosteriores)

    print("-" * (espacosCaracteres + 7) + "\n      \033[31m|\033[m", end="")  #  Printa as linhas '-'
    # Printa o numero de cada tempo
    for i in range(1, somaTempo + 1):
        print(f"{i:>2}\033[31m|\033[m", end="")

    # Chama a função para printar os dados dos processos
    dadosTempos(dadosTempo, processos)


def circular(processos):
    # Se o processo for o processo comparado ele adiciona "XX" se nao for adiciona "  ", o algoritimo vai fazer isso com todos os processos
    # Se o processo estiver com tempo 0, nao ira acontecer nada nas strings, é como se o processo tivesse terminado
    listaGrafico = list()  # Grafico sem cor para ser feito os calculos
    listaGraficoCor = list()  # Grafico com cor para ser printado no terminal
    processosTempo = processos["Tempo"][:]  # Copiando uma lista
    quantum = 2
    somaTempo = sum(processos["Tempo"])
    espacosPosteriores = 0

    # Dados dos processos
    dadosTempo = {"TempoEsperaIniciar": [], "TempoMedioEsperaIniciar": 0.0, "TempoProcesso": [],
                  "TempoEsperaFinalizar": [], "TempoTotalProcessador": 0}

    # Inicializando os gráficos
    for i in range(0, processos["Quantidade"]):
        listaGrafico.append("")
        listaGraficoCor.append("")

    while True:
        # Se a soma dos processos forem 0, para o while
        if sum(processosTempo) <= 0:
            break
        # Percorre a lista auxiliar de tempo dos processos
        for celula, tempoProcesso in enumerate(processosTempo):
            if tempoProcesso >= quantum:
                # Percorre a lista das strings de cada processo que sera printada no grafico
                for indice in range(0, len(listaGrafico)):
                    # Se for o processo comparado, adciona "XX" se nao for adiciona "  "
                    if celula == indice:
                        listaGrafico[indice] += " X|" * quantum
                        listaGraficoCor[indice] += " X\033[31m|\033[m" * quantum
                    else:
                        listaGrafico[indice] += "  |" * quantum
                        listaGraficoCor[indice] += "  \033[31m|\033[m" * quantum
                # Subtrai o tempo do quantum que foi executado do processo na lista
                processosTempo[celula] -= quantum
            elif tempoProcesso < quantum:
                for indice in range(0, len(listaGrafico)):
                    if celula == indice:
                        # Se o processo for com tempo 0, ele nao vai adicionar nada, ou seja nao vai acontecer nada nas strings
                        listaGrafico[indice] += " X|" * tempoProcesso
                        listaGraficoCor[indice] += " X\033[31m|\033[m" * tempoProcesso
                    else:
                        listaGrafico[indice] += "  |" * tempoProcesso
                        listaGraficoCor[indice] += "  \033[31m|\033[m" * tempoProcesso
                # Se o processo for com tempo 0, ele vai subtrair 0, ou seja nao vai acontecer nada
                # Subtrair o tempo do processo. Ja que é menor que o quantum o tempo ira zerar
                processosTempo[celula] -= tempoProcesso

    print(f"\nGrafico Circular | quantum = 2:\n{'-' * ((somaTempo * 3) + 7)}")  # Printa a quantidade de '-' conforme a quantidade de tempo dos processos
    for i in range(0, processos["Quantidade"]):
        print(f"\t{processos['Nome'][i]:>2}|", end="")  # Printa o nome do processo
        print(listaGraficoCor[i])  # Printa as string de cada processo

    print("-" * ((somaTempo * 3) + 7) + "\n      \033[31m|\033[m", end="")  # Printa as linhas '-'
    # Printa o numero de cada tempo
    for i in range(1, somaTempo + 1):
        print(f"{i:>2}\033[31m|\033[m", end="")

    # Dados dos processos
    for i in range(0, processos["Quantidade"]):
        # Calcula o TEMPO DE ESPERA PARA INICIAR
        dadosTempo["TempoEsperaIniciar"].append(int(listaGrafico[i].find(' X|') / 3))  # Tempo de espera para iniciar são os espaços anteriores do tempo do processo

        # Calcula o TEMPO DE ESPERA PARA FINALIZAR CADA PROCESSO
        # Subtrai o TEMPO DE ESPERA PARA INICIAR, o TEMPO DO PROCESSO e os ESPACOS POSTERIORES do TEMPO TOTAL DE PROCESSAMENTO, resultando no tempo de espera para finalizar
        espacosPosteriores = int((len(listaGrafico[i]) - (listaGrafico[i].rfind(' X|') + 3)) / 3)
        dadosTempo["TempoEsperaFinalizar"].append(somaTempo - dadosTempo["TempoEsperaIniciar"][i] - processos["Tempo"][i] - espacosPosteriores)

    # Chama a função para printar os dados dos processos
    dadosTempos(dadosTempo, processos)


def espacosAntecedentes(TempoProcesso, celulaAtual, processos):
    espacos = 0
    for celulaComparada, i in enumerate(processos['Tempo']):   # "i" é o tempo do processo
        if i < TempoProcesso or (i == TempoProcesso and celulaComparada < celulaAtual):  # Se o tempo do processo comparado for menor que o processo atual ou (se o tempo do processo comparado for IGUAL ao processo atual e a celula do processo comparado for menor que a do processo atual)
            espacos += i

    return espacos


def dadosTempos(dadosTempo, processos):

    # Printa o TEMPO DE ESPERA PARA INICIAR
    print("\n\nTempo de espera para iniciar: ", end='')
    for i in range(0, processos["Quantidade"]):
        # Forma do print: p1=7
        print(f"\033[34m{processos['Nome'][i]}\033[m={dadosTempo['TempoEsperaIniciar'][i]}  ", end='')

    # Calcula e Printa o TEMPO MEDIO DE ESPERA PARA INICIAR
    dadosTempo["TempoMedioEsperaIniciar"] = sum(dadosTempo["TempoEsperaIniciar"]) / processos["Quantidade"]
    # Forma do print: 15 / 3 = 5
    print(f"\nTempo médio de espera para iniciar: {sum(dadosTempo['TempoEsperaIniciar'])}/{processos['Quantidade']} = {dadosTempo['TempoMedioEsperaIniciar']:.1f}", end='')

    # Calcula o TEMPO DOS PROCESSOS
    dadosTempo["TempoProcesso"] = processos["Tempo"][:]  # faz uma copia da lista processos["Tempo"] para a lista dadosTempo["TempoProcesso"]
    print("\nTempo de processamento de cada processo: ", end='')
    for i in range(0, processos["Quantidade"]):
        # Forma do print: p3=5
        print(f"\033[34m{processos['Nome'][i]}\033[m={dadosTempo['TempoProcesso'][i]}  ", end='')

    # Calcula o TEMPO TOTAL DO PROCESSADOR
    dadosTempo["TempoTotalProcessador"] = sum(processos["Tempo"])  # Soma os tempos de todos os processos
    print(f"\nTempo total do processador: {dadosTempo['TempoTotalProcessador']}", end='')

    # Printa o TEMPO DE ESPERA PARA FINALIZAR
    print("\nTempo de espera para finalizar: ", end='')
    for i in range(0, processos["Quantidade"]):
        # Forma do print: p2=0
        print(f"\033[34m{processos['Nome'][i]}\033[m={dadosTempo['TempoEsperaFinalizar'][i]}  ", end='')
    print()
