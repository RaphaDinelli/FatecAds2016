algoritmo "Ex.43"
// Função : Calcule e mostre quantos anos serão necessários para que Ana
// seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e
// Maria tem 1,5 m e cresce 2 cm ao ano.
// Data : 19/02/2016
// Seção de Declarações 
var
         anaAno, maria, ana: real
inicio
        ana := 1.10
        maria := 1.5
        
        enquanto ana < maria faca
            ana := ana + 0.03
            maria := maria + 0.02
            anaAno := anaAno +1
        fimenquanto
        escreval("Ana levou ", anaAno, " anos, para utrapassar Maria.")
fimalgoritmo


