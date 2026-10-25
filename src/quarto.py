class Quarto:
    """
    Classe base de qualquer quarto do hotel.

    Guarda capacidade, número, tarifa, status e os dados
    de bloqueio (motivo e período).
    """

    def __init__(self, capacidade, numero, tarifa, status="DISPONIVEL"):
        # Inicializa os atributos do quarto e seus dados de bloqueio.
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
        # Exige uma capacidade inteira maior ou igual a 1.
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
        # Verifica se a tarifa é numérica e não é um valor booleano.
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError("A tarifa deve ser númerica.")

        # Impede tarifas iguais ou inferiores a zero.
        if valor <= 0:
            raise ValueError("A tarifa deve ser maior que zero.")

        self._tarifa = valor

    def calcular_tarifa(self):
        # Retorna a tarifa-base de uma diária.
        return self.tarifa

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        # Define os status permitidos para um quarto.
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
        # Registra o motivo e o período do bloqueio e atualiza o status.
        self.motivo_bloqueio = motivo
        self.periodo_bloqueio = periodo
        self.status = status

    def desbloquear(self):
        # Remove os dados do bloqueio e libera o quarto.
        self.motivo_bloqueio = None
        self.periodo_bloqueio = None
        self.status = "DISPONIVEL"

    def __str__(self):
        # Retorna um resumo dos dados principais do quarto.
        return (
            f"Quarto {self.numero} - "
            f"Capacidade: {self.capacidade} - "
            f"Tarifa: R$ {self.tarifa:.2f} - "
            f"Status: {self.status}"
        )