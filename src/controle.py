from datetime import date, datetime

from quarto import Quarto


class Controle:
    """
    Verifica a disponibilidade de um quarto num intervalo de datas,
    evitando reservas sobrepostas (overbooking).
    """
    def __init__(self, reservas=None):
        #Inicializa a lista de reservas.
        if reservas is None:
            reservas = []
        
        self.reservas = reservas

    
    @property
    def reservas(self):
        #Retorna uma cópia para proteger a lista original
        return self._reservas.copy()

    @reservas.setter
    #Verifica se o valor recebido é uma lista.
    def reservas(self, valor):
        if not isinstance(valor, list):
            raise ValueError("As reservas devem estar em uma lista.")
    
        #Importa Reserva para validar os elementos da lista.
        from reserva import Reserva 

        #Verifica se os elementos são reservas.
        for reserva in valor:
            if not isinstance(reserva, Reserva):
                raise ValueError ("A lista deve conter apenas reservas válidas.")
        
        #Armazena uma cópia da lista.
        self._reservas = valor.copy()
    
    def verificar_disponibilidade(self, quarto, data_entrada, data_saida):
        if not isinstance(quarto, Quarto):
            raise ValueError("O objeto informado não é um quarto válido.")
    
        if (
            not isinstance(data_entrada, date) 
            or isinstance(data_entrada, datetime)
            or not isinstance(data_saida, date)
            or isinstance(data_saida, datetime)
        ):
            raise ValueError("As datas devem ser datas válidas.")
        
        if data_entrada >= data_saida:
            raise ValueError("A data de entrada deve ser anterior à data de saída.")
        
        for reserva in self._reservas:
            if reserva.status in ("CANCELADA", "NO_SHOW", "CHECKOUT"):
                continue
            
            if reserva.quarto.numero != quarto.numero:
                continue
            
            if (data_entrada < reserva.data_saida and data_saida > reserva.data_entrada):
                return False
            

        return True
            
