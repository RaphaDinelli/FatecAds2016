algoritmo "Ex.44"
// Fun��o : Receba o n�mero da base e do expoente. Calcule e mostre o valor
// da pot�ncia .
// Data : 19/02/2016
// Se��o de Declara��es 
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



