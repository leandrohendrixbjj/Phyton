# isinstance(): Permite verificar se uma variável corresponde a um tipo de dado específico

name = "Leandro"

# Verifica se a variável é do tipo string
isStr = isinstance(name, str)
print(f"Hello, {isStr}!")

age = 20

# Verifica multiplos tipos de dados
isInt = isinstance(age, (bool, float))
print(f"Hello, {isInt}!")
