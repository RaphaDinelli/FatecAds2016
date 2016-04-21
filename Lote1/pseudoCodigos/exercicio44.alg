algoritmo "Ex.44"
// Função : Receba o número da base e do expoente. Calcule e mostre o valor
// da potência .
// Data : 19/02/2016
// Seção de Declarações 
var
         base, expo,cont, total: inteiro
inicio
         escreval("Digite a base e o expoente: ")
         leia(base)
         leia(expo)
         cont:= 1
         enquanto cont < expo faca
             se (total < 1) entao
                total := base * base
                    cont := cont+1
             senao
                total := total * base
                cont := cont + 1
             fimse
         fimenquanto
         escreva("Resultado: ", total)

fimalgoritmo



