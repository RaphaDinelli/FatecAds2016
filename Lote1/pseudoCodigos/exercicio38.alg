algoritmo "Ex.38"
// Fun��o : Receba 100 n�meros inteiros reais. Verifique e mostre o maior
// e o menos valor.
// Obs.: somente valores positivos.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es 
var
         cont, num, maior, menor : inteiro
inicio
    enquanto cont <= 5 faca
        escreva ("Digite um n�mero:  ")
        leia(num)
        
        se(num > maior) entao
            maior := num
        senao
            se(menor=0) entao
                menor:= num
            senao
                se(num < menor)entao
                    menor:= num
                fimse
            fimse
        fimse
        cont := cont+1
    fimenquanto
    escreval("Maior: ", maior, " | Menor: ", menor)



fimalgoritmo

