# Obtém os valores financeiros como uma lista de entrada do usuário,
# convertendo cada valor para float após remover espaços em branco e dividindo a entrada pelos caracteres de vírgula.
entrada = [float(valor.strip()) for valor in input().split(',')]

# Define a função de normalização Min-Max.
def min_max_normalization(data):
    # Encontra o menor e o maior valor na lista de dados.
    min_val = min(data)
    max_val = max(data)
    
    # Verifica se todos os valores são iguais.
    if max_val == min_val:
        # Se todos os valores são iguais, retorna uma lista de zeros.
        return [0.0] * len(data)
    
    # TODO: Aplique a fórmula de normalização Min-Max para cada valor na lista de dados.
    x_norm = [(x - min_val) / (max_val - min_val) for x in data]
    
    return x_norm

# Imprime os valores normalizados.
print(min_max_normalization(entrada))

'''
Entrada	                                     Saída
1500.0, 2000.0, 2500.0, 3000.0, 3500.0	      [0.0, 0.25, 0.5, 0.75, 1.0]
1000.0, 1500.0, 2000.0	                      [0.0, 0.5, 1.0]
1200.0, 800.0, 1000.0, 900.0                  [1.0, 0.0, 0.5, 0.25]

'''
