from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    """
        Classmethod: diz que a função pode ser acessada diretamente pela classe, sem precisar de uma 
        instância. Geralmente recebe como primeiro parâmetro a própria classe (cls), Isso permite que 
        você acesse atributos e métodos da classe diretamente, sem precisar de uma instância.

        Lembrado que existem diferenças importantes entre classmethod e staticmethod
    """           
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    """
      Property: Método pode ser acessado como um atributo, mas na verdade é um método. 
         - Ele NÃO pode ser invocado sem uma instância
         - É principalmente uma forma de expor um método através da sintaxe de atributo.         
         - Você não precisa ter um atributo declarado no __init__ para usar @property.'
    """
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'    
    
    def adicionar_produto_ao_cardapio(self, produto):
        self._cardapio.append(produto)

    def get_cardapio(self):
        print(f'{'Nome do prato'.ljust(25)} | {'Preço'.ljust(25)} | {'Descrição'.ljust(25)}')
        for produto in self._cardapio:  # produto é um objeto da classe Prato ou Bebida
            descricao = produto._descricao if hasattr(produto, '_descricao') else produto._volume
            print(
                f'{produto._nome.ljust(25)} | '
                f'{str(produto._preco).ljust(25)} | '
                f'{str(descricao).ljust(25)}'                 
            )
        return '\n'.join([produto._nome for produto in self._cardapio]) # retorna uma string com os nomes dos produtos  
