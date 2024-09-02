def inverter(s):
    return s[::-1]

#EXECUÇÃO

stringInicial = input("Digite uma string para inverter: ")
stringInvertida = inverter(stringInicial)

print(f"String original: {stringInicial}")
print(f"String invertida: {stringInvertida}")