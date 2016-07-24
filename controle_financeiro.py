import datetime

receitas = []
despesas = []

def menu():
	pass

def gerar_datas(data):
	data = data.split("/")
	if len(data[2]) != 4:
		print("Formato inválido!\n")
		return (False, None)
	try:
		data = [int(x) for x in data]
		data = datetime.datetime(data[2],data[1],data[0])
		return (True,data)
	except:
		print("Dados inconsistentes!")
		return (False, None)
		
def adicionar_receitas():
	tipos_de_receitas = {1:"Salário",2:"Benefícios",3:"Premios",4:"Outros"}
	id_receitas = len(receitas) + 1 
	print("=" * 59)
	print("\n\t\t\tADICIONAR RECEITAS\n")
	print(("=" * 59) + "\n")
	
	print("TIPOS DE RECEITAS\n")
	for i in tipos_de_receitas:
		print("%s - %s" %(i, tipos_de_receitas[i]))
	opcao = int(input("Digite o codigo do tipo de receita: "))
	while opcao not in tipos_de_receitas:
		print("Código invalido!")
		opcao = int(input("Digite o codigo do tipo de receita: "))
	try:
		valor = float(input("Digite o valor da receita: "))
		vencimento = input("Digite a data de recebimento: (dd/mm/aaaa)")
		if gerar_datas(vencimento)[0]:
			vencimento = gerar_datas(vencimento)[1]
			receitas.append((id_receitas, tipos_de_receitas[opcao], valor, vencimento))	
			print("\n" * 50)
			print("\t\tOPERAÇÃO REALIZADA COM SUCESSO!\n\n")
			print("Codigo da receita(ID): %s" %(id_receitas))
			print("Tipo de receita: %s" %tipos_de_receitas[opcao])
			print("Valor: %s" %valor)
			print("Data de recebimento: %s\n" %vencimento)
			input("TECLE ENTER PARA RETORNAR AO MENU.")
			menu()
		else:
			print("\n" * 50)
			adicionar_receitas()
	except:
		print("Dados inconsistentes!\n")
		input("Tecle enter para continuar.")
		print("\n" * 50)
		adicionar_receitas()
		
def mostrar_receitas():
	print("-" * 59 + "\n")
	for i in receitas:
		print("Codigo da receita(ID): %s" %(i[0]))
		print("Tipo de receita: %s" %i[1])
		print("Valor: %s" %i[2])
		print("Data de recebimento: %s\n" %i[3])
		print("-" * 59 + "\n")
		
def excluir_receitas():
	ids = [x[0] for x in receitas]
	print("=" * 59)
	print("\n\t\t\tEXCLUIR RECEITAS\n")
	print(("=" * 59) + "\n")
	mostrar_receitas()
	try:
		escolha = int(input("Digite o codigo da receita a ser excluída :"))
		while escolha not in ids:
			print("Código (ID) inválido! Tente outra vez!\n")
			escolha = int(input("Digite o codigo da receita a ser excluída :"))
	except:
		print("Dados inválidos!")
		print("\n" * 50)
		excluir_receitas()
	print('\n' * 50)
	for i in receitas:
		if i[0] == escolha:
			print("Tipo de receita: %s" %i[1])
			print("Valor: %s" %i[2])
			print("Data de recebimento: %s\n" %i[3])
			print("-" * 59 + "\n")
			confirma = input("Confirma a exclusão? (s/n): ")
			while confirma not in ("s", "n"):
				print("Opcão invalida! Tente novamente!")
				confirma = input("Confirma a exclusão? (s/n): ")
			if confirma == "s":
				receitas.remove(i)
				break
			else:
				print("Operação cancelada pelo usuário!")
	
