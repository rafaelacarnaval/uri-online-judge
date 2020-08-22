valor = int(input())

notas = [100,50,20,10,5,2,1]
cont = 0

print(valor)


while valor >= 0 and cont < len(notas):
    if valor >= notas[cont]:
        resto = valor % notas[cont]
        valor2 = valor - resto
        quant = valor2 / notas[cont]

        print("%d nota(s) de R$ %d,00" %(quant,notas[cont]))

        valor = resto
        cont += 1
        
    else:
        print ("0 nota(s) de R$ %d,00" %(notas[cont]))
        cont += 1


