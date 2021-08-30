import requests


nome_procurar = input('Nome do deputado\n')
r = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados?nome=' + nome_procurar)


lista_dados = r.json().get('dados')

if (len(lista_dados) == 0):
	print('Nenhum deputado encontrado')

for deputado in lista_dados:
	nome = deputado.get('nome')
	siglaPartido = 'Não cadastrado'
	if (deputado.get('siglaPartido') is not None):
		siglaPartido = deputado.get('siglaPartido')
	siglaUF = deputado.get('siglaUf')
	email = 'Não cadastrado'

	if (deputado.get('email') is not None):
		email = deputado.get('email')

	print(
		f'{nome}, Partido: {siglaPartido}\n'
		f'UF: {siglaUF}\n'
		f'E-mail: {email}\n'
		)

if (len(lista_dados) > 0):
	print(f'Foram encontrados {len(lista_dados)} deputados com o nome {nome_procurar}.')
