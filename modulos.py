##Programa de calculo de notas, feito por ##Victor Smirnov RA1800337


## Função que checa se frequencia está dentro do intervalo e se é um ponto flutuante
def ChecaFreq(freq):
	if isinstance(freq, float) == False: ##Pergunta se a frequencia está dentro do intervalo e se é um número.
		raise ValueError("Erro no Parâmetro freq: O Valor inserido não é flutuante")
	elif freq < 0 or freq > 1:
		raise ValueError("Erro no Parâmetro freq: O Valor inserido não está entre o resultado de 0 a 1.")
	else:
		return 


## Função que coleta as notas da ACs
#def ColetaAcs(acs):

#	for k, i in enumerate(acs):
#		print(k)
#		acs[k] = float(input("Digite a Nota da AC:"))
#	return(acs)


## Função que checa se as Notas de ACs está dentro do intervalo e se é um ponto flutuante

def ChecaAcs(acs):

##Pergunta se a nota está dentro do intervalo e se é um número.
	for k, i in enumerate(acs):
		if acs[k] not in range (-1, 11):
		
			raise ValueError("Erro no Parâmetro acs no indice", k,"O Valor inserido não está entre o resultado de 0 a 1.")	
	else:
		return

## Calcula a Média das ACs

def MediaAcs(acs):
	acs.sort(reverse = True) ## Ordena os elementos da lista
	acs.pop(9) ##Remove o menor Indice
	acs.pop(8) ##Remove o segundo menor Indice
	acs.pop(7) ##Remove o terceiro menor Indice
	print(acs)
	media = sum(acs) / 7 ## Calcula Média
	return media

## Calcula a Média Geral

def MediaGeral(acs, prova, pai, extra):
	
	v_media_acs = MediaAcs(acs) ##Recebe as 
	print(v_media_acs)
	##Verifica se o Aluno tem nota do PAI
	if pai == 0:
		media = (v_media_acs * 0.6) + (prova * 0.4) + extra	
	else:
		media = (v_media_acs * 0.5) + (prova * 0.3) + (pai * 0.2) + extra	
	return media

## Função que checa se a nota da Prova está dentro do intervalo e se é um ponto flutuante
def ChecaProva(prova):
	if isinstance(prova, float) == False: ##Pergunta se a frequencia está dentro do intervalo e se é um número.
		raise ValueError("Erro no Parâmetro prova: O Valor inserido não é flutuante")
	if prova not in range (-1, 11):
		raise Exception("Erro no Parâmetro prova: O Valor inserido não está entre o resultado de 0 a 10.")
	else:
		return 

## Função que checa se a nota da Prova Substitutiva está dentro do intervalo e se é um ponto flutuante
def ChecaSub(sub):
	if isinstance(sub, float) == False: ##Pergunta se a frequencia está dentro do intervalo e se é um número.
		raise ValueError("Erro no Parâmetro sub: O Valor inserido não é flutuante")
	if sub not in range (-1, 11):
		raise Exception("Erro no sub: O Valor inserido não está entre o resultado de 0 a 10.")
	else:
		return 

## Função que checa se a nota Extra está dentro do intervalo e se é um ponto flutuante
def ChecaExtra(extra):
	if isinstance(extra, float) == False: ##Pergunta se a frequencia está dentro do intervalo e se é um número.
		raise ValueError("Erro no Parâmetro extra: O Valor inserido não é flutuante")
	if extra not in range (-1, 11):
		raise Exception("Erro no Parâmetro Extra: O Valor inserido não está entre o resultado de 0 a 10.")
	else:
		return 

## Função que checa se a nota do Pai está dentro do intervalo e se é um ponto flutuante
def ChecaPai(pai):
	if isinstance(pai, float) == False: ##Pergunta se a frequencia está dentro do intervalo e se é um número.
		raise ValueError("Erro no Parâmetro pai: O Valor inserido não é flutuante")
	if pai not in range (-1, 11):
		raise Exception("Erro no Parâmetro pai: O Valor inserido não está entre o resultado de 0 a 10.")
	else:
		return 

##Checa se o aluno foi aprovado
def ChecaAprova(freq, media_geral):
    motivo = []
    aprovacao =	{"Aprovado": False, "Motivo": motivo}
    if freq > 0.75 and media_geral < 6:
        motivo.append ("Nota")
    elif freq < 0.75 and media_geral > 6:
        motivo.append = ("Faltas")
    elif freq < 0.75 and media_geral < 6:
        motivo.append = ("Nota")
        motivo.append = ("Faltas")
    else:
        aprovacao["Aprovado"] = True
    return aprovacao