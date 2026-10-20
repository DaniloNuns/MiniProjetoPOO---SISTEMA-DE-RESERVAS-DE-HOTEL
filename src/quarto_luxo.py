from quarto import Quarto


class QuartoLuxo(Quarto):
    """Quarto luxo. Adiciona serviços inclusos e uma taxa de serviço na tarifa."""

    def __init__(self, capacidade, numero, tarifa, servicos_inclusos=None,
                 taxa_servico=0.0, status="DISPONIVEL"):
        super().__init__(capacidade, numero, tarifa, status)
        self.servicos_inclusos = servicos_inclusos if servicos_inclusos is not None else []
        self.taxa_servico = taxa_servico

    def calcular_tarifa(self):
        return self.tarifa * (1 + self.taxa_servico)

    def adicionar_servico(self, servico):
        self.servicos_inclusos.append(servico)