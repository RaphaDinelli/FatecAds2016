'''Caixa de bar'''

import datetime

# tipo do produto, nome do produto, valor, quantidade, registrador temporário
produtos = [[],[],[],[],[]]

types_p = {1:"Cerveja",2:"Destilados",3:"Drinks",4:"Lanches"}


def get_atual():
	tempo = str(datetime.datetime.today())[:16]
	return tempo
	
def abastecer_estoque():
	print("Escolha a opção desejada: \n")
	for i in types_p:
		print("%s -- %s" %(i, types_p[i]))
	opcao = int(input("\n>>"))
	
	nome = input("\nDigite o nome do produto: \n>>")
	if nome not in produtos[1]:
		produtos[0].append(opcao)
		produtos[1].append(nome)
	
		valor = float(input("\nDigite o valor unitário do produto: \n>>"))
		produtos[2].append(valor)
	
		qtd = int(input("\nDigite a quantidade do produto: \n>>"))
		produtos[3].append(qtd)
	else:
		qtd = int(input("\nDigite a quantidade do produto: \n>>"))
		produtos[3][(produtos[1].index(nome))] += qtd
	
	
		
	
def show_products(type_p):
	for i in range(len(produtos[0])):
		if produtos[0][i] == type_p:
			print("Nome:  %s" %produtos[1][i])
			print("Valor: R$%.2f" %produtos[2][i])
			print("Qtd:   %s" %produtos[3][i])
			print("\n----------------\n")
