algoritmo "Ex.5"
// Função : Receba os coeficientes A, B e C de uma equação do
// 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais
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
