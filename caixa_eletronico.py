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
from time import sleep

# A primeira linha refere-se aos tipos de notas, a segunda a quantidade e a terceira são registradores
# temporários da quantidade de notas para as auxíliar nas operações 
caixa = [
    (100, 50, 20, 10, 5, 2), 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0] 
]

# A primeira linha refere-se aos tipos de bancos, a segunda linha ao maior valor sacado,
# a terceira linha ao menor valor sacado e a ultima linha ao valor total sacado.
bancos = [
    ("Banco do Brasil", "Santander", "Itaú", "Caixa"),  # Tipos de bancos disponpiveis
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


limiteSaques = 100
saldo_caixa = 0


def limpa_tela():
    print("\n" * 100)

def mostrar_notas(x):
	'''
	Se x for maior que 0 mostra as notas caso a quantidade (caixa[1][y]) for maior que 0.
	Do contrário mostra todas as notas.
	'''
    if x > 0:
        for i in range(len(caixa[0])):
            print((i + 1), " -- R$", caixa[0][i])
    else:
        for i in range(len(caixa[0])):
            if caixa[1][i] > 0:
                print((i + 1), " -- R$", caixa[0][i])


def mostra_bancos():
	'''
	Mostra os bancos.
	'''
    for i in range(len(bancos[0])):
        print("%s - %s" % ((i + 1), bancos[0][i]))
    print("\n$--------------------------------$\n")


def saldo_total():
	'''
	Atualiza o saldo do caixa multiplicando a quantidade de notas pelo seu valor.
	'''
    global saldo_caixa
    saldo_caixa = 0
    for i in range(len(caixa[0])):
        saldo_caixa = saldo_caixa + (caixa[0][i] * caixa[1][i])


def carregar_notas():
	'''
	Carrega as notas no caixa.
	'''
    print("CARREGAR NOTAS\n\n")
    
    # Carrega a quantidade de cada tipo de nota do caixa (caixa[0][x])
    for i in range(len(caixa[0])):
        print("Digite a quantidade de notas de R$%i" % (caixa[0][i]))
        caixa[1][i] += int(input())
        limpa_tela()
        saldo_total()
        print("Saldo do caixa: R$%s\n" % saldo_caixa)
        
        # Mostra a quantidade atual de cada nota caso seja maior que 0.
        for j in range(len(caixa[0])):
            if caixa[1][j] > 0:
                print("Nota de R$", caixa[0][j], "--- Quantidade: ", caixa[1][j])
        print("\n")
    print("CARREGAMENTO COMPLETO")
    sleep(5)
    limpa_tela()


def copia(x):
	'''
	Caso valor seja 1 copia para a linha de quantidade de notas (caixa[1][x]) o valor 
	dos registradores temporários (caixa[2][x]).
	
	Caso valor seja 0 copia para os registradores temporários o valor da quantidade de notas.
	'''
    if x > 0:
        for i in range(len(caixa[1])):
            caixa[1][i] = caixa[2][i]
    else:
        for i in range(len(caixa[1])):
            caixa[2][i] = caixa[1][i]
    saldo_total()


def validarSaque(valor1):
	'''
	Verifica se é possível sacar o valor solicitado dentro das possibilidades disponíveis conforme, 
	a quantidade de notas e saldo do caixa.
	'''
    valor = valor1
    copia(0)
    valido = True
    cont = 0
    
    # Verifica se o valor solicitado é menor ou igual ao saldo do caixa.
    if valor1 > saldo_caixa:
        print("EXCEDEU O LIMITE DO CAIXA!")
        return False
    while valor > 0:
    	
    	# Verifica se há notas de 5 e 2 disponíveis para saques que terminem em 1 ou 3 
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
        	
        	# Verifica se o valor pode ser sacado subtraindo a maior nota mais próxima do valor,
        	# até que não haja mais notas daquele tipo ou que o  valor tenha sido zerado.
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
    
    # Caso o valor seja diferente de 0, ou caso a quantidade de notas nos registradores temporários, 
    # seja negativo, significa que não há notas disponíveis para o valor solicitado.
    
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
	'''
	Registra a operação de saque na matriz bancos[][]
	'''
    esc -= 1 # Ajusta o indice da matriz caixa[][]
    bancos[3][esc] += valor  # Soma o valor do saque ao valor total sacado.
    
    # Determina o maior e o menor valor sacado.
    if valor > bancos[1][esc]:
        bancos[1][esc] = valor
    else:
        if valor < bancos[2][esc] or bancos[2][esc] == 0:
            bancos[2][esc] = valor


def retirada():
	'''
	Efetua saques do caixa, solicita o banco, o valor e o valor a ser retirado, verifica se é possível retirar o valor solicitado
	
	e se positivo chama a função para escolha das notas.
	'''
    global limiteSaques
    limpa_tela()
    copia(0)
    
    # Verifica se não foi ultrapassado o número máximo de saques, e prossegue com as verificações 
    if limiteSaques > 0:
        print("$$$ --- RETIRADA DE NOTAS --- $$$\n\n")
        mostra_bancos()
        escolha_banco = int(input("Digite o código do banco desejado\n"))
        saque = int(input("Digite o valor do saque: "))
        if validarSaque(saque):
            escolha_notas(saque)
            registra_banco(escolha_banco, saque)
            limiteSaques -= 1
    else:
        print("LIMITE DO NÚMERO DE SAQUES EXCEDIDO!\n")
        sleep(5)
        limpa_tela()


def escolha_notas(valor):
	'''
	Solicita ao usuário a escolha das notas referente ao saque.
	'''
    limpa_tela()
    retirada = valor
    
    # Solicita a escolha de notas ao usuário enquanto ainda ouver valor a ser sacado.
    while retirada > 0:
        print("Escolha as notas desejadas: ")
        for i in range(len(caixa[0])):
        	
        	# Oferece a opção de escolha da próxima nota menor ou igual ao valor de saque restante.
            if caixa[0][i] <= retirada and caixa[1][i] > 0:
                if retirada == 0:
                    break
                else:
                    print("VALOR SOLICITADO: R$%s    |    VALOR RETIRADO: R$%s" % (valor, (valor - retirada)))
                    sub = (int(input("Quantidade de notas de R$%s: " % caixa[0][i])))
                    caixa[2][i] -= sub
                    retirada -= caixa[0][i] * sub
                    if caixa[2][i] < 0 or retirada < 0:
                        retirada = valor
                        copia(0)
                        print("EXCEDEU O LIMITE DO VALOR SOLICITADO\n")
                        print("ESCOLHA NOVAMENTE")
                        break
    print("\n\nValor de R$%s, retirado com sucesso!" % valor)
    sleep(5)
    copia(1)
    limpa_tela()


def estatisticas():
    limpa_tela()
    print("ESTATÍSTICAS\n")
    mostra_bancos()
    escolha_banco = int(input("\nDigite o código do banco escolhido: "))
    limpa_tela()
    escolha_banco -= 1
    print("$$$----%s----$$$\n" % bancos[0][escolha_banco])
    print("\nVALOR TOTAL SACADO : R$%s" % bancos[3][escolha_banco])
    print("MAIOR VALOR SACADO: R$%s" % bancos[1][escolha_banco])
    print("MENOR VALOR SACADO: R$%s\n" % bancos[2][escolha_banco])
    print("SOBRA DO CAIXA: R$%s\n" % saldo_caixa)

    input("Digite enter para terminar!")
    limpa_tela()


def menu():
    while True:
        print("------------ CAIXA ELETRÔNICO ------------\n\n")
        print("\tMenu Principal\n")
        print("1 - Carregar notas")
        print("2 - Retirar notas")
        print("3 - Estatísticas")
        print("9 - Fim\n")
        try:
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
                sleep(5)
                limpa_tela()
        except:
            print("Entrada inválida!")

    print("\n" * 100)
    print("CAIXA ELETRONICO FINALIZADO")
    
menu()
