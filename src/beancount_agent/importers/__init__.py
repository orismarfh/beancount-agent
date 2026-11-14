"""Importadores (beangulp) de extratos e faturas.

Planejados, ainda não implementados:

- ``inter_extrato``: extrato da conta do Banco Inter PJ.
- ``inter_cartao``: fatura do cartão Inter.
- ``rain``: transações do cartão Rain.

Cada importador deve ser determinístico e idempotente: importar o mesmo arquivo duas vezes
não pode gerar lançamentos duplicados.
"""
