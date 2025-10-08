divident = float(input("Quin és el divident?"))
divisor = float(input("Quin és el divisor?"))

quocient = divident//divisor
residu = divident-(divisor*quocient)

print(f"Divisió: {divident}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")