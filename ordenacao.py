def quick_sort(valores):
	if len(valores) <= 1:
		# Se a lista ter apenas 0 ou 1 elemento, significa que já está ordenada, retornando a própria lista.
		return valores

	pivo = valores[len(valores) // 2]
	# O pivo seria o elemento do meio da lista, que vai ser utilizado para dividir a lista em três partes.
	menores = [valor for valor in valores if valor < pivo]
	# Menores será os valores menores que o pivo.
	iguais = [valor for valor in valores if valor == pivo]
	# Iguais será os valores iguais ao pivo.
	maiores = [valor for valor in valores if valor > pivo]
	# Maiores será os valores maiores que o pivo.

	return quick_sort(menores) + iguais + quick_sort(maiores)
    # Ele retorna a lista ordenada, chamando a função quick_sort para os menores e maiores, e concatenando com os iguais.

print(quick_sort([7, 3, 9, 1, 5]))