'''
1. Criar e coletar um vetor [50] inteiro. Calcular e exibir:
a. A média dos valores entre 10 e 200;
b. A soma dos números ímpares.
'''

from random import randint

def preenche_vetor(x, y):
	for i in range(y):
		x.append(int(randint(0,100)))
		
vet = []

preenche_vetor(vet, 50)
media10a200 = 0
contMedia = 0
impares = 0
for i in range(len(vet)):
	if vet[i] > 10 and vet[i] < 200:
		media10a200 += vet[i]
		contMedia += 1
	if vet[i] % 2 != 0:
		impares += vet[i]
		
media10a200 = media10a200 / contMedia

print("Media dos números entre 10 e 200: ", media10a200)
print("\nSoma dos números impares:  ", impares)
