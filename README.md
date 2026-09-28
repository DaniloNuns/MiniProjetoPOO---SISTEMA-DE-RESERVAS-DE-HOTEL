[README.md](https://github.com/user-attachments/files/32778952/README.md)
# Sistema de Reservas de Hotel

Mini-projeto de Programação Orientada a Objetos (POO) — Tema 8, disciplina de Engenharia de Software, UFCA.

## Descrição

Sistema para gerenciar as reservas de um hotel: cadastro de hóspedes e quartos, criação e acompanhamento de reservas (com check-in, check-out, cancelamento e no-show), controle de disponibilidade, pagamentos e adicionais, aplicação de políticas configuráveis (multa de cancelamento, termo de adesão), e geração de relatórios (taxa de ocupação, ADR, RevPAR, entre outros).

## Objetivo

Aplicar os pilares de Programação Orientada a Objetos — encapsulamento, herança (incluindo herança múltipla), polimorfismo e composição — na modelagem de um domínio real, cobrindo desde o diagrama de classes até a implementação com validações, persistência e testes automatizados.

## Estrutura planejada

| Classe | Descrição |
|---|---|
| `Politica` | Classe base das regras configuráveis do hotel. Guarda uma descrição e se a regra está ativa. |
| `Politica_de_cancelamento` *(herda de `Politica`)* | Calcula a multa de cancelamento, conforme a antecedência e o percentual configurados. |
| `Politica_de_adesao` *(herda de `Politica`)* | Representa o termo que o hóspede confirma antes de fechar a reserva. |
| `Quarto` | Classe base de qualquer quarto do hotel. Guarda capacidade, número, tarifa, status e os dados de bloqueio (motivo e período). |
| `Quarto_simples` *(herda de `Quarto`)* | Sem atributos ou métodos próprios — herda tudo de `Quarto`. |
| `Quarto_duplo` *(herda de `Quarto`)* | Sem atributos ou métodos próprios — herda tudo de `Quarto`. |
| `Quarto_Luxo` *(herda de `Quarto`)* | Adiciona serviços inclusos e uma taxa de serviço, sobrescrevendo o cálculo de tarifa da classe mãe. |
| `Reserva` | Liga um `Hospede` a um `Quarto`. Guarda as datas, o número de hóspedes, a origem, o status (PENDENTE, CONFIRMADA, CHECKIN, CHECKOUT, CANCELADA, NO_SHOW) e as ações do ciclo de vida da reserva: confirmar, cancelar, check-in, check-out, marcar no-show. Agrega, por composição, os `Pagamento` e `Adicional` lançados nela. |
| `Relatorio` | Calcula as métricas do hotel num período: taxa de ocupação, ADR, RevPAR, cancelamentos/no-shows e receita por tipo de quarto. |
| `Pessoa` | Classe base de qualquer pessoa do sistema. Guarda nome, documento, e-mail e telefone. |
| `Hospede` *(herda de `Pessoa`)* | Guarda o histórico de reservas do hóspede. |
| `Auditavel` | Guarda um histórico de ações realizadas no sistema. |
| `Funcionario` *(herda de `Pessoa` e `Auditavel` — herança múltipla)* | Guarda cargo e matrícula. Herda de duas classes ao mesmo tempo, cobrindo o requisito de herança múltipla do projeto. |
| `Pagamento` | Guarda valor, data e forma de pagamento de uma reserva. |
| `Adicional` | Guarda nome e valor de um item extra lançado numa reserva. |
| `Controle` | Verifica a disponibilidade de um quarto num intervalo de datas, evitando reservas sobrepostas (overbooking). |
| `calculos` *(módulo)* | Funções puras que calculam o valor de uma diária, considerando os multiplicadores de temporada e fim de semana. |
| `dados` *(módulo, planejado para a Semana 3)* | Funções de persistência, para salvar e carregar quartos, hóspedes, reservas e pagamentos em JSON. |

## Diagrama de classes

O UML textual completo (classes, atributos, métodos e relacionamentos), incluindo um diagrama Mermaid renderizado automaticamente pelo GitHub, está em [`uml-textual.md`](uml-textual.md).

A versão editável do diagrama, feita no Excalidraw, está em [`diagrama.excalidraw`](diagrama.excalidraw) — pode ser aberta em [excalidraw.com](https://excalidraw.com) (menu → Open) para visualização ou edição.

## Status

Projeto em desenvolvimento. Entrega da Semana 1: UML textual, README inicial e esqueleto de classes.
