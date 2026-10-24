from datetime import date

class Pagamento:
    """
    Guarda valor, data e forma de pagamento de uma reserva.
    """
    def __init__(self, valor, data, forma):
        self.valor = valor
        self.data = data
        self.forma = forma

    @property
    def forma(self):
        return self._forma
    
    @forma.setter
    def forma(self, valor):
        formas_validas = ["CARTAO", "PIX", "DINHEIRO"]
    
        if valor not in formas_validas:
            raise ValueError ("Forma de pagamento inválida.")
    
        self._forma = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise ValueError ("O valor do pagamento deve ser númerico.")    
            
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero.")
            

        self._valor = valor

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, valor):
        if not isinstance(valor, date):
            raise ValueError("A data do pagamento deve ser uma data válida.")
        
        self._data = valor



    

        
    

    
        
