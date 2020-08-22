peca1 = input().split(" ")
peca2 = input().split(" ")

codigo = int(peca1[0])
numero = int(peca1[1])
valor = float(peca1[2])

codigo2 = int(peca2[0])
numero2 = int(peca2[1])
valor2 = float(peca2[2])

total = (numero * valor) + (numero2 * valor2)

print("VALOR A PAGAR: R$ %.2f" %total)
