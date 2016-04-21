Algoritmo "calculaSalario"
// Descrição   :  Receba a quantidade de horas trabalhadas,
//o valor por hora, o percentual de desconto e o número de descendentes.
//Calcule o salário que serão as horas trabalhadas x o valor por hora.
//Calcule o salário líquido (= Salário Bruto - desconto).
//A cada dependente será acrescido R$ 100 no Salário Líquido.
//Exiba o salário a receber.
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