Algoritmo "cauculaJurosPoupan�a"
// Descri��o   : Receba o valor de um dep�sito em poupan�a.
//Calcule e mostre o valor ap�s 1 m�s de aplica��o sabendo
//que rende 1,3% a. m.
// Autor(a)    : Raphael Dinelli
// Data atual  : 20/02/2016
Var
   deposito, rendimento : real

Inicio
   leia(deposito)
   rendimento := deposito * 0.013
   
   escreval("Ap�s um m�s de aplica��o voc� ter�: ", (deposito + rendimento))



Fimalgoritmo