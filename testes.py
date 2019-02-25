##Programa de calculo de notas, feito por ##Victor Smirnov RA1800337
from nota import *
from modulos import *

def menu():
	print ("""Bem vindo ao programa de teste do módulo de nota, informe o teste que você gostaria de realizar
				1 - Aprovado: Frequência, Prova e ACS.
				2 - Aprovado: Frequência, Avaliação Substitutiva, Prova e ACs
				3 - Aprovado: Frequência, Prova, PAI e Extra
				4 - Reprovado: Frequência
				5 - Reprovado: Notas
				6 - Reprovado: Frequência e Notas
				7 - Teste Customizado
				Outra opção - Sair""")

	opcao = int(input("Opçâo:  "))
	if opcao == 1:
		##Primeiro teste, deve mostrar o Aluno como "Aprovado", sem PAI, sem Nota Extra e Sem Avaliação Substitutiva
		##Coleta a Frequencia
		freq = 1.0
		##Coleta os valores das ACs e os Testa
		acs = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
		##Coleta a Prova
		prova = 10.0
		##Coleta a Prova Substitutiva
		sub = 0.0
		##Coleta a Nota Extra
		extra = 0.0 
		##Coleta o PAI
		pai = 0.0
		aluno_aprovado(freq, acs, prova, sub, pai, extra)
	elif opcao == 2:
		##Segundo teste, deve mostrar o Aluno como "Aprovado", sem PAI, sem Nota Extra e com Avaliação Substitutiva
		##Coleta a Frequencia
		freq = 1.0
		##Coleta os valores das ACs e os Testa
		acs = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
		##Coleta a Prova
		prova = 3.0
		##Coleta a Prova Substitutiva
		sub = 10.0
		##Coleta a Nota Extra
		extra = 0.0 
		##Coleta o PAI
		pai = 0.0
		aluno_aprovado(freq, acs, prova, sub, pai, extra)
	elif opcao == 3:
		##Terceiro teste, deve mostrar o Aluno como "Aprovado", com PAI, com Nota Extra e sem Avaliação Substitutiva
		##Coleta a Frequencia
		freq = 1.0
		##Coleta os valores das ACs e os Testa
		acs = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
		##Coleta a Prova
		prova = 5.0
		##Coleta a Prova Substitutiva
		sub = 0.0
		##Coleta a Nota Extra
		extra = 1.0 
		##Coleta o PAI
		pai = 10.0
		aluno_aprovado(freq, acs, prova, sub, pai, extra)
	if opcao == 4:
		##Quarto teste, deve mostrar o Aluno como "Reprovado" por falta
		##Coleta a Frequencia
		freq = 0.1
		##Coleta os valores das ACs e os Testa
		acs = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
		##Coleta a Prova
		prova = 10.0
		##Coleta a Prova Substitutiva
		sub = 0.0
		##Coleta a Nota Extra
		extra = 0.0 
		##Coleta o PAI
		pai = 0.0
		aluno_aprovado(freq, acs, prova, sub, pai, extra)
	if opcao == 5:
		##Quinto teste, deve mostrar o Aluno como "Reprovado" por Notas
		##Coleta a Frequencia
		freq = 0.8
		##Coleta os valores das ACs e os Testa
		acs = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
		##Coleta a Prova
		prova = 5.0
		##Coleta a Prova Substitutiva
		sub = 0.0
		##Coleta a Nota Extra
		extra = 0.0 
		##Coleta o PAI
		pai = 0.0
		aluno_aprovado(freq, acs, prova, sub, pai, extra)
	if opcao == 6:
		##Sexto teste, deve mostrar o Aluno como "Reprovado" por Notas e faltas
		##Coleta a Frequencia
		freq = 0.3
		##Coleta os valores das ACs e os Testa
		acs = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
		##Coleta a Prova
		prova = 5.0
		##Coleta a Prova Substitutiva
		sub = 0.0
		##Coleta a Nota Extra
		extra = 0.0 
		##Coleta o PAI
		pai = 0.0
		aluno_aprovado(freq, acs, prova, sub, pai, extra)
	if opcao == 7:
		##Teste Personalizado
		##Coleta a Frequencia
		freq = float(input("Digite a frequência: "))
		##Coleta os valores das ACs e os Testa
		for k, i in enumerate(acs):
			print(k)
			acs[k] = float(input("Digite a Nota da AC:"))
		##Coleta a Prova
		prova = float(input("Digite a nota da prova: "))
		##Coleta a Prova Substitutiva
		sub = float(input("Digite a nota da prova substitutiva: "))
		##Coleta a Nota Extra
		extra = float(input("Digite a nota extra: "))
		##Coleta o PAI
		pai = float(input("Digite a nota do pai: "))
		aluno_aprovado(freq, acs, prova, sub, pai, extra)
	else:
		repete = False
	return repete

repete = True
while repete:
	repete = menu()


