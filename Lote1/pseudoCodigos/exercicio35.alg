algoritmo "Ex.35"
// Função : Receba 2 números inteiros, verifique qual o maior entre eles.
// Calcule e mostre o resultado da somatória dos números ímpares entre
// esses valores.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         num1, num2, maior, menor, soma, cont : inteiro
inicio
    escreva ("Digite um número:  ")
       leia (num1)
    escreva ("Digite um número:  ")
       leia (num2)
       
    se(num1 > num2) entao
        maior := num1
        menor := num2
    senao
        maior := num2
        menor := num1
    fimse
    cont:= menor + 1
    
    enquanto cont < maior faca
        se((cont%2)<> 0) entao
            soma := soma + cont
        fimse
        cont := cont + 1
    fimenquanto

    escreva("Somatória dos números impáres: ", soma)

fimalgoritmo
