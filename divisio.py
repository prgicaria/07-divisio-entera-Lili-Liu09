divident = int(input("Quin és el divident?"))
divisor = int(input("Quin és el divisor?"))

quocient = divident//divisor
residu = divident-(divisor*quocient)
divisió = {divident}/{divisor}

print(f"Divisió: {divisió: .0f}")
print(f"Quocient: {quocient: .0f}")
print(f"Residu: {residu: .0f}")