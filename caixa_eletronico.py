'''
Lote 4
CAIXA ELETRÔNICO
1. Criar um menu de opções: Menu Principal 1 – Carregar Notas 2 – Retirar Notas 3 – Estatística 9 – Fim
1.1. Carregar a quantidade de notas em uma área da memória com 6 ocorrências.
1.2. Solicitar que o cliente faça a retirada de valores obedecendo ao critério do maior pelo menor.
1.3. Dar a opção para o cliente escolher o valor e a quantidade de notas. P. ex.: 1 x 20, 2 x 10...
1.4. Caso não tenha o valor da maior cédula, disponibilizar a próxima.
1.5. Se o valor a ser solicitado for maior que o saldo total do caixa, enviar a mensagem “EXCEDEU O LIMITE DO CAIXA”.
1.6. Solicitar até 100 retiradas ou até não haver mais notas.
1.7. No momento da solicitação do valor, coletar também o código do banco que o cliente tem conta, segundo:
1.8. No final, exibir a estatística, separada por bancos, com:
1.8.1. O maior e o menor valor sacado;
1.8.2. A média dos saques;
1.8.3. Valor total dos saques;
1.8.4. Valor das sobras dos caixas.
'''

caixa = [
    (100, 50, 20, 10, 5, 2),
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
bancos = [
    ("Banco do Brasil", "Santander", "Itaú", "Caixa"),
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

limiteSaques = 100
saldo_caixa = 0


def limpa_tela():
    print("\n" * 100)


def mostrar_notas(x):
    if x > 0:
        for i in range(len(caixa[0])):
            print((i + 1), " -- R$", caixa[0][i])
    else:
        for i in range(len(caixa[0])):
            if caixa[1][i] > 0:
                print((i + 1), " -- R$", caixa[0][i])


def saldo_total():
    global saldo_caixa
    for i in range(len(caixa[0])):
        saldo_caixa = saldo_caixa + (caixa[0][i] * caixa[1][i])


def carregar_notas():
    print("CARREGAR NOTAS\n\n")
    for i in range(len(caixa[0])):
        print("Digite a quantidade de notas de R$%i" % (caixa[0][i]))
        caixa[1][i] = int(input())
        limpa_tela()
        saldo_total()
        print("Saldo do caixa: R$%s\n" % saldo_caixa)
        for j in range(len(caixa[0])):
            if caixa[1][j] > 0:
                print("Nota de R$", caixa[0][j], "--- Quantidade: ", caixa[1][j])
        print("\n")


def copia(x):
    if x > 0:
        for i in range(len(caixa[1])):
            caixa[1][i] = caixa[2][i]
    else:
        for i in range(len(caixa[1])):
            caixa[2][i] = caixa[1][i]
    saldo_total()


def validarSaque(valor1):
    saldo_total()
    valor = valor1
    copia(0)
    if valor1 > saldo_caixa:
        print("EXCEDEU O LIMITE DO CAIXA!")
        return False
    while valor > 0:
        if valor == 11:
            caixa[3][4] = caixa[3][4] - 1
            caixa[3][5] = caixa[3][5] - 3
            valor = valor - 11
            break
        elif valor == 13:
            caixa[3][4] = caixa[3][4] - 1
            caixa[3][4] = caixa[3][4] - 4
            valor = valor - 13
            break
        else:
            cont = 0
            for i in range(len(caixa[0])):
                while valor > caixa[0][cont]:
                    if caixa[3][cont] > 0:
                        caixa[3][cont] = caixa[3][cont] - 1
                        valor = valor - caixa[0][cont]
                    else:
                        if i < len(caixa[1]):
                            break
                        else:
                            continue
                        
    def menu():
        print("------------ CAIXA ELETRÔNICO ------------\n\n")
        print("\tMenu Principal\n")
        print("1 - Carregar notas")
        print("2 - Retirar notas")
        print("3 - Estatísticas")
        print("9 - Fim\n")

        opc = int(input("\nDigite a opção desejada: "))

        while opc != 9:
            if opc == 1:
                carregar_notas()
            elif opc == 2:
                retirar_notas()
            elif opc == 3:
                estatisticas()

        print("\n" * 100)
        print("CAIXA ELETRONICO FINALIZADO")

carregar_notas()
saldo_total()

