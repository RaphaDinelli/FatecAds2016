Algoritmo "trocaValor"
// Descrição   : Receba os valores em x e y.
//Efetua a troca de seus valores e mostre seus conteúdos.
// Autor(a)    : Raphael Dinelli
// Data atual  : 20/02/2016
Var
   x, y, troca : inteiro

Inicio
   leia(x)
   escreval("x = ", x)
   leia(y)
   escreval("y = ", y)
   escreval("Troca de valores:")
   troca := x
   x := y
   y := troca
   escreval("x = ",x)
   escreva("y = ",y)


Fimalgoritmo