from datetime import date, datetime

from quarto import Quarto


class Relatorio:
    """
    Calcula as métricas do hotel num período: taxa de ocupação,
    ADR, RevPAR, cancelamentos/no-shows e receita por tipo de quarto.
    """

    def __init__(self, data_inicio, data_fim, reservas, quartos):
        # Inicializa o período e as listas utilizadas no relatório.
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.reservas = reservas
        self.quartos = quartos

    @property
    def data_inicio(self):
        # Retorna a data inicial armazenada.
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        # Valida se o valor recebido é uma data válida.
        if not isinstance(valor, date) or isinstance(valor, datetime):
            raise ValueError("A data inicial deve ser uma data válida.")

        # Garante que a data inicial seja anterior à data final.
        if hasattr(self, "_data_fim") and valor >= self._data_fim:
            raise ValueError(
                "A data inicial deve ser anterior à data final."
            )

        self._data_inicio = valor

    @property
    def data_fim(self):
        # Retorna a data final armazenada.
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        # Valida se o valor recebido é uma data válida.
        if not isinstance(valor, date) or isinstance(valor, datetime):
            raise ValueError("A data final deve ser uma data válida.")

        # Garante que a data final seja posterior à data inicial.
        if valor <= self.data_inicio:
            raise ValueError(
                "A data final deve ser posterior à data inicial."
            )

        self._data_fim = valor

    @property
    def reservas(self):
        # Retorna uma cópia para proteger a lista original.
        return self._reservas.copy()

    @reservas.setter
    def reservas(self, valor):
        # Verifica se o valor recebido é uma lista.
        if not isinstance(valor, list):
            raise ValueError("As reservas devem estar em uma lista.")

        # Importa Reserva para validar os elementos da lista.
        from reserva import Reserva

        # Verifica se todos os elementos são reservas válidas.
        for reserva in valor:
            if not isinstance(reserva, Reserva):
                raise ValueError(
                    "A lista deve conter apenas reservas válidas."
                )

        # Armazena uma cópia da lista validada.
        self._reservas = valor.copy()

    @property
    def quartos(self):
        # Retorna uma cópia para proteger a lista original.
        return self._quartos.copy()

    @quartos.setter
    def quartos(self, valor):
        # Verifica se o valor recebido é uma lista.
        if not isinstance(valor, list):
            raise ValueError("Os quartos devem estar em uma lista.")

        # Verifica se todos os elementos são quartos válidos.
        for quarto in valor:
            if not isinstance(quarto, Quarto):
                raise ValueError(
                    "A lista deve conter apenas quartos válidos."
                )

        # Armazena uma cópia da lista validada.
        self._quartos = valor.copy()

    def calcular_taxa_ocupacao(self):
        # Calcula o total de diárias disponíveis no período.
        dias_periodo = (self.data_fim - self.data_inicio).days
        total_diarias_disponiveis = len(self._quartos) * dias_periodo

        # Evita divisão por zero quando não há diárias disponíveis.
        if total_diarias_disponiveis == 0:
            return 0.0

        total_diarias_ocupadas = 0

        # Obtém os números dos quartos considerados no relatório.
        numeros_quartos = {
            quarto.numero for quarto in self._quartos
        }

        # Percorre as reservas para contabilizar as diárias ocupadas.
        for reserva in self._reservas:
            if reserva.status in ("CANCELADA", "NO_SHOW"):
                continue

            if reserva.quarto.numero not in numeros_quartos:
                continue

            # Considera somente as datas dentro do período do relatório.
            inicio = max(reserva.data_entrada, self.data_inicio)
            fim = min(reserva.data_saida, self.data_fim)

            if inicio < fim:
                total_diarias_ocupadas += (fim - inicio).days

        # Calcula a porcentagem de ocupação do período.
        return round(
            total_diarias_ocupadas / total_diarias_disponiveis * 100,
            2
        )

    def calcular_adr(self):
        # Inicializa a receita estimada e o total de diárias vendidas.
        receita = 0.0
        diarias_vendidas = 0

        numeros_quartos = {
            quarto.numero for quarto in self._quartos
        }

        # Percorre as reservas válidas para calcular o ADR.
        for reserva in self._reservas:
            if reserva.status in ("CANCELADA", "NO_SHOW"):
                continue

            if reserva.quarto.numero not in numeros_quartos:
                continue

            # Delimita a parte da reserva dentro do período analisado.
            inicio = max(reserva.data_entrada, self.data_inicio)
            fim = min(reserva.data_saida, self.data_fim)

            if inicio >= fim:
                continue

            diarias = (fim - inicio).days

            # Soma a receita estimada e a quantidade de diárias.
            receita += reserva.quarto.calcular_tarifa() * diarias
            diarias_vendidas += diarias

        # Retorna zero quando nenhuma diária foi contabilizada.
        if diarias_vendidas == 0:
            return 0.0

        # ADR = receita estimada dividida pelas diárias vendidas.
        return round(receita / diarias_vendidas, 2)

    def calcular_revpar(self):
        # Calcula o total de diárias disponíveis no período.
        dias_periodo = (self.data_fim - self.data_inicio).days
        diarias_disponiveis = len(self._quartos) * dias_periodo

        # Evita divisão por zero quando não há diárias disponíveis.
        if diarias_disponiveis == 0:
            return 0.0

        receita = 0.0

        numeros_quartos = {
            quarto.numero for quarto in self._quartos
        }

        # Soma a receita estimada das reservas válidas.
        for reserva in self._reservas:
            if reserva.status in ("CANCELADA", "NO_SHOW"):
                continue

            if reserva.quarto.numero not in numeros_quartos:
                continue

            # Considera apenas as diárias dentro do período analisado.
            inicio = max(reserva.data_entrada, self.data_inicio)
            fim = min(reserva.data_saida, self.data_fim)

            if inicio >= fim:
                continue

            diarias = (fim - inicio).days
            receita += reserva.quarto.calcular_tarifa() * diarias

        # RevPAR = receita estimada dividida pelas diárias disponíveis.
        return round(receita / diarias_disponiveis, 2)

    def contar_cancelamentos_noshows(self):
        # Inicializa os contadores de cancelamentos e no-shows.
        cancelamentos = 0
        no_shows = 0

        # Percorre as reservas para contabilizar suas ocorrências.
        for reserva in self._reservas:
            inicio = max(reserva.data_entrada, self.data_inicio)
            fim = min(reserva.data_saida, self.data_fim)

            # Ignora reservas sem sobreposição com o período.
            if inicio >= fim:
                continue

            if reserva.status == "CANCELADA":
                cancelamentos += 1
            elif reserva.status == "NO_SHOW":
                no_shows += 1

        # Retorna as quantidades em um dicionário.
        return {
            "cancelamentos": cancelamentos,
            "no_shows": no_shows
        }

    def calcular_receita_por_tipo_quarto(self):
        # Inicializa a receita de cada tipo de quarto.
        receita_por_tipo = {}

        numeros_quartos = {
            quarto.numero for quarto in self._quartos
        }

        # Cria uma entrada para cada tipo de quarto cadastrado.
        for quarto in self._quartos:
            tipo = type(quarto).__name__
            receita_por_tipo.setdefault(tipo, 0.0)

        # Calcula a receita estimada de cada reserva por tipo de quarto.
        for reserva in self._reservas:
            if reserva.status in ("CANCELADA", "NO_SHOW"):
                continue

            if reserva.quarto.numero not in numeros_quartos:
                continue

            # Considera apenas as diárias dentro do período analisado.
            inicio = max(reserva.data_entrada, self.data_inicio)
            fim = min(reserva.data_saida, self.data_fim)

            if inicio >= fim:
                continue

            diarias = (fim - inicio).days
            tipo = type(reserva.quarto).__name__

            receita_por_tipo[tipo] += (
                reserva.quarto.calcular_tarifa() * diarias
            )

        # Retorna os valores de receita arredondados para duas casas.
        return {
            tipo: round(valor, 2)
            for tipo, valor in receita_por_tipo.items()
        }