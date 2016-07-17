'''Caixa de bar'''
from datetime import datetime

class Controle_financeiro(object):
    # Armazena como string a data atual no formato aaaa/mm/dd
    hoje = datetime.today()
    
    def __init__(self):
        self.receitas = []
        self.despesas = []
        
    def gerar_datas(self, data):
        data=data.split("/")
        data = [int(x) for x in data]
        data = datetime(data[3],data[2],data[1])
        return data
        
    def adicionar_receitas(self, tipo, valor, data=self.hoje):
        self.receitas.append((tipo, valor, data))
        
    def adicionar_despesas(self, tipo, nome, valor, vencimento):
        self.despesas.append((tipo, nome, valor, vencimento))
        
    def resumo(self, periodo_inicial, periodo_final):
        total_receitas = 0.
        total_despesas = 0.
        maior_receita = 0.
        maior_despesa = 0.

        for i in self.receitas:
            if i[2] >= periodo_inicial and i[2] <= periodo_final:
                total_receitas += i[1]
            if i[1] > maior_receita:
                maior_receita = i[1]
        for i in self.despesas:
            if i[3] >= periodo_inicial and i[4] <= periodo_final:
                total_despesas += i[2]
            if i[2] > maior_despesa:
                maior_despesa = i[1]    
                
        print("TOTAL DE RECEITAS: R$%.2f\n" %total_receitas)
        print("TOTAL DE DESPESAS: R$%.2f\n\n" %total_despesas)
        print("Maior receita: R$%.2f" %maior_receita)
        print("Maior despesa: R$%.2f" %maior_receita)
        
        input("\nDigite enter para voltar ao menu.\n")
        self.menu()
        
        
    def menu(self):
        pass
