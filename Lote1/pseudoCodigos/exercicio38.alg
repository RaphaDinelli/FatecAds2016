algoritmo "Ex.38"
// Função : Receba 100 números inteiros reais. Verifique e mostre o maior
// e o menos valor.
// Obs.: somente valores positivos.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         cont, num, maior, menor : inteiro
inicio
    enquanto cont <= 5 faca
        escreva ("Digite um número:  ")
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

