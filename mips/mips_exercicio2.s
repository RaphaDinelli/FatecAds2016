.data
	msg1: .asciiz"\nDigite um numero\n"
	msg2: .asciiz"\n é par."
	msg3: .asciiz"\n é impar."
.text

main:
	li $v0, 4
	la $a0, msg1
	syscall
	
	li $v0, 5
	syscall
	add, $t0, $v0, $zero

	rem $t1, $t0, 2
	bgt $t1, 0, Impar
	j Par

	Impar:
	li $v0, 1
	add $a0, $t0, $zero
	syscall 

	li $v0, 4
	la $a0, msg3
	syscall
	j Fim

	Par:
	li $v0, 1
	add $a0, $t0, $zero
	syscall
	
	li $v0, 4
	la $a0, msg2
	syscall
	
	Fim:
	li $v0, 10
	syscall
	