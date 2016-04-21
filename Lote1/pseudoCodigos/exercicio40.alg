algoritmo "Ex.40"
// Função : Receba 2 números inteiros. Verifique e mostre todos os
// números primos existentes entre eles.
// Obs.: somente valores positivos.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         a, b, cont,: inteiro
inicio
    escreval("Digite dois números em ordem crescente: ")
    leia(b)
    leia(a)

    enquanto b < a faca
        primo:=1
        escolha b
            caso 0
                b:= 1
                escreva(b, ", ")
                b:= b+1
            caso 1
                b:= b+1
                escreva(b, ", ")
                b:= b+1
            caso 2
                escreva(b, ", ")
                b:= b+1
            caso 3
                escreva(b, ", ")
                b:= b+1
            outrocaso
                para cont de 2 ate (b-1) faca
                    se(b % cont = 0) entao
                        primo := 0
                    fimse
                fimpara
        fimescolha
        se(primo > 0) entao
            escreva(b, ", ")
            b:= b+1
        senao
            primo := 1
            b:= b+1
        fimse
    fimenquanto






fimalgoritmo


