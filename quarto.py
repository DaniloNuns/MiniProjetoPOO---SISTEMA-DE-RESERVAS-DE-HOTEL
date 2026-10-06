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
        self.status = status

        self.motivo_bloqueio = None
        self.periodo_bloqueio = None


    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if valor < 1:
            raise ValueError("A capacidade deve ser maior ou igual a 1.")

        self._capacidade = valor
        
    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, valor):
        if valor <= 0:
            raise ValueError("A tarifa deve ser maior que 0.")

        self._tarifa = valor 

    def calcular_tarifa(self):
        return self.tarifa
    
    def atualizar_status(self, novo_status):
        status_validos = [
            "DISPONIVEL"
            "OCUPADO"
            "MANUTENÇÃO"
            "BLOQUEADO"
        ]

        if novo_status not in status_validos:
            raise ValueError("Status de quarto inválido.")

        self.status = novo_status

    def bloquear(self, motivo, periodo, status="BLOQUEADO"):
        self.motivo_bloqueio = motivo
        self.periodo_bloqueio = periodo
        self.atualizar_status(status)

    def desbloquear(self):
        self.motivo_bloqueio = None
        self.periodo_bloqueio = None
        self.atualizar_status = ("DISPONIVEL")

    def __str__(self):
        return (
            f"Quarto {self.numero} - "
            f"Capacidade {self.capacidade} - "
            f"Tarifa: R$ {self.tarifa:.2f} - "
            f"Status: {self.status} - "
        )

    def __lt__(self, outro_quarto):
        if not isinstance(outro_quarto, Quarto):
            return NotImplemented

        return (type(self).__name__, self.numero) < (
            type(outro_quarto).__name__,
            outro_quarto.numero
        )