algoritmo "exercicío29"
// Função :  Receba o tipo de investimento (1 = poupança e 2 = renda fixa)
// e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias
// sabendo que a poupança = 3% e a renda fixa = 5%.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações
var
         invest : inteiro
         val : real
         cor: real
         
inicio
         escreval("Digite o tipo de investmento, 1 para Poupança e 2 para renda fixa: ")
         leia(invest)
         escreval("Digite o valor do investimento: ")
         leia(val)
         
         se(invest > 1) entao
             cor := 0.05
         senao
             cor := 0.03
         fimse
         

         escreval("Rendimento em 30 dias: ", (val + (val * cor)))

         
fimalgoritmo
