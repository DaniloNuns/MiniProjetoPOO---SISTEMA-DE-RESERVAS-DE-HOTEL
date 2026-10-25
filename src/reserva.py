from datetime import date, datetime
from quarto import Quarto
from pagamento import Pagamento
from adicional import Adicional


class Reserva:
    """
    Liga um Hospede a um Quarto.

    Guarda as datas, o número de hóspedes, a origem, o status e
    as ações do ciclo de vida da reserva, agregando Pagamento e Adicional.
    """

    def __init__(self, hospede, quarto, data_entrada, data_saida, numero_hospedes, origem):
        #Define o hóspede e o quarto associado à reserva.
        if hospede is None:
            raise ValueError ("A reserva deve possuir um hóspede.")
        
        if not isinstance(quarto, Quarto):
            raise ValueError ("A reserva deve estar associada a um quarto válido.")
        
        self._hospede = hospede
        self._quarto = quarto


        # Inicializa os dados da reserva e suas listas de pagamentos e adicionais.
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.numero_hospedes = numero_hospedes
        self.origem = origem

        self._pagamentos = []
        self._adicionais = []

        self.status = "PENDENTE"
        self.termos_aceito = False

    @property
    def hospede(self):
        return self._hospede
    
    @property
    def quarto(self):
        return self._quarto

    @property
    def data_entrada(self):
        return self._data_entrada

    @data_entrada.setter
    def data_entrada(self, valor):
        # Verifica se o valor recebido é uma data válida.
        if not isinstance(valor, date) or isinstance(valor, datetime):
            raise ValueError("A data de entrada deve ser uma data válida.")

        # Impede que a entrada seja posterior ou igual à saída.
        if hasattr(self, "_data_saida") and valor >= self._data_saida:
            raise ValueError("A data de entrada deve ser anterior à data de saída.")

        self._data_entrada = valor

    @property
    def data_saida(self):
        return self._data_saida

    @data_saida.setter
    def data_saida(self, valor):
        # Verifica se o valor recebido é uma data válida.
        if not isinstance(valor, date) or isinstance(valor, datetime):
            raise ValueError("A data de saída deve ser uma data válida.")

        # Impede que a saída seja anterior ou igual à entrada.
        if hasattr(self, "_data_entrada") and valor <= self._data_entrada:
            raise ValueError("A data de saída deve ser posterior à data de entrada.")

        self._data_saida = valor

    @property
    def numero_hospedes(self):
        return self._numero_hospedes

    @numero_hospedes.setter
    def numero_hospedes(self, valor):
        # Exige um número inteiro positivo, sem aceitar valores booleanos.
        if not isinstance(valor, int) or isinstance(valor, bool) or valor < 1:
            raise ValueError(
                "O número de hóspedes deve ser um inteiro maior ou igual a 1."
            )

        # Impede que a quantidade de hóspedes exceda a capacidade do quarto.
        if valor > self.quarto.capacidade:
            raise ValueError(
                "O número de hóspedes não pode exceder a capacidade do quarto."
            )

        self._numero_hospedes = valor
    

    @property
    def origem(self):
        return self._origem
    
    @origem.setter
    def origem(self, valor):
        #Exige uma origem informada como texto não vazio.
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError ("A origem deve ser um texto não vazio.")
        
        self._origem = valor

    @property
    def pagamentos(self):
        #Retorna uma cópia para evitar alterações externas na lista interna.
        return self._pagamentos.copy()
    
    @property
    def adicionais(self):
        #Retorna uma cópia para proteger a lista interna de adicionais.
        return self._adicionais.copy()
    
    def registrar_pagamento(self, pagamento):
        #Aceita somente objetos da classe Pagamento.
        if not isinstance(pagamento, Pagamento):
            raise ValueError ("O pagamento deve ser um objeto Pagamento.")
        
        self._pagamentos.append(pagamento)

    def lancar_adicional(self, adicional):
        #Aceita somente objetos da classe Adicional
        if not isinstance(adicional, Adicional):
            raise ValueError ("O adicional deve ser um objeto Adicional.")
        
        self._adicionais.append(adicional)

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError ("O status deve ser um texto não vazio.")

        self._status = valor
    
    @property
    def termos_aceito(self):
        return self._termos_aceito

    @termos_aceito.setter
    def termos_aceito(self, valor):
        if not isinstance(valor, bool):
            raise ValueError ("A confirmação dos termos dever ser booleano.")
        
        self._termos_aceito = valor
    
    def __len__(self):
        # Retorna a quantidade de diárias da reserva.
        return (self.data_saida - self.data_entrada).days