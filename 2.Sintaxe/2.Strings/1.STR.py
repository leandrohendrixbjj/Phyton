"""
    index: retorna o índice da primeira ocorrência de um substring em uma string. Se o substring não for encontrado, retorna um erro.
"""

my_str = 'Hello world'

print(my_str[6])  # 'w'
print(my_str[-1])  # 'd'
print(my_str[11])  # IndexError: string index out of range

# Para alterar o conteúdo de uma string, podemos criar uma nova string com o conteúdo desejado.
my_str = 'Hello python'
print(my_str)  # 'Hello python'

# Strings são imutáveis, portanto, não podemos alterar o conteúdo de uma string.
my_str[0] = 'J'  # TypeError: 'str' object does not support item assignment

