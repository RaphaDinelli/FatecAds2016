algoritmo "exercicío21"
// Função :  Receba 4 notas bimestrais de um aluno. Calcule e mostre a
// média aritmética. Mostre a mensagem de acordo com a média:
// a. Se a média for >= 6,0 exibir "APROVADO"; b.
// Se a média for >= 3,0 ou < 6,0 exibir "EXAME"; c.
// Se a média for < 3,0 exibir "RETIDO".

// Autor : Raphael Dinelli
// Data : 19/02/2016
// Seção de Declarações
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
