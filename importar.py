from aluno import Aluno
from database import *

file = open('alunos.txt', 'r')

for linha in file.readlines():

	nome = linha.split(';')[1].replace('\n', '')
	matricula = linha.split(';')[0]
	lista_alunos.append(Aluno(nome, matricula))