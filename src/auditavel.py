class Auditavel:
    """
    Guarda um histórico de ações realizadas no sistema.
    """

    def __init__(self):
        #Inicializa o histórico privado de ações.
        self._historico_acoes = []
    
    @property
    def historico_acoes(self):
        #Retorna uma cópia para proteger a lista original
        return self._historico_acoes.copy()
    
    def registrar_acao(self, descricao):
        #Verifica se a descrição é um texto não vazio.
        if not isinstance(descricao, str) or not descricao.strip():
            raise ValueError("A descrição da ação não pode ser vazia.")

        #Registra a ação no histórico
        self._historico_acoes.append(descricao.strip())
    
    def listar_historico(self):
        #Retorna uma cópia do histórico de ações.
        return self.historico_acoes
    