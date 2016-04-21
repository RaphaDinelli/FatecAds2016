algoritmo "Ex.32"
// Função : Receba um número inteiro. Calcule e mostre o seu fatorial.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         num, cont, mult : inteiro
inicio
    escreva ("Digite um número:  ")
       leia (num)

       para cont de num ate 2 passo -1 faca
                se (cont = num) entao
                    mult := cont * (cont - 1)

                fimse

                se (cont < num) e (cont <> 1)  entao
                     mult <- mult * (cont - 1)
                fimse
        fimpara
                escreval ("O fatorial de ", num, " é: ", mult)

fimalgoritmo
