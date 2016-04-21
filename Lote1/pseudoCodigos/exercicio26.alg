algoritmo "exercicío26"
// Função : Receba 2 números inteiros.
// Verifique e mostre se o maior número é múltiplo do menor.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações
var
         a, b : inteiro
inicio
         escreval("Digite 2 número inteiro: ")
         leia(a)
         leia(b)

         se (a > b)  entao
            se (a % b = 0) entao
               escreva(a, " é multiplo por ", b)
            fimse
         senao
            se(b % a = 0) entao
                 escreva(b, " é multiplo por ", a)
            fimse
         fimse
         
fimalgoritmo
