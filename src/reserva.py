class Reserva:
    """
    Liga um Hospede a um Quarto.

    Guarda as datas, o número de hóspedes, a origem, o status e
    as ações do ciclo de vida da reserva, agregando Pagamento e Adicional.
    """
    def __init__(self, hospede, quarto, data_entrada, data_saida, numero_hospedes, origem):
        self.hospede = hospede
        self.quarto = quarto

        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.numero_hospedes = numero_hospedes
        
        self.origem = origem

        self.pagamentos = []
        self.adicionais = []

        self.status = "PENDENTE"
        self.termos_aceito = False

    @property
    def data_entrada(self):
        return self._data_entrada

    @data_entrada.setter
    def data_entrada(self, valor):
        if hasattr(self, "_data_saida") and valor >= self._data_saida:
            raise ValueError (
                "A data de entrada deve ser anterior à data de saída."
            )

        self._data_entrada = valor
    
    @property
    def data_saida(self):
        return self._data_saida
    
    @data_saida.setter
    def data_saida(self, valor):
        if hasattr(self, "_data_entrada") and valor <= self._data_entrada:
            raise ValueError (
                "A data de saída deve ser posterior à data de entrada."
            )
        
        self._data_saida = valor

    @property
    def numero_hospedes(self):
        return self._numero_hospedes
    
    @numero_hospedes.setter
    def numero_hospedes(self, valor):
        if not isinstance(valor, int) or valor < 1:
            raise ValueError (
                "O número de hóspedes deve ser um inteiro maior ou iugal a 1."
            )

        if valor > self.quarto.capacidade:
            raise ValueError(
                "O número de hóspedes não pode exceder a capacidade do quarto."
            )
        
        self._numero_hospedes = valor
    
    def __len__ (self):
        return (self.data_saida - self.data_entrada).days