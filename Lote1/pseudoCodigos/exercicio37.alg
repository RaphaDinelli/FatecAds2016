algoritmo "Ex.37"
// Fun��o : 37. Receba um n�mero inteiro. Calcule e mostre a s�rie de
// Fibonacci at� o seu N'n�simo termo.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es 
var
         num, incremento, anterior, cont : inteiro
inicio
    escreva ("Digite um n�mero:  ")
       leia (num)
       cont := 1
       anterior := cont
       incremento := cont + anterior

       escreva(anterior,", ",cont, ", ")
       enquanto (incremento < num) faca
            escreva(incremento,", ")
            cont := incremento
            incremento := incremento + anterior
            anterior := cont
       fimenquanto


fimalgoritmo
