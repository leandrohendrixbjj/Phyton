"""
    O que é um set?
      - uma coleção usada principalmente quando você precisa trabalhar com valores únicos, sem duplicidade.
      - não é uma coleção indexada.
      - estrutura interna é baseada em hash table. (O(1) para inserção, remoção e busca)]
      - é mutável: você pode adicionar, remover e modificar elementos após a criação.
      - set → conjunto de valores únicos VS dict → conjunto de pares chave: valor
"""

numbers = {1, 2, 2, 3, 4, 5, 1}

# Não aparecem duplicados
print(f"Hello, {numbers}!")

names = {"Leandro", "Soares"}
people = {"Leandro", "Ribeiro"}

"""
    Operações com sets:
      - |: União: Retorna um novo set com os elementos de ambos os sets, sem duplicidade.
      - &: Interseção: Retorna um novo set com os elementos comuns aos dois sets.
      - -: Diferença: Retorna um novo set com os elementos do primeiro set que não estão no segundo set.
"""
  
join = names | people
print(f"Hello, {join}!")

# Adiciona um elemento ao set
backend = {"Python", "Java"}
backend.add("JavaScript")
print(f"Hello, {backend}!")

# Não é possível acessar um elemento pelo índice
#print(f"Hello, {numbers[0]}!")