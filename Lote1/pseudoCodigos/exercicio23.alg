algoritmo "numerosEmOrdemCrescente"
// Fun��o : Receba 3 inteiros em ordem crescente e mais um em qualquer ordem
// mostre os 4 n�meros em ordem crescente.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es
var
         a, b, c, d : inteiro
inicio
         escreval("Digite tres n�meros em ordem crescente")
         leia(a)
         leia(b)
         leia(c)
         escreval("Digite um n�mero em qualquer ordem")
         leia(d)
         se(d < a) entao
              escreva(d, a, b, c)
         senao
              se (d < b) entao
                 escreva(a, d, b, c)
              senao
                 se(d < c) entao
                      escreva(a, b, d, c)
                 senao
                      escreva(a, b, c, d)
                 fimse
         fimse
         fimse
fimalgoritmo
