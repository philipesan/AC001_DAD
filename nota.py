##Programa de calculo de notas, feito por ##Victor Smirnov RA1800337

from modulos import *
##Função que deverá ser entregue

def aluno_aprovado(freq, acs, prova, sub, pai, extra):
	aprovacao = {}
	ChecaFreq(freq)
	ChecaAcs(acs)
	ChecaProva(prova)
	ChecaSub(sub)
	ChecaPai(pai)
	ChecaExtra(extra)
	media_geral = MediaGeral(acs, prova, pai, extra)
	aprovacao = ChecaAprova(freq, media_geral)
	print(aprovacao)

