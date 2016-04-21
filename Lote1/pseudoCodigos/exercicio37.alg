algoritmo "Ex.37"
// Função : 37. Receba um número inteiro. Calcule e mostre a série de
// Fibonacci até o seu N'nésimo termo.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         num, incremento, anterior, cont : inteiro
inicio
    escreva ("Digite um número:  ")
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
