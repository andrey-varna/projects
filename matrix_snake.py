# Таблица размером  n×n, заполненная числами от 1 до n по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке.

n = int(input())
s = []
for i in range(n):
    s.append([0] * n )
tot = 1
for i in range(1):
    for j in range(n):
        s[i][j] = tot
        tot += 1
m = 1
while n > 1and n >= m:
    for i in range(m, n):
        s[i][n - 1] = tot
        tot += 1
    for i in range(n - 2, - 2 + m, -1):
        s[n - 1][i] = tot
        tot += 1

    for i in range(n - 2, m -1, -1):
        s[i][-1+m] = tot
        tot += 1

    for i in range(m,n - 1):
        s[m][i] = tot
        tot += 1
    n -= 1
    m += 1
for i in s:
    print(*i)
