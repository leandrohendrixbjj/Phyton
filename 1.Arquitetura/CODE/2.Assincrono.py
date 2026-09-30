"""
1. Conceitualmente:
  Tarefa A ── espera I/O ─────────── continua
  Tarefa B ── espera I/O ─────────── continua
             ↑
       enquanto uma espera,
       outra pode executar
"""

import asyncio

async def tarefa(nome, tempo = 2):
    print(f"Iniciando {nome}")
    await asyncio.sleep(tempo)
    print(f"Terminando {nome}")

async def main():
    await asyncio.gather(
        tarefa("A", 5),
        tarefa("B", 2)
        
    )

asyncio.run(main()) 