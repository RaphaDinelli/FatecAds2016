algoritmo "Ex.5"
// Fun��o : Receba os coeficientes A, B e C de uma equa��o do
// 2� grau (AX�+BX+C=0). Calcule e mostre as ra�zes reais
// (considerar que a equa��o possue 2 ra�zes).
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es
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
         
         escreva("As Raizes s�o: ", x1, " e", x2)


         
fimalgoritmo
