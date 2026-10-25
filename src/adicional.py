class Adicional:
    """
    Representa um adicional oferecido pelo hotel.
    """

    # Define os adicionais disponíveis e seus preços fixos.
    PRECOS = {
        "CAFE_DA_MANHA": 30.00,
        "LANCHE_DA_TARDE": 30.00,
        "SPA": 80.00,
    }

    def __init__(self, nome):
        # Define o nome e o preço correspondente ao adicional.
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        # Verifica se o nome é válido e está cadastrado no catálogo.
        if not isinstance(valor, str) or valor not in self.PRECOS:
            raise ValueError("Adicional inválido.")

        self._nome = valor
        self._valor = self.PRECOS[valor]

    @property
    def valor(self):
        return self._valor

    def __str__(self):
        # Retorna o nome do adicional acompanhado de seu preço.
        return f"{self.nome}: R$ {self.valor:.2f}"