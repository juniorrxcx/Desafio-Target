import json

#Carregar os dados do arquivo JSON
def dados(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data['faturamentoDiario']

#Função para analisar o faturamento diário
def analisarFat(faturamentos):
    #Dias com faturamento maior que zero
    filtrados = [f['valor'] for f in faturamentos if f['valor'] > 0]
    
    #Calcula o menor e maior faturamento
    menorFaturamento = min(filtrados)
    maiorFaturamento = max(filtrados)
    
    #Calcula a média mensal de faturamento
    media_mensal = sum(filtrados) / len(filtrados)
    
    # Conta os dias com faturamento acima da média mensal
    dias_acima_da_media = len([f for f in filtrados if f > media_mensal])
    
    return menorFaturamento, maiorFaturamento, dias_acima_da_media

#Execução
dadosFaturamento = dados('fat.json')
menor, maior, dias_acima_media = analisarFat(dadosFaturamento)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
