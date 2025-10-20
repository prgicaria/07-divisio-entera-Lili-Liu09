divident = int(input("Entra el divident: "))
divisor = int(input("Entra el divisor: "))

quocient = divident//divisor
residu = divident-(divisor*quocient)

print(f"Divisió:{divident}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")