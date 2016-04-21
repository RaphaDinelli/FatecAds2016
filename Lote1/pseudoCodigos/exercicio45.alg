algoritmo "Ex.45"
// Função : Calcule e mostre a série 1 - 2/4 + 3/9 - 4/16 + 5/25 + ... + 15/225
// Data : 19/02/2016
// Seção de Declarações 
var
         a, b, total: real
inicio
         a := 2
         b := a * a
         
         total := 1 - (a / b) + ((a+1)/ ((a+1)^2))
         
         escreval("1 - ", a,"/",b, " + ",(a+1),"/",((a+1)^2), " = ", total)
         
         enquanto a < 14 faca
            a:= a+1
            b:= a * a
            total := total - (a / b) + ((a+1)/ ((a+1)^2))
            escreval("- ", a,"/",b, " + ",(a+1),"/",((a+1)^2), " = ", total)
         fimenquanto
fimalgoritmo



