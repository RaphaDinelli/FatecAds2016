Algoritmo "calculaCombustivel%"
// Descrição   : Calcule a quantidade de litros gastos em uma viagem,
//sabendo que o automóvel faz 12 km/l.
//Receber o tempo de percurso e a velocidade média.
// Autor(a)    : Raphael Dinelli
// Data atual  : 20/02/2016
Var
   t, velocidad : inteiro
   kmPercorrido: real
   
Inicio
   leia(t)
   leia(velocidad)
   kmPercorrido := t * velocidad
   
   escreva("Combustivel gasto", (kmpercorrido/12), " Lts")
   
Fimalgoritmo