algoritmo "exercic�o21"
// Fun��o :  Receba 4 notas bimestrais de um aluno. Calcule e mostre a
// m�dia aritm�tica. Mostre a mensagem de acordo com a m�dia:
// a. Se a m�dia for >= 6,0 exibir "APROVADO"; b.
// Se a m�dia for >= 3,0 ou < 6,0 exibir "EXAME"; c.
// Se a m�dia for < 3,0 exibir "RETIDO".

// Autor : Raphael Dinelli
// Data : 19/02/2016
// Se��o de Declara��es
var
         a, b, c, d, m: real
inicio
         escreval("Digite as 4 notas: ")
         leia(a)
         leia(b)
         leia(c)
         leia(d)
         
         m := (a+b+c+d) / 4
            se (m > 6 ) entao
                escreva("APROVADO")
            senao
                se(m > 3) entao
                    escreva("EXAME")
                senao
                    escreva("RETIDO")
                fimse
            fimse
         
fimalgoritmo
