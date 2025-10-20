dividend = int(input("Entra el dividend: "))
divisor = int(input("Entra el divisor: "))

quocient = dividend//divisor
residu = dividend-(divisor*quocient)

print(f"Divisió:{dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")