'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado
teve dentro do valor total mensal da distribuidora.'''

geral = [{"estado":'SP',"valor":67.83643},{"estado":'RJ',"valor":36.67866},{"estado":'MG',"valor":29.22988},{"estado":'ES',"valor":27.16548},{"estado":'OUTROS',"valor":19.84953}]
faturamento =[]
for i in geral:
    faturamento.append(i["valor"])
print("Percentual de representação por estado baseado no valor total: ")
valor_total_faturamento = sum(faturamento)
for i in geral:
    if i["estado"] != 'OUTROS':
        print(f"O estado {i['estado']} representa ", end="")
        print(f"{i['valor']/valor_total_faturamento:.1%}")   
    else: 
        print(f'A Respresentação dos demais estados é de ',end="")
        print(f"{i['valor']/valor_total_faturamento:.1%}")   


