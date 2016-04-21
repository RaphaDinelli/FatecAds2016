Algoritmo "cauculaJurosPoupança"
// Descrição   : Receba o valor de um depósito em poupança.
//Calcule e mostre o valor após 1 mês de aplicação sabendo
//que rende 1,3% a. m.
// Autor(a)    : Raphael Dinelli
// Data atual  : 20/02/2016
Var
   deposito, rendimento : real

Inicio
   leia(deposito)
   rendimento := deposito * 0.013
   
   escreval("Após um mês de aplicação você terá: ", (deposito + rendimento))



Fimalgoritmo