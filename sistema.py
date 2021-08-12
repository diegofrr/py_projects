from metodos import *
from importar import *

while True:
	menu = input(f'''1. PROCURAR ALUNO(A) PELO NOME
2. PROCURAR ALUNO(A) PELA MATRÍCULA
3. Nº DE ALUNOS CADASTRADOS
4. SAIR
''')


	#PROCURAR ALUNO(A) PELO NOME
	if menu == '1':
		nome = input('Digite o nome\n')
		alunos_encontrados, encontrou = procurar_nome(nome)
		if encontrou:
			lista_nomes = ''
			for aluno in alunos_encontrados:
				lista_nomes += f'{aluno.toString()} \n'
			print(f'{len(alunos_encontrados)} aluno(s) encontrado(s): \n{lista_nomes}')
		else:
			print('Nenhum aluno encontrado\n')


	#PROCURAR ALUNO(A) PELA MATRÍCULA	
	elif menu == '2':
		matricula = input('Digite a matrícula\n')
		alunos_encontrados, encontrou = procurar_matricula(matricula)
		if encontrou:
			lista_nomes = ''
			for aluno in alunos_encontrados:
				lista_nomes += f'{aluno.toString()} \n'
			print(f'{len(alunos_encontrados)} aluno(s) encontrado(s): \n{lista_nomes}')
		else:
			print('Nenhum aluno encontrado\n')


	elif menu == '3':
		print(f'Existem {quant_alunos()} alunos cadastrados no sistema.\n')


	#SAINDO DO SISTEMA
	elif menu == '4':
		print('Saindo do sistema')
		break


	#CASO NENHUMA OPÇÃO SEJA EQUIVALENTE AS ANTERIORES O SISTEMA CONTINUA NO LOOP
	else:
		print('Opção inválida!')