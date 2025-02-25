x = 1
total = 0
i = 1

print("**** Lojas Luiz ****")
while x != 0:
    x = float(input(f"Produto {i}: "))
    total += x
    i += 1
print("************")
print(f"Total: R${total:.2f}")
dinheiro = float(input("Dinheiro: "))
troco = dinheiro - total
print(f"Troco: R${troco:.2f}")
