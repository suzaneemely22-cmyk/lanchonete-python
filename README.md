# Sistema de Atendimento e Pedidos — Burger

**Estudante:** Suzane Emely Ribeiro Ventura
**Disciplina:** Algoritmos e Programação
**Título do projeto:** Sistema de Atendimento e Pedidos em Python

## Descrição

Programa em Python, executado no terminal, que substitui o registro manual de pedidos de uma pequena lanchonete. O cliente escolhe produtos do cardápio e informa as quantidades. O programa acumula o total, aplica desconto conforme o valor da compra, solicita a forma de pagamento e mostra um resumo final.

## Funcionalidades

- Identificação do cliente pelo nome
- Cardápio com 5 produtos (código, nome e preço)
- Seleção de produtos por código e informação da quantidade
- Cálculo do subtotal de cada item e acúmulo do total da compra
- Repetição dos pedidos até o usuário digitar `0` para finalizar
- Validação de código de produto, quantidade e forma de pagamento inválidos
- Desconto automático:
  - abaixo de R$ 50,00: sem desconto
  - de R$ 50,00 a R$ 99,99: 5%
  - a partir de R$ 100,00: 10%
- Forma de pagamento: Dinheiro, PIX ou Cartão
- Resumo final com cliente, valor original, desconto (%), valor do desconto, valor final e forma de pagamento

## Como executar

1. Instale o Python 3.10 ou superior (necessário para o `match-case`).
2. Baixe ou clone este repositório.
3. No terminal, dentro da pasta do projeto, execute:

```
python Lanchonete.py
```

## Arquivos

- `Lanchonete.py` — programa principal
- `README.md` — este arquivo