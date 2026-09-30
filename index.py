"""
1. Conceitualmente:
  A ── espera 5s ── termina
  B ── espera 2s ── termina
"""

import time

def tarefa(nome, tempo = 2):
    print(f"Iniciando {nome}")
    time.sleep(2)
    print(f"Terminando {nome}")

def main():
    tarefa("A", 5)
    tarefa("B", 2)

main()