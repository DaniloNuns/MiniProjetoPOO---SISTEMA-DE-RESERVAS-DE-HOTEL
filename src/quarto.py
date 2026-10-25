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
        if not isinstance(valor, int) or isinstance(valor, bool) or valor < 1:
            raise ValueError (  
                "A capacidade deve ser um inteiro maior ou igual a 1."
                )

        self._capacidade = valor

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("A tarifa deve ser númerica.")

        if valor <= 0:
            raise ValueError("A tarifa deve ser maior que zero.")

        self._tarifa = valor

    def calcular_tarifa(self):
        return self.tarifa

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        status_validos = [
            "DISPONIVEL",
            "OCUPADO",
            "MANUTENCAO",
            "BLOQUEADO"
        ]

        if valor not in status_validos:
            raise ValueError("Status do quarto inválido.")
        
        self._status = valor
    
    def bloquear(self, motivo, periodo, status="BLOQUEADO"):
        self.motivo_bloqueio = motivo
        self.periodo_bloqueio = periodo
        self.status = status

    def desbloquear(self):
        self.motivo_bloqueio = None
        self.periodo_bloqueio = None
        self.status = "DISPONIVEL"

    def __str__(self):
        return (
            f"Quarto {self.numero} - "
            f"Capacidade: {self.capacidade} - "
            f"Tarifa: R$ {self.tarifa:.2f} - "
            f"Status: {self.status}"
        )