from datetime import date, datetime

class Pagamento:
    """
    Guarda valor, data e forma de pagamento de uma reserva.
    """
    def __init__(self, valor, data, forma):
        # Inicializa os atributos utilizando suas propriedades de validação.
        self.valor = valor
        self.data = data
        self.forma = forma

    @property
    def forma(self):
        return self._forma
    
    @forma.setter
    def forma(self, valor):
        # Define as formas de pagamento aceitas pelo sistema.
        formas_validas = ["CARTAO", "PIX", "DINHEIRO"]
    
        if valor not in formas_validas:
            raise ValueError ("Forma de pagamento inválida.")
    
        self._forma = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        # Exige um valor numérico, sem aceitar valores booleanos.
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError ("O valor do pagamento deve ser numérico.")    
            
        # Impede pagamentos com valor igual ou inferior a zero.
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero.")
            
        self._valor = valor

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, valor):
        # Aceita datas, mas não objetos datetime.
        if not isinstance(valor, date) or isinstance(valor, datetime):
            raise ValueError("A data do pagamento deve ser uma data válida.")
        
        self._data = valor



    

        
    

    
        
