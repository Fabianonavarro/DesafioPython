# Entrada do usuário
idades = list(map(int, input().split(',')))

# Define uma função chamada agrupamento_idade que recebe uma lista de idades e retorna um dicionário com contagem de idades em grupos pré-definidos
def agrupamento_idade(idades):
    # Inicializa um dicionário com grupos de idade como chaves e contadores iniciados em zero como valores
    grupos = {'0-18': 0, '19-35': 0, '36-50': 0, '51-70': 0, '71+': 0}
    
    # Itera sobre cada idade na lista de idades
    for idade in idades:
        # Verifica em qual faixa etária a idade se encaixa e incrementa o contador apropriado
          if idade <= 18:
              grupos['0-18'] += 1
          elif idade <= 35:
              grupos['19-35'] += 1
        # TODO: Complete o código inserindo os demais grupos de faixas etárias
          elif idade <= 50:
              grupos['36-50'] += 1
          elif idade <= 70:
              grupos['51-70'] += 1
          else:
              grupos['71+'] += 1
    
       
    # Retorna o dicionário com a contagem de idades em cada grupo
    return grupos

# Chama a função agrupamento_idade com a lista de idades fornecida como entrada do usuário e imprime o resultado
print(agrupamento_idade(idades))


'''
Entrada                       	Saída
15, 22, 34, 45, 52, 67, 80	{'0-18': 1, '19-35': 2, '36-50': 1, '51-70': 2, '71+': 1}
18, 22, 27, 32, 38, 42, 49	{'0-18': 1, '19-35': 3, '36-50': 3, '51-70': 0, '71+': 0}
'''
