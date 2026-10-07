"""
    1. Parsing: após a tokenização Python entra na etapa de parsing. É quando ele verifica se aqueles tokens obedecem à gramática da 
      linguagem e constrói uma estrutura sintática válida.

    Fluxo: 

        Código-fonte
              ↓
          1. Tokenização
              ↓
          Tokens
              ↓
          2. Parsing
              ↓
          AST (Abstract Syntax Tree)
              ↓
          3. Compilação para bytecode
              ↓
          Bytecode
              ↓
          4. Execução pela Python VM  
"""

"""
    2. Precedência:
      - Código-fonte: x = 10 + 20 * 3
      - Tokens: ['x', '=', '10', '+', '20', '*', '3']
      - AST:
                 +
                / \
              10   *
                  / \
                 20  3

"""

"Uma forma interessante de estudar isso é usando o módulo ast do Python."
import ast

codigo = "x = 10 + 20 * 3"

arvore = ast.parse(codigo)

print(ast.dump(arvore, indent=2))