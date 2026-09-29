class Politica:
    """
    Classe base das regras configuráveis do hotel.

    Guarda uma descrição e se a regra está ativa.
    """
    pass


class Politica_de_cancelamento(Politica):
    """
    Calcula a multa de cancelamento, conforme a antecedência 
    e o percentual configurados.
    """
    pass


class Politica_de_adesao(Politica):
    """
    Representa o termo que o hóspede confirma antes de fechar a reserva.
    """
    pass


class Quarto:
    """
    Classe base de qualquer quarto do hotel.

    Guarda capacidade, número, tarifa, status e os dados 
    de bloqueio (motivo e período).
    """
    pass


class Quarto_simples(Quarto):
    """
    Sem atributos ou métodos próprios — herda tudo de Quarto.
    """
    pass


class Quarto_duplo(Quarto):
    """
    Sem atributos ou métodos próprios — herda tudo de Quarto.
    """
    pass


class Quarto_Luxo(Quarto):
    """
    Adiciona serviços inclusos e uma taxa de serviço, 
    sobrescrevendo o cálculo de tarifa da classe mãe.
    """
    pass


class Reserva:
    """
    Liga um Hospede a um Quarto.

    Guarda as datas, o número de hóspedes, a origem, o status e 
    as ações do ciclo de vida da reserva, agregando Pagamento e Adicional.
    """
    pass


class Relatorio:
    """
    Calcula as métricas do hotel num período: taxa de ocupação, 
    ADR, RevPAR, cancelamentos/no-shows e receita por tipo de quarto.
    """
    pass


class Pessoa:
    """
    Classe base de qualquer pessoa do sistema.

    Guarda nome, documento, e-mail e telefone.
    """
    pass


class Hospede(Pessoa):
    """
    Guarda o histórico de reservas do hóspede.
    """
    pass


class Auditavel:
    """
    Guarda um histórico de ações realizadas no sistema.
    """
    pass


class Funcionario(Pessoa, Auditavel):
    """
    Guarda cargo e matrícula.

    Herda de duas classes ao mesmo tempo, cobrindo o requisito 
    de herança múltipla do projeto.
    """
    pass


class Pagamento:
    """
    Guarda valor, data e forma de pagamento de uma reserva.
    """
    pass


class Adicional:
    """
    Guarda nome e valor de um item extra lançado numa reserva.
    """
    pass


class Controle:
    """
    Verifica a disponibilidade de um quarto num intervalo de datas, 
    evitando reservas sobrepostas (overbooking).
    """
    pass
