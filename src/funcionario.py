from pessoa import Pessoa
from auditavel import Auditavel


class Funcionario(Pessoa, Auditavel):
    """
    Representa um funcionário do hotel.

    Herda os dados pessoais de Pessoa e o histórico
    de ações de Auditavel       
    """

    def __init__(self, nome, tipo_documento, numero_documento, email, telefone, cargo, matricula):

        #Inicializa os dados herdados da classe Pessoa.
        Pessoa.__init__(self, nome, tipo_documento, numero_documento, email, telefone)

        #Inicia o histórico herdade da classe Auditavel.
        Auditavel.__init__(self)

        #Inicia os atributos próprios de Funcionário.
        self.cargo = cargo
        self.matricula = matricula
    
    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo (self, valor):
        #Valida o cargo antes de armazená-lo.
        self._cargo = self._validar_texto(valor, "O cargo")
    
    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula (self, valor):
        #Mantém a matrícula como texto.
        self._matricula = self._validar_texto(valor, "A matrícula")
        
    
