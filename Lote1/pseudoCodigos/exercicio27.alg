algoritmo "exercic�o27"
// Fun��o :  Receba o n�mero de voltas, a extens�o do circuito (em metros)
// e o tempo de dura��o (minutos). Calcule e mostre a velocidade m�dia em
// km/h.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es
var
         voltas, circuito, duracao : inteiro
inicio
         escreval("Digite o n�mero de voltas: ")
         leia(voltas)
         escreval("Digite o tamanho do circuito em metros: ")
         leia(circuito)
         escreval("Digite a dura��o em minutos: ")
         leia(duracao)
         // Calcula o tamanho do circu�to em Km
         circuito := int((circuito * voltas) / 1000)
         // Converte a duracao para horas
         duracao := int(duracao / 60)
         
         //Mostra a velocidade m�dia
         escreval("Velocidade m�dia: ", (circuito / duracao))

         
fimalgoritmo
