algoritmo "Ex.39"
// Fun��o : Calcule a quantidade de gr�os contidos em um tabuleiro de xadrez
// onde: Casa:  1 2 3 4 ... 64 Qte: 1 2 4 8 ... N
// Obs.: somente valores positivos.
// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es 
var
         casa, grao, total : inteiro
inicio
    casa := 1
    enquanto casa <= 8 faca
        escolha casa
            caso 1
                grao := 1
                total := total + grao
                grao := grao + 1
            outrocaso
                grao := grao + grao
                total := total + grao
        fimescolha
        casa := casa + 1
    fimenquanto
    escreva("Resultado: ", total)



fimalgoritmo

