algoritmo "exercic�o26"
// Fun��o : Receba 2 n�meros inteiros.
// Verifique e mostre se o maior n�mero � m�ltiplo do menor.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es
var
         a, b : inteiro
inicio
         escreval("Digite 2 n�mero inteiro: ")
         leia(a)
         leia(b)

         se (a > b)  entao
            se (a % b = 0) entao
               escreva(a, " � multiplo por ", b)
            fimse
         senao
            se(b % a = 0) entao
                 escreva(b, " � multiplo por ", a)
            fimse
         fimse
         
fimalgoritmo
