algoritmo "Ex.42"
// Fun��o : Calcule e mostre a s�rie 1 + 2/3 + 3/5 + ... + 50/99
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es 
var
         a, b, total: real
inicio
        a := 2
        b := 3
        total := (a / b+1)
        escreval("1 + ", a, " / ", b, " = ", total, " + ")
        
        enquanto b < 99 faca
            a:= a + 1
            b:= b + 2
            total:= total + (a / b)
            escreval(a, " / ", b, " = ", total, " + ")
        fimenquanto

fimalgoritmo


