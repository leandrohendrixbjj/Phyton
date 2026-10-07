"""
    O que é um frozenset?
      - bastante parecido com o set, com uma diferença fundamental: é imutável.
      - o set permite adicionar e remover elementos.
      - o frozenset não permite adicionar nem remover elementos.
      - a busca continua O(1), como no set, porque a estrutura interna também é uma hash table.
"""

"""
    Por que existe o frozenset?
      - ele pode ser usado em situações nas quais um set não pode.
      - um set não pode ser elemento de outro set; um frozenset pode.
      - um set não pode ser chave de um dict; um frozenset pode.
"""

numeros = frozenset({1, 2, 3})
conjunto = {numeros}
print(conjunto)

permissoes = frozenset({"read", "write"})
usuarios = {
    permissoes: "admin",
}
print(usuarios)
