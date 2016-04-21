algoritmo "Ex.34"
// Função : Receba um número. Calcule e mostre os resultados da tabuada
// desse número.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         num, incremento, resultado: real
inicio
    escreva ("Digite um número:  ")
       leia (num)
       incremento := 1
       enquanto incremento <= 10 faca
            resultado:= incremento * num
            escreval(incremento, " x ", num, " = ", resultado)
            incremento:= incremento + 1
       fimenquanto


fimalgoritmo
