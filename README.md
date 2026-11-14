# beancount-agent

Contabilidade diária movida a agentes, construída sobre o [Beancount](https://github.com/beancount/beancount) e o [Fava](https://github.com/beancount/fava).

> Status: em construção (MVP). Ainda não use em produção.

## O que faz

1. **Importa** os arquivos exportados pelo banco e pelos cartões (OFX/CSV) e os transforma em lançamentos de partida dobrada. Primeiros alvos: o extrato do Banco Inter PJ, a fatura do cartão Inter e as transações do cartão Rain.
2. **Deduplica**: o mesmo extrato importado duas vezes, ou a despesa da fatura e o pagamento da fatura, não geram lançamento em dobro.
3. **Classifica** as transações: primeiro com regras determinísticas e, para o resto, com um agente de IA que explica a sugestão. **Nada entra no livro sem aprovação humana**, e as aprovações viram regras.
4. **Concilia**: confere o saldo do livro com o saldo do extrato e o total da fatura (`balance` assertions).
5. **Gera relatórios no padrão brasileiro**: balancete, DRE e balanço patrimonial mensais.
6. **Roda na nuvem**: uma rotina diária no GitHub Actions e o Fava no Cloud Run para a revisão.
7. **Sela o fechamento**: registra o hash do livro do mês em um timestamp público (OpenTimestamps), sem expor os dados.

## Código público, dados privados

Este repositório contém **apenas código, plano de contas de referência e um livro de exemplo com dados sintéticos**.
Os livros reais de cada empresa ficam em um repositório **privado** separado, que usa este projeto como ferramenta.
Nunca faça commit de extratos, faturas, livros reais ou credenciais aqui.

## Licença

Apache-2.0
