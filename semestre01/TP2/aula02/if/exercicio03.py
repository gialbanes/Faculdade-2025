pessoa1 = float(input("Digite a altura da primeira pessoa: "))
pessoa2 = float(input("Digite a altura da segunda pessoa: "))
pessoa3 = float(input("Digite a altura da terceira pessoa: "))

array = [pessoa1, pessoa2, pessoa3]
array.sort(reverse=True)
print(array)