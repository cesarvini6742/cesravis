altura1 = float(input("Digite a primeira altura: "))
altura2 = float(input("Digite a segunda altura: "))
altura3 = float(input("Digite a terceira altura: "))

if altura1 == altura2 or altura1 == altura3 or altura2 == altura3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")
else:
    maior = max(altura1, altura2, altura3)
    print(f"A maior estatura é {maior} m")
