# leitura correta
lista1 = input().split()
lista2 = input().split()

# cálculo correto
valor = (int(lista1[1]) * float(lista1[2])) + (int(lista2[1]) * float(lista2[2]))

# saída formatada
print(f"VALOR A PAGAR: R$ {valor:.2f}")