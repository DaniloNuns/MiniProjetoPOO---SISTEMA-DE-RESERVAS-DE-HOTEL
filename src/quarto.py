"""Define a classe Quarto e suas subclasses (QuartoSimples, QuartoDuplo, QuartoLuxo)."""


class Quarto:
    """
    Classe base de qualquer quarto do hotel.

    Guarda capacidade, número, tarifa, status e os dados
    de bloqueio (motivo e período).
    """

    def __init__(self, capacidade, numero, tarifa, status="DISPONIVEL"):
        self.capacidade = capacidade
        self.numero = numero
        self.tarifa = tarifa
        self.atualizar_status(status)

        self.motivo_bloqueio = None
        self.periodo_bloqueio = None

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor < 1:
            raise ValueError(
                "A capacidade deve ser um inteiro maior ou igual a 1."
            )
        self._capacidade = valor

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, valor):
        if valor <= 0:
            raise ValueError("A tarifa deve ser maior que 0.")
        self._tarifa = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        status_validos = ["DISPONIVEL", "OCUPADO", "MANUTENCAO", "BLOQUEADO"]
        if valor not in status_validos:
            raise ValueError("Status do quarto inválido.")
        self._status = valor

    def calcular_tarifa(self):
        """Valor de uma diária. Cada subclasse pode sobrescrever esta regra."""
        return self.tarifa

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def bloquear(self, motivo, periodo, status="BLOQUEADO"):
        self.motivo_bloqueio = motivo
        self.periodo_bloqueio = periodo
        self.atualizar_status(status)

    def desbloquear(self):
        self.motivo_bloqueio = None
        self.periodo_bloqueio = None
        self.atualizar_status("DISPONIVEL")

    def __str__(self):
        return (
            f"Quarto {self.numero} - "
            f"Capacidade: {self.capacidade} - "
            f"Tarifa: R$ {self.tarifa:.2f} - "
            f"Status: {self.status}"
        )

    def __lt__(self, outro_quarto):
        if not isinstance(outro_quarto, Quarto):
            return NotImplemented

        ordem_tipo = {
            "QuartoSimples": 0,
            "QuartoDuplo": 1,
            "QuartoLuxo": 2,
        }
        tipo_self = ordem_tipo.get(type(self).__name__, 99)
        tipo_outro = ordem_tipo.get(type(outro_quarto).__name__, 99)

        return (tipo_self, self.numero) < (tipo_outro, outro_quarto.numero)


class QuartoSimples(Quarto):
    """Quarto simples. Sem atributos ou regras próprias — herda tudo de Quarto."""


class QuartoDuplo(Quarto):
    """Quarto duplo. Sem atributos ou regras próprias — herda tudo de Quarto."""


class QuartoLuxo(Quarto):
    """Quarto luxo. Adiciona serviços inclusos e uma taxa de serviço na tarifa."""

    def __init__(self, capacidade, numero, tarifa, servicos_inclusos=None,
                 taxa_servico=0.0, status="DISPONIVEL"):
        super().__init__(capacidade, numero, tarifa, status)
        self.servicos_inclusos = servicos_inclusos if servicos_inclusos is not None else []
        self.taxa_servico = taxa_servico

    def calcular_tarifa(self):
        """Sobrescrito: soma a taxa de serviço ao valor da diária."""
        return self.tarifa * (1 + self.taxa_servico)

    def adicionar_servico(self, servico):
        self.servicos_inclusos.append(servico)