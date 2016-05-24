caixa = [
			 [100,50,20,10,5,2], 
			 [0,0,0,0,0,0], 
			 [0,0,0,0,0,0]
		 ]
bancos = [
			["Banco do Brasil","Santander", "Itaú", "Caixa"], 
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]
		]
		
limiteSaques = 100
saldo_caixa = 0

def limpa_tela():
	print("\n" * 100)
	
def mostrar_notas(x):
	if x > 0:
		for i in range(len(caixa[0])):
			print((i+1), " -- R$", caixa[0][i])
	else:
		for i in range(len(caixa[0])):
			if caixa[1][i] > 0:
				print((i+1), " -- R$", caixa[0][i])
				
def saldo_total():
	total = 0
	for i in range(len(caixa[0])):
		total = total + (caixa[0][i] * caixa[1][i])
	return total
				
def carregar_notas():
	print("CARREGAR NOTAS\n\n")
	for i in range(len(caixa[0])):
		print("Digite a quantidade de notas de R$%i" %(caixa[0][i]))
		caixa[1][i] = int(input())
		limpa_tela()
		saldo_caixa = saldo_total()
		print("Saldo do caixa: R$", saldo_caixa )
		for j in range(len(caixa[0])):
			if caixa[1][j] > 0:
				print("Nota de R$", caixa[0][j], "--- Quantidade: ",caixa[1][j])
		print("\n")
	





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
print(saldo_caixa)
