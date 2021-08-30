def dia_semana(dia_inicio):
	if dia_inicio.upper() == 'S':
		return False
	elif dia_inicio.upper() in ['SEG', 'SEGUNDA']:
		return ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
	elif dia_inicio.upper() in ['TER', 'TERÇA', 'TERCA']:
		return ['Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom', 'Seg']
	elif dia_inicio.upper() in ['QUA', 'QUARTA']:
		return ['Qua', 'Qui', 'Sex', 'Sab', 'Dom', 'Seg', 'Ter']
	elif dia_inicio.upper() in ['QUI', 'QUINTA']:
		return ['Qui', 'Sex', 'Sab', 'Dom', 'Seg', 'Ter', 'Qua']
	elif dia_inicio.upper() in ['SEX', 'SEXTA']:
		return ['Sex', 'Sab', 'Dom', 'Seg', 'Ter', 'Qua', 'Qui']
	elif dia_inicio.upper() in ['SAB', 'SABADO']:
		return ['Sab', 'Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex']
	elif dia_inicio.upper() in ['DOM', 'DOMINGO']:
		return ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
	else:
		return None


lista = ''
count = 1

while(True):
	dia_inicio = input("Dia início (ex.: Sabado) - Digite 's' para sair\n")
	dia = dia_semana(dia_inicio)

	if dia is False:
		print('Saindo do sistema...')
		break

	elif dia is None:
		print('Inválido!')
		continue

	else:
		separador = input('Separador\n')
		for k in range(5):
			lista += f'{dia[0]}{k+count}{separador}'
			lista += f'{dia[1]}{k+count+1}{separador}'
			lista += f'{dia[2]}{k+count+2}{separador}'
			lista += f'{dia[3]}{k+count+3}{separador}'
			lista += f'{dia[4]}{k+count+4}{separador}'
			lista += f'{dia[5]}{k+count+5}{separador}'
			lista += f'{dia[6]}{k+count+6}{separador}'
			count += 6

		print(lista)
		break