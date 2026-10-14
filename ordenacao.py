def quick_sort(valores):
	if len(valores) <= 1:
		return valores

	pivo = valores[len(valores) // 2]
	menores = [valor for valor in valores if valor < pivo]
	iguais = [valor for valor in valores if valor == pivo]
	maiores = [valor for valor in valores if valor > pivo]

	return quick_sort(menores) + iguais + quick_sort(maiores)