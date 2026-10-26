from pessoa import Pessoa


class Hospede(Pessoa):
    """
    Representa um hóspede do hotel.

    Herda os dados pessoais de Pessoa e mantém
    o histórico de reservas do hóspede.
    """
    
    def __init__(self, nome, tipo_documento, numero_documento, email, telefone):
        #Inicializa os atributos herdados de Pessoa
        super().__init__(nome, tipo_documento, numero_documento, email, telefone)

        #Inicializa o histórico privado de reservas
        self._historico = []

    @property
    def historico(self):
    #Retorna uma cópia para proteger a lista original
        return self._historico.copy()


    def adicionar_reserva_ao_historico(self, reserva):
        #Importa Reserva aqui para reduzir o risco de importações circulares.
        from reserva import Reserva
        
        #Verifica se o objeto recebido é uma reserva.
        if not isinstance(reserva, Reserva):
            raise ValueError ("O objeto informado não é uma reserva válida.")
        
        #Verifica se a reserva pertence a este hóspede.
        if reserva.hospede is not self:
            raise ValueError("A reserva não pertecen a este hóspede.")
        
        #Impede que a mesma reserva seja adicionada duas vezes.
        if any(item is reserva for item in self._historico):
            raise ValueError("Esta reserva já está no histórico do hóspede.")
        
        self._historico.append(reserva)

    def consultar_historico(self):
        #Retorna uma cópia do histórico
        return self.historico
    


