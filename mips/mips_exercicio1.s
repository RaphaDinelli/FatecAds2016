# Fazer, em SPIM, um algoritmo que leia 15 números, a partir de uma estrutura de laço e diga qual o menor 

.data
	msg1: .asciiz"\nDigite um numero inteiro: "
	msg2: .asciiz"\nO menor numero e o: "
.text

main: 
	li $t0, 1
	li $t1, 5
	li $t3, 0
	Enquanto:
		li $v0, 4
		la $a0, msg1
		syscall
		li$v0, 5
		syscall
		add $t2, $v0, $zero
		
		beq $t0, 1, PrimeiroMenor
		blt $t0, $t3, Menor
		add $t0, $t0, 1
		ble $t0, $t1, Enquanto 
		j Fimenquanto
	
	PrimeiroMenor: 
		add $t3, $t2, $zero
		add $t0, $t0, 1
		j Enquanto
	
	Menor:
		add $t3, $t2, $zero
		add $t0, $t0, 1
		j Enquanto 

	Fimenquanto:
		li $v0, 4
		la $a0, msg2
		syscall 
		li $v0, 1
		add $a0, $t3, $zero
		syscall
