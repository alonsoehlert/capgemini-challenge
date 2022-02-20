# Programa em Python 3 para contar pares de 
# substrings que são anagramas

def anagram_substring_count(string):
	'''Retorna o total de substrings anagramas de uma entrada string'''

	# Definindo o comprimento da string que é parâmetro da função
	n = len(string)

	# Definindo um dicionário Python para armazenar substring como 
	# chave e sua contagem de frequência como valor
	substring_map = dict()

	# Definindo número de substrings anagramas inicial
	anagrams = 0

	# loop aninhado no comprimento da string para obter 
	# todas substrings possíveis em ordem alfabética (sorted)
	for i in range(n):
		substring = ''
		for j in range(i, n):

			#Gerando todas substrings possíveis ao longo da string
			substring = ''.join(sorted(substring + string[j]))

			# Armazenando a substring como chave no dicionário Python 
			# e atribuindo valor zero
			substring_map[substring] = substring_map.get(substring, 0)

			# incrementando a contagem no dicionário Python para a chave encontrada
			substring_map[substring] += 1
	
	# loop sobre todos os itens do dicionário de substrings
	# e definindo a contagem de pares de substrings que são anagramas.
	for key, value in substring_map.items():
		# Cálculo do número de pares de substrings de acordo com a contagem de ocorrências
		# Fonte: https://www.hackerrank.com/challenges/sherlock-and-anagrams/forum/comments/120063
		anagrams += (value*(value-1))//2
	return print(anagrams)

# Definindo string e chamando a função
if __name__ == "__main__":
	string = "jiboia"
	anagram_substring_count(string)

