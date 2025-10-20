dividend = int(input("Quin és el dividend? "))
divisor = int(input("Quin és el divisor? "))

quocient = dividend//divisor
residu = dividend-(divisor*quocient)

print(f"Divisió:{dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")