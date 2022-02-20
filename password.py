# Programa em Python 3 para informar a quantidade
# de dígitos necessários para formação de uma senha segura. 
# Para este problema, o módulo 're' de expressões regulares foi utilizado.

import re

def count_char(password):
	'''Função que retorna o número mínimo de caracteres de uma senha a serem digitados, de acordo com um padrão'''
	remaining = 0 # Número de caracteres/dígitos faltantes no início

	# Definindo padrões para achar dígitos, 
	# letras em caixa alta, letras em caixa baixa e 
	# caracteres especiais.
	digit = re.compile("(\\d)")
	lowercase = re.compile("([a-z])")
	uppercase = re.compile("([A-Z])")
	special_char = re.compile("(\\W)")


	# Condicionais para encontrar os padrões acima em uma senha.
	# Caso não encontrado, o número de caracteres/dígitos faltantes
	# é incrementado em uma unidade. 

	# Condicional para verificar dígito
	if not re.search(digit, password):
		remaining += 1

	# Condicional para verificar minúsculas
	if not re.search(lowercase, password):
		remaining += 1

	# Condicional para verificar maiúsculas
	if not re.search(uppercase, password):
		remaining += 1

	# Condicional para verificar caracteres especiais
	if not re.search(special_char, password):
		remaining += 1

	# Condicional para verificar se o comprimento da string é menor que 6
	if (remaining + len(password)) < 6:
		# Número de caracteres a serem adicionados
		remaining = remaining + 6 - (remaining + len(password))

	return print(f'\nO número mínimo de caracteres que devem ser adicionados é {remaining}.')

# Pedindo uma senha para o usuário e informando quantos caracteres 
# ainda são necessários 

if __name__ == "__main__":
	password = input('\nDigite uma senha: ')
	count_char(password)



