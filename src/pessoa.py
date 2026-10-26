class Pessoa:
    """
    Classe base de qualquer pessoa do sistema.

    Guarda nome, tipo e número do documento, e-mail e telefone.
    """

    # Define os tipos de documento aceitos pelo sistema.
    TIPOS_DOCUMENTO = (
        "CPF",
        "RG",
        "PASSAPORTE",
        "CNH"
    )

    def __init__(self, nome, tipo_documento, numero_documento, email, telefone):
        # Inicializa os atributos utilizando suas propriedades.
        self.nome = nome
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.email = email
        self.telefone = telefone
    
    @staticmethod
    def _validar_texto(valor, campo):
        # Verifica se o valor é um texto não vazio e remove espaços na extremidades.
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} deve ser um texto não vazio.")
        
        return valor.strip()
    
    @property 
    def nome(self):
        return self._nome
    
    @nome.setter
    # Valida o nome antes de armazená-lo
    def nome (self, valor):
        self._nome = self._validar_texto(valor, "O nome")
        
    @property
    def tipo_documento(self):
        return self._tipo_documento
    
    @tipo_documento.setter
    def tipo_documento(self, valor):
        # Normaliza o texto e verifica se o tipo está no catálogo.
        valor = self._validar_texto(valor, "O tipo de documento").upper()
        
        if valor not in self.TIPOS_DOCUMENTO:
            raise ValueError("Tipo de documento inválido.")

        self._tipo_documento = valor

    @property
    def numero_documento(self):
        return self._numero_documento

    @numero_documento.setter
    # Mantém o documento como texto para preservar zeros iniciais.
    def numero_documento(self, valor):
        self._numero_documento = self._validar_texto(valor, "O numero do documento")
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        valor = self._validar_texto(valor, "O e-mail")

        if "@" not in valor or ".com" not in valor.lower():
            raise ValueError ("Formato de e-mail inválido.")
        
        self._email = valor
    
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        #Valida o telefone antes de armazená-lo
        valor = self._validar_texto(valor, "O telefone")
        
        digitos = "".join(caractere for caractere in valor if caractere.isdigit())

        if len(digitos) not in (10, 11):
            raise ValueError("O telefone deve conter DDD e 8 ou 9 dígitos")
        
        self._telefone = valor

    def atualizar_contato(self, email, telefone):
        #Valida os dois dados antes de modificar o contato atual
        email_validado = self._validar_texto(email, "O e-mail")
        telefone_validado = self._validar_texto(telefone, "O telefone")

        #Valida o formato do e-mail.
        if ("@" not in email_validado or ".com" not in email_validado.lower()):
            raise ValueError ("Formato de e-mail inválido.")

        #Verifica a quantidade de dígitos do telefone.
        digitos = "".join(caractere for caractere in telefone_validado if caractere.isdigit())
        if len(digitos) not in (10, 11):
            raise ValueError ("O telefone deve conter DDD e 8 ou 9 dígitos.")

        #Atualiza o contato somente depois que ambas validações passam.
        self._email = email_validado
        self._telefone = telefone_validado