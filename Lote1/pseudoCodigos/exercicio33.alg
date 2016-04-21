algoritmo "Ex.33"
// Função : Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         num, incremento, resultado: real
inicio
    escreva ("Digite um número:  ")
       leia (num)
       incremento := 2
       enquanto incremento <> num faca
            resultado:= resultado + (1 + 1/incremento)
            incremento:= incremento + 1
       fimenquanto
       escreval("Resultado: ", resultado)

fimalgoritmo
