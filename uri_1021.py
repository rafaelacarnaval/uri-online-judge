n = float(input())

notas = [100,50,20,10,5,2]
moedas = [1,0.50,0.25,0.10,0.05,0.01]

print("NOTAS:")
for nota in notas:
    quantidade = n / nota

    print("%d nota(s) de R$ %d.00" %(quantidade, nota))

    n = n % nota

print("MOEDAS:")
for moeda in moedas:
    quantidade = n / moeda

    print("%d moeda(s) de R$ %.2f" %(quantidade, moeda))

    n = round((n % moeda),2)
