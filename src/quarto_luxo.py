from quarto import Quarto


class QuartoLuxo(Quarto):
    """
    Adiciona serviços inclusos e uma taxa de serviço,
    sobrescrevendo o cálculo de tarifa da classe-mãe.
    """

    # Define os serviços que podem ser incluídos no quarto de luxo.
    SERVICOS_DISPONIVEIS = {
        "HIDROMASSAGEM",
        "SERVICO_DE_QUARTO_VIP",
        "CAFETEIRA",
    }

    def __init__(
        self,
        capacidade,
        numero,
        tarifa,
        taxa_servico=10.00,
        status="DISPONIVEL"
    ):
        # Inicializa os atributos herdados da classe Quarto.
        super().__init__(capacidade, numero, tarifa, status)

        # Inicializa a lista de serviços e define a taxa por serviço.
        self._servicos_inclusos = []
        self.taxa_servico = taxa_servico

    @property
    def servicos_inclusos(self):
        # Retorna uma cópia para proteger a lista interna contra alterações externas.
        return self._servicos_inclusos.copy()

    @property
    def taxa_servico(self):
        return self._taxa_servico

    @taxa_servico.setter
    def taxa_servico(self, valor):
        # Verifica se a taxa é numérica e não é um valor booleano.
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("A taxa de serviço deve ser numérica.")

        # Impede que a taxa por serviço seja negativa.
        if valor < 0:
            raise ValueError("A taxa de serviço não pode ser negativa.")

        self._taxa_servico = valor

    def calcular_tarifa(self):
        # Acrescenta à tarifa-base o valor correspondente aos serviços inclusos.
        return self.tarifa + (
            len(self._servicos_inclusos) * self.taxa_servico
        )

    def adicionar_servico(self, servico):
        # Verifica se o serviço pertence às opções disponíveis.
        if servico not in self.SERVICOS_DISPONIVEIS:
            raise ValueError("Serviço inválido.")

        # Impede que o mesmo serviço seja incluído mais de uma vez.
        if servico in self._servicos_inclusos:
            raise ValueError("Esse serviço já está incluído no quarto.")

        self._servicos_inclusos.append(servico)