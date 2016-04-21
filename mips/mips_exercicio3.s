.data
	msg1: .asciiz"\nDigite a nota da P1: "
	msg2: .asciiz"\nDigite a nota da P2: "
	msg3: .asciiz"\nDigite a nota do trabalho: "
	msg4: .ascii"\n A media e : "
.text
main: 
	#leitura da P1
	li $v0, 4
	la $a0, msg1
	syscall
	li $v0, 6
	syscall
	mov.s $f1, $f0
	
	#Leitura da P2
	li $v0, 4
	la $a0, msg2
	syscall
	li $v0, 6
	syscall
	mov.s $f2, $f0

	#Leitura do trabalho
	li $v0, 4
	la $a0, msg3
	syscall
	li $v0, 6
	syscall
	mov.s $f3, $f0
	
	li.s $f4, 0.3
	mul.s $f1, $f1, $f4
	li.s $f4, 0.5
	mul.s $f2, $f2, $f4
	li.s $f4, 0.2
	mul.s $f3, $f3, $f4
	
	add.s $f1, $f1, $f2
	add.s $f1, $f1, $f3

	li $v0, 4
	la $a0, msg4
	syscall
	li $v0, 2
	mov.s $f12, $f1
	syscall
	li $v0, 10
	syscall
	