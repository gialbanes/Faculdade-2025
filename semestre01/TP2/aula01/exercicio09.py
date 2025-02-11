brancos = int(input("Digite a quantidade de votos brancos: "))
nulos = int(input("Digite a quantidade de votos nulos: "))
validos = int(input("Digite a quantidade de votos válidos: "))

totalEleitores = brancos + nulos + validos

percBrancos = (brancos * 100) / totalEleitores
percNulos = (nulos * 100) / totalEleitores
percValidos = (validos * 100) / totalEleitores

print("---------------------------------------")
print(f"O número de votos brancos é {brancos}")
print(f"O número de votos nulos é {nulos}")
print(f"O número de votos válidos é {validos}")

print("---------------------------------------")
print(f"O número total de eleitores é {totalEleitores}")

print("---------------------------------------")
print(f"O percentual de votos brancos é {percBrancos}")
print(f"O percentual de votos nulos é {percNulos}")
print(f"O percentual de votos válidos é {percValidos}")