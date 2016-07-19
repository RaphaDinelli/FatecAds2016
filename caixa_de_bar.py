import datetime
from time import sleep

receitas = []
despesas = []

def menu():
    opcoes = {1:"Cadastrar receitas", 2:"Cadastrar despesas", 3:"Resumo"}
    print("\n" * 50)
    print("$$$$ MENU DE OPÇÕES $$$$\n\n")
    
    for i in opcoes:
        print("%s - %s" %(i, opcoes[i]))
    print()
    
    opcao = int(input("Digite a opçao desejada: "))
    print("\n" * 50)
    
    if opcao == 1:
        interface_adicionar_receitas()

def gerar_data(data):
    data_int = data.split("/")
    data_int = [int(x) for x in data_int]
    data_data = datetime.datetime(data_int[2], data_int[1], data_int[0])
    return data_data
    
def adicionar_receitas(tipo, valor, data):
    receitas.append((tipo, valor, gerar_data(data)))
    
def interface_adicionar_receitas():
    tipos = ["Salário", "Vale refeição", "Comissão", "Outros"]
    print("+++ ADICIONAR RECEITAS +++\n\n")
    try:
        opcao = int(input("Digite 1 para adicionar receitas e 2 para adicionar tipos: "))
    except :
        print("Caractere digitado invalido! Tente outra vez\n.")
        interface_adicionar_receitas()
    if opcao == 1:
        print("Tipos de receitas: \n")
        for i in tipos:
            print(i)
        try:
            tipo = input("\nDigite o tipo de receita: ")
            valor = float(input("Digite o valor: "))
            data = input("Digite a data no formato (dd/mm/aaaa)")
        except:
        	print("Dados inconsistentes! Tente outra vez.")
        	interface_adicionar_receitas()
        adicionar_receitas(tipo, valor, data)
        print("Operação concluida!")
        sleep(5)
        menu()
    
def adicionar_despesas(nome, tipo, valor, vencimento):
    receitas.append((nome, tipo, valor, gerar_data(vencimento)))

def resumo(periodo):
    total_receitas = 0.
    total_despesas = 0.
    for i in receitas:
        if i[2] >= periodo:
            total_receitas += i[1]
            
    for i in despesas:
         if i[3] >= periodo:
             total_despesas += i[2]
    
    print("RESUMO\n\n")
    print("Total das receitas: R$%.2f" % total_receitas)
    print("Total das receitas: R$%.2f\n" % total_receitas)
    print("Saldo: R$%.2f" % (total_receitas - total_despesas))
    
menu()
