algoritmo "exercicío27"
// Função :  Receba o número de voltas, a extensão do circuito (em metros)
// e o tempo de duração (minutos). Calcule e mostre a velocidade média em
// km/h.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações
var
         voltas, circuito, duracao : inteiro
inicio
         escreval("Digite o número de voltas: ")
         leia(voltas)
         escreval("Digite o tamanho do circuito em metros: ")
         leia(circuito)
         escreval("Digite a duração em minutos: ")
         leia(duracao)
         // Calcula o tamanho do circuíto em Km
         circuito := int((circuito * voltas) / 1000)
         // Converte a duracao para horas
         duracao := int(duracao / 60)
         
         //Mostra a velocidade média
         escreval("Velocidade média: ", (circuito / duracao))

         
fimalgoritmo
