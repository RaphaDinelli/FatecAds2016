algoritmo "Ex.20"
// Fun��o : Receba 3 coeficientes A, B, e C de uma equa��o do 2� grau
// da f�rmula AX�+BX+C=0. Verifique e mostre a exist�ncia de ra�zes
// reais e se caso exista, calcule e mostre.
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
