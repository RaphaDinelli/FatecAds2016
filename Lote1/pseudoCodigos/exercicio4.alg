Algoritmo "ConverteFahreiheit%"
// Descrição   : Receba o salário de um funcionário e mostre o novo salário
//com reajuste de 15%.Receba a temperatura em graus Celsius. Calcule e
//mostre a sua temperatura convertida em fahrenheit (F = (9*C+160)/5.
// Autor(a)    : Raphael Dinelli
// Data atual  : 20/02/2016
Var
   celcius, fahrenheit : real

Inicio
   leia(celcius)
   fahrenheit := (9*celcius+160)/5
   escreva("Fahrenheit: ", fahrenheit)


Fimalgoritmo