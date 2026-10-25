class Pessoa:
    """
    Classe base de qualquer pessoa do sistema.

    Guarda nome, documento, e-mail e telefone.
    """

    def __init__(self, nome, documento, email, telefone):
        #Inicializa os atributos utilizando suas propriedades.
        self.nome = nome
        self.documento = documento
        self.email = email
        self.telefone = telefone
    

    @property 
    def nome(self):
        return self._name
    
    @nome.setter
    def nome (self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome deve ser um texto não vazio.")
    
    self._nome = valor

    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O documento deve ser um texto não vazio.")
    
    self._documento = valor

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O e-mail deve ser um texto não vazio.")
    
    self._email = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O telefone deve ser um texto não vazio.")
    
    self._telefone = valor

    def atualizar_contato(self, email, telefone):
        #Atualiza os dados de contato utilizando validações existentes.
        self.email = email
        self.telefone = telefone