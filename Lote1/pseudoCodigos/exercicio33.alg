algoritmo "Ex.33"
// Fun��o : Receba um n�mero. Calcule e mostre a s�rie 1 + 1/2 + 1/3 + ... + 1/N.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es 
var
         num, incremento, resultado: real
inicio
    escreva ("Digite um n�mero:  ")
       leia (num)
       incremento := 2
       enquanto incremento <> num faca
            resultado:= resultado + (1 + 1/incremento)
            incremento:= incremento + 1
       fimenquanto
       escreval("Resultado: ", resultado)

fimalgoritmo
