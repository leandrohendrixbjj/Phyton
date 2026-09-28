"""
    O que é um frozenset?
      - Ele é bastante parecido com o set, mas tem uma diferença fundamental: é imutável.
      - Depois de criado, você não pode adicionar ou remover elementos.
      - Pode ser elemento de outro elemento frozenset. Set, nesse caso não é possível.
      - E ele mantém as principais operações de conjunto: união, interseção, diferença e diferença simétrica.
"""

# Imutável, não é possível adicionar ou remover elementos
backend = frozenset({"Python", "Java"})
print(f"Hello, {type(backend)}!")

# Cria um novo frozenset a partir de um set
frozen_backend = frozenset(backend)
print(f"Hello, {frozen_backend}!")