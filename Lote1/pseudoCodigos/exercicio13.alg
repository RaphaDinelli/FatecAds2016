Algoritmo "consumoAlimento"
// Descrição   :  Receba a quantidade de alimento em quilos.
// Calcule e mostre quantos dias durará esse alimento sabendo
// que a pessoa consome 50g ao dia.
// Autor(a)    : Raphael Dinelli
// Data atual  : 20/02/2016
Var
   alimento, dias : real
   
   

Inicio
   leia(alimento)
   alimento := (alimento * 1000)
   dias := (alimento / 50)
   escreval(dias)



Fimalgoritmo