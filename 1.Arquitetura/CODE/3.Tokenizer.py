"""
1. Tokenizer

  - Uma das primeiras etapas do processamento do código-fonte.
  - Divide o código-fonte em tokens.
  - Não é a compilação inteira.
  - py -m tokenize index.py mostra, no terminal, como o arquivo foi dividido.
"""

"""
2. Fluxo

  Código-fonte
      │
      ▼
  Tokenizer / Lexer          quebra o texto em tokens
      │
      ▼
  Parser                     verifica a estrutura e a sintaxe
      │
      ▼
  AST                        estrutura da linguagem
      │
      ▼
  Compilador                 gera bytecode
      │
      ▼
  Bytecode (.pyc / memória)
      │
      ▼
  Python Virtual Machine (PVM)
      │
      ▼
  Execução
"""

"""
3. Tokens de print("Hello, World!")

  0,0-0,0:     ENCODING     'utf-8'
  1,0-1,1:     NL           '\n'
  2,0-2,5:     NAME         'print'
  2,5-2,6:     OP           '('
  2,6-2,21:    STRING       '"Hello, World!"'
  2,21-2,22:   OP           ')'
  2,22-2,23:   NEWLINE      '\n'
  3,0-3,0:     ENDMARKER    ''
"""

print("Hello, World!")
