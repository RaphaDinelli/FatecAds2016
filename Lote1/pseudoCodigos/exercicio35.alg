algoritmo "Ex.35"
// Fun��o : Receba 2 n�meros inteiros, verifique qual o maior entre eles.
// Calcule e mostre o resultado da somat�ria dos n�meros �mpares entre
// esses valores.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es 
var
         num1, num2, maior, menor, soma, cont : inteiro
inicio
    escreva ("Digite um n�mero:  ")
       leia (num1)
    escreva ("Digite um n�mero:  ")
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

    escreva("Somat�ria dos n�meros imp�res: ", soma)

fimalgoritmo
