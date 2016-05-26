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


def mostra_bancos():
    for i in range(len(bancos[0])):
        print("%s - %s" % (i, bancos[0][i]))


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
    valor = valor1
    copia(0)
    valido = True
    cont = 0
    if valor1 > saldo_caixa:
        print("EXCEDEU O LIMITE DO CAIXA!")
        return False
    while valor > 0:
        if valor == 11:
            caixa[2][4] = caixa[2][4] - 1
            caixa[2][5] = caixa[2][5] - 3
            valor = valor - 11
            break
        elif valor == 13:
            caixa[2][4] = caixa[2][4] - 1
            caixa[2][4] = caixa[2][4] - 4
            valor = valor - 13
            break
        else:
            while valor >= caixa[0][cont]:
                if caixa[2][cont] > 0:
                    caixa[2][cont] = caixa[2][cont] - 1
                    valor = valor - caixa[0][cont]
                    if valor < caixa[0][cont] and valor != 0:
                        cont += 1
                        if cont > len(caixa[1]) - 1:
                            print("NOTAS INSUFICIENTES PARA ESTA OPERAÇÃO")
                            return False
                    elif valor == 0:
                        return valido
                else:
                    cont += 1
                    if cont > len(caixa[1]) - 1:
                        print("NOTAS INSUFICIENTES PARA ESTA OPERAÇÃO")
                        return False
                    else:
                        continue
            else:
                cont += 1
                if cont > len(caixa[1]) - 1:
                    print("NOTAS INSUFICIENTES PARA ESTA OPERAÇÃO")
                    return False
    if valor != 0:
        valido = False
    for i in range(len(caixa[2])):
        if caixa[2][i] < 0:
            valido = False
    if valido:
        return valido
    else:
        print("NOTAS INSUFICIENTES PARA ESTA OPERAÇÃO")
        return valido


def registra_banco(esc, valor):
    bancos[3][esc - 1] += valor
    if valor > bancos[1][esc - 1]:
        bancos[1][esc - 1] = valor
    else:
        if valor < bancos[2][esc - 1] or bancos[2][esc - 1] == 0:
            bancos[2][esc - 1] = valor


def retirada():
    limpa_tela()
    copia(0)
    print("$$$ --- RETIRADA DE NOTAS --- $$$\n\n")
    mostra_bancos()
    escolha_banco = int(input("Digite o código do banco desejado\n"))
    saque = int(input("Digite o valor do saque: "))

    if validarSaque(saque):
        escolha_notas(saque)
        registra_banco(escolha_banco, saque)


def escolha_notas(valor):
    limpa_tela()
    retirada = valor
    while retirada > 0:
        print("Escolha as notas desejadas: ")
        for i in range(len(caixa[0])):
            print("VALOR SOLICITADO: R$%s    |    VALOR RETIRADO: R$%s" % (valor, retirada))
            if caixa[0][i] <= retirada and caixa[1][i] > 0:
                if retirada == 0:
                    break
                else:
                    sub = - (int(input("Quantidade de notas de R$%s" % caixa[0][i])))
                    caixa[2][i] -= sub
                    retirada -= caixa[0][i]
                    if caixa[2][i] < 0 or retirada < 0:
                        retirada = valor
                        copia(0)
                        print("EXCEDEU O LIMITE DO VALOR SOLICITADO\n")
                        print("ESCOLHA NOVAMENTE")
    print("Valor de R$%s, retirado com sucesso!" % valor)
    copia(1)


def menu():
    while True:
        print("------------ CAIXA ELETRÔNICO ------------\n\n")
        print("\tMenu Principal\n")
        print("1 - Carregar notas")
        print("2 - Retirar notas")
        print("3 - Estatísticas")
        print("9 - Fim\n")
        opc = int(input("\nDigite a opção desejada: "))
        if opc == 1:
            carregar_notas()
        elif opc == 2:
            retirada()
        elif opc == 3:
            estatisticas()
        elif opc == 9:
            break
        else:
            print("OPÇÃO INVALIDA")

    print("\n" * 100)
    print("CAIXA ELETRONICO FINALIZADO")
