import math
r = float(input("Digite o raio do cilindro: "))
h = float(input("Digite a altura do cilindro: "))
vol = math.pi * pow(r,2) * h

print("----------------------------------")
print(f"O volume do cilindro é {vol:.2f}")