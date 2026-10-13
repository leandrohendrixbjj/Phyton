# 1. Operador +

name = 'John'
last_name = 'Doe'

full_name = name + ' ' + last_name

print(full_name) # John Doe


# 2. Interpolação de string com f-strings (f"")
name = 'Steve'
last_name = 'Jobs'

full_name = f"{name} {last_name}"

print(full_name) # Steve Jobs


# 3. Método join()
partes = ["Leandro", "Hendrix", "Ribeiro"]

nome_completo = " ".join(partes)

print(nome_completo) # Leandro Hendrix Ribeiro

# 4 += Operador
name = 'Natalia'
last_name = 'Oliveira'

name += ' ' + last_name

print(name) # Natalia Oliveira