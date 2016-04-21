algoritmo "Ex.41"
// Função : Mostre todas as possibilidades de 2 dados de forma que a soma
// tenha como resultado 7.
// Obs.: somente valores positivos.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações 
var
         a, cont: inteiro
inicio
        a:=1
        enquanto a < 7 faca
            para cont de 1 ate 7 faca
                se((cont + a)=7)entao
                    escreval(cont, " + ", a, " = 7")
                fimse
            fimpara
            a := a+1
        fimenquanto
fimalgoritmo


