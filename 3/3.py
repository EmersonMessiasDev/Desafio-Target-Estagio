import json
# importando arquivo json
with open("3/dados.json") as dados:
    dados = json.load(dados)
    
dia = []
valor = []
for i in dados:
    #?criando uma lista com os itens pra ficar mais facil de manipular
    dia.append(i['dia'])
    valor.append(i['valor'])
    
maior_valor = max(valor)
i = valor.index(maior_valor)
melhor_dia = dia[i]
print(f'O maior valor de faturamento ocorrido foi no dia {melhor_dia} com valor de R${maior_valor}')

menor_valor = min(valor)
print(f'O menor valor de faturamento ocorrido R${menor_valor}')

media = sum(valor) / len(dia)
dias_acima_da_media = 0

for i in valor:
    if i > media:
        dias_acima_da_media += 1
print(f'O numero de dias no mes em que o valor diario foi superior a media foi {dias_acima_da_media} dias')
