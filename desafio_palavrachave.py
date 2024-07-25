# Recebe uma entrada do usuário e a divide em uma lista de strings utilizando ', ' como delimitador
strings = input().split(', ')
# Recebe uma entrada do usuário como a palavra-chave para filtragem
palavra_chave = input()

# Define a função para filtrar strings por uma palavra-chave específica
def filtrar_por_palavra_chave(strings, palavra_chave):
    # Inicializa uma lista para armazenar as strings que contêm a palavra-chave
    strings_filtradas = []
    
    # Separa a palavra-chave em palavras individuais
    palavras_chave = palavra_chave.split()
    
    # Itera sobre cada string na lista de strings
    for string in strings:
        # Verifica se a string contém pelo menos uma das palavras-chave (ignorando maiúsculas/minúsculas)
        if any(palavra_chave.lower() in string.lower() for palavra_chave in palavras_chave):
            # Se encontrarmos pelo menos uma palavra-chave na string, adicionamos à lista de resultados
            strings_filtradas.append(string)
    
    # Retorna a lista de strings que contêm a palavra-chave
    return strings_filtradas

# Chama a função filtrar_por_palavra_chave com as strings e a palavra-chave fornecidas pelo usuário # Imprime o resultado
print(filtrar_por_palavra_chave(strings, palavra_chave))

'''
Entrada                               saida
o filme foi emocionante, o enredo     ['o filme foi emocionante',
deixou a desejar, ele emociona        'ele emociona']
emociona

gostei da historia, jogo divertido,   ['gostei da historia',
tem uma historia envolvente           'tem uma historia envolvente']
historia
'''
