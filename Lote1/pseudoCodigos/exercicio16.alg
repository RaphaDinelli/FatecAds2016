Algoritmo "calculaSalario"
// Descri��o   :  Receba a quantidade de horas trabalhadas,
//o valor por hora, o percentual de desconto e o n�mero de descendentes.
//Calcule o sal�rio que ser�o as horas trabalhadas x o valor por hora.
//Calcule o sal�rio l�quido (= Sal�rio Bruto - desconto).
//A cada dependente ser� acrescido R$ 100 no Sal�rio L�quido.
//Exiba o sal�rio a receber.
// Autor(a)    : Raphael Dinelli
// Data atual  : 20/02/2016
Var
   horas, valor, desconto, desc, salario, salarioLiquido : real
   
Inicio
   leia(horas)
   leia(valor)
   leia(desconto)
   leia(desc)
   
   salario := horas * valor
   desconto := (desconto / 100)* salario
   salarioLiquido := salario - desconto + (desc * 100)
   
   escreva(salarioLiquido)
   
   
   



Fimalgoritmo