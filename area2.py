# Ввод строк
s1 = "AGGTAB"
s2 = "GXTXAYB"

# Длина строк
m = len(s1)
n = len(s2)

# Создание двумерного массива для хранения длин LCS
# (m+1) x (n+1), так как учитываем пустые строки
L = [[0] * (n + 1) for i in range(m + 1)]

# Заполнение массива L
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:  # Если символы равны
            L[i][j] = L[i - 1][j - 1] + 1
        else:
            L[i][j] = max(L[i - 1][j], L[i][j - 1])  # Если не равны

# Длина наибольшей общей последовательности
length_of_lcs = L[m][n]

# Восстановление самой последовательности
lcs = []
i, j = m, n
while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:  # Если символы равны
        lcs.append(s1[i - 1])  # Добавляем символ в результат
        i -= 1
        j -= 1
    elif L[i - 1][j] > L[i][j - 1]:  # Двигаемся в сторону большего значения
        i -= 1
    else:
        j -= 1

# Обратим последовательность, так как мы собирали её с конца
lcs.reverse()

# Вывод результата
print("Длина LCS:", length_of_lcs)
print("Наибольшая общая последовательность:", ''.join(lcs))
