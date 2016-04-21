algoritmo "Ex.20"
// Função : Receba 3 coeficientes A, B, e C de uma equação do 2º grau
// da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes
// reais e se caso exista, calcule e mostre.
// (considerar que a equação possue 2 raízes).
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações
var
         a, b, c, d, x1, x2 : real
inicio
         escreval("Digite os 3 coeficientes: ")
         leia(a)
         leia(b)
         leia(c)
         
         d := b^2 - (4*b*c)
         
         x1 := (-(b) + raizq(d)) / (2*a)
         
         x2 := (-(b) - raizq(d)) / (2*a)
         
         escreva("As Raizes são: ", x1, " e", x2)


         
fimalgoritmo
