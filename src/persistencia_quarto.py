import json

"""Persistência simples de Quarto em arquivo JSON (json.dump / json.load)."""

from quarto import Quarto
from quarto_simples import QuartoSimples
from quarto_duplo import QuartoDuplo
from quarto_luxo import QuartoLuxo

CLASSES_QUARTO = {
    "Quarto": Quarto,
    "QuartoSimples": QuartoSimples,
    "QuartoDuplo": QuartoDuplo,
    "QuartoLuxo": QuartoLuxo,
}


def quarto_to_dict(quarto):
    dados = {
        "tipo": type(quarto).__name__,
        "capacidade": quarto.capacidade,
        "numero": quarto.numero,
        "tarifa": quarto.tarifa,
        "status": quarto.status,
        "motivo_bloqueio": quarto.motivo_bloqueio,
        "periodo_bloqueio": quarto.periodo_bloqueio,
    }
    if isinstance(quarto, QuartoLuxo):
        dados["servicos_inclusos"] = quarto.servicos_inclusos
        dados["taxa_servico"] = quarto.taxa_servico
    return dados


def quarto_from_dict(dados):
    classe = CLASSES_QUARTO.get(dados["tipo"], Quarto)

    if classe is QuartoLuxo:
        quarto = QuartoLuxo(
            capacidade=dados["capacidade"],
            numero=dados["numero"],
            tarifa=dados["tarifa"],
            servicos_inclusos=dados.get("servicos_inclusos", []),
            taxa_servico=dados.get("taxa_servico", 0.0),
            status=dados.get("status", "DISPONIVEL"),
        )
    else:
        quarto = classe(
            capacidade=dados["capacidade"],
            numero=dados["numero"],
            tarifa=dados["tarifa"],
            status=dados.get("status", "DISPONIVEL"),
        )

    quarto.motivo_bloqueio = dados.get("motivo_bloqueio")
    quarto.periodo_bloqueio = dados.get("periodo_bloqueio")
    return quarto


def salvar_quartos(quartos, caminho="quartos.json"):
    dados = [quarto_to_dict(q) for q in quartos]
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)


def carregar_quartos(caminho="quartos.json"):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return [quarto_from_dict(d) for d in dados]