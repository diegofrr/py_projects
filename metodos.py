import re
from database import *


def procurar_matricula(matricula):
	alunos_encontrados = []
	for aluno in lista_alunos:
		if matricula in aluno.matricula:
			alunos_encontrados.append(aluno)
	if len(alunos_encontrados) == 0:
		return None, False
	else:
		return alunos_encontrados, True
		

def procurar_nome(nome):
	alunos_encontrados = []
	for aluno in lista_alunos:
		if nome.upper() in aluno.nome:
			alunos_encontrados.append(aluno)

	if len(alunos_encontrados) == 0:
		return None, False
	else:
		return alunos_encontrados, True



def quant_alunos():
	return len(lista_alunos)