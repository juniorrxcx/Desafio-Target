faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#Ccalcular o percentual de representação de cada estado
def Percentual(faturamento):
    totalFaturamento = sum(faturamento.values())
    percentual = {}
    
    for estado, valor in faturamento.items():
        percentual[estado] = (valor / totalFaturamento) * 100
    
    return percentual

#Calcular os percentuais
percentuais = Percentual(faturamento_estado)

#Mostrando os resultados
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")