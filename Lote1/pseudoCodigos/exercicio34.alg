algoritmo "Ex.34"
// Fun��o : Receba um n�mero. Calcule e mostre os resultados da tabuada
// desse n�mero.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es 
var
         num, incremento, resultado: real
inicio
    escreva ("Digite um n�mero:  ")
       leia (num)
       incremento := 1
       enquanto incremento <= 10 faca
            resultado:= incremento * num
            escreval(incremento, " x ", num, " = ", resultado)
            incremento:= incremento + 1
       fimenquanto


fimalgoritmo
