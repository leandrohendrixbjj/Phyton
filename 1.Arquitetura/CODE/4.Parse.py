"""
- Código-fonte: x = 10 + 20 * 3
- Tokens: ['x', '=', '10', '+', '20', '*', '3']
- AST:
       +
      / \
    10   *
        / \
       20  3
"""

import ast

codigo = "x = 10 + 20 * 3"

arvore = ast.parse(codigo)

print(ast.dump(arvore, indent=2))