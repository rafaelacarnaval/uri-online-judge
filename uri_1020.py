n = int(input())

anos = n / 365
n = n % 365
meses = n / 30
n = n % 30


print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(anos, meses, n))
