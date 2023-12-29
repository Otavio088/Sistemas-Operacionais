'''
Alunos: Guilherme Pereira dos Santos.
        Otávio Augusto de Melo Ribeiro.
        Ryan Batista de Azevedo.
'''

import funcoes


# Programa Principal
processos = funcoes.cadastrarProcessos()
retorno = ' '
while True:
    if retorno in 'Nn':
        break

    print("-" * 70, end='')
    opcao = int(input("\n\033[34m[1]\033[m - FCFS"
                      "\n\033[34m[2]\033[m - SJF"
                      "\n\033[34m[3]\033[m - Circular"
                      "\nDigite qual gráfico deseja: "))
    if opcao == 1:
        funcoes.FCFS(processos)
    elif opcao == 2:
        funcoes.SJF(processos)
    elif opcao == 3:
        funcoes.circular(processos)

    retorno = str(input("\n\n\tDeseja exibir outro gráfico? \033[32m[S]\033[m - SIM  |  \033[31m[N]\033[m - NAO :"))
