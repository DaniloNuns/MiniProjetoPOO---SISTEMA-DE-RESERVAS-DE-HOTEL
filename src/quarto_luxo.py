from quarto import Quarto


class QuartoLuxo(Quarto):
    """Adiciona serviços inclusos e uma taxa de serviço, sobrescrevendo o cálculo de tarifa da classe mãe."""

    SERVICOS_DISPONIVEIS = {
        "HIDROMASSAGEM",
        "SERVICO_DE_QUARTO_VIP",
        "CAFETEIRA",
    }


    def __init__(self, capacidade, numero, tarifa, servicos_inclusos=None,
                 taxa_servico=10.00, status="DISPONIVEL"):
        super().__init__(capacidade, numero, tarifa, status)
        
        self.servicos_inclusos = []
        self.taxa_servico = taxa_servico

    @property
    def servicos_inclusos(self):
        return self._servicos_inclusos.copy()
    
    @property
    def taxa_servico(self):
        return self._taxa_servico
    
    @taxa_servico.setter
    def taxa_servico(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError ("A taxa de serviço deve ser númerica.")

        if valor < 0:
            raise ValueError ("A taxa de serviço não pode ser negativa.")
    
        self._taxa_servico = valor
    
    def calcular_tarifa(self):
        return self.tarifa + (
            len(self._servicos_inclusos) * self.taxa_servico
        )
    
    def adicionar_servico(self, servico):
        if servico not in self.SERVICOS_DISPONIVEIS:
            raise ValueError ("Serviço inválido.")
        
        if  servico in self.servicos_inclusos:
            raise ValueError ("Esse serviço ja está incluido no quarto.")

        self._servicos_inclusos.append(servico)




