from pessoa import Pessoa
from auditavel import Auditavel


class Funcionario(Pessoa, Auditavel):
    """
    Guarda cargo e matrícula.

    Herda de duas classes ao mesmo tempo, cobrindo o requisito
    de herança múltipla do projeto.
    """
    pass
