def ler_nome():
    nome = input("Digite o nome do cliente: ")
    while nome == "":
        print("Nome inválido!")
        nome = input("Digite o nome do cliente: ")
    return nome


def mostrar_cardapio():
    print("\n========== CARDÁPIO ==========")
    print("1 - X-Burguer ........ R$ 18.00")
    print("2 - X-Salada ......... R$ 20.00")
    print("3 - Sorvete .......... R$ 12.00")
    print("4 - Batata frita ..... R$ 15.00")
    print("5"
    " - Refrigerante ..... R$ 6.50")
    print("0 - Finalizar pedido")
    print("==============================")


def obter_preco(codigo):
    match codigo:
        case "1":
            return 18.00
        case "2":
            return 20.00
        case "3":
            return 12.00
        case "4":
            return 15.00
        case "5":
            return 6.50
        case _:
            return 0


def ler_quantidade():
    quantidade = int(input("Quantidade: "))
    while quantidade <= 0:
        print("Quantidade inválida! Digite um número maior que 0.")
        quantidade = int(input("Quantidade: "))
    return quantidade


def calcular_subtotal(preco, quantidade):
    return preco * quantidade


def realizar_pedidos():
    total = 0
    continuar = True

    while continuar:
        mostrar_cardapio()
        codigo = input("Código do produto (0 para finalizar): ")

        if codigo == "0":
            continuar = False
        else:
            preco = obter_preco(codigo)
            if preco == 0:
                print("Código inválido!")
            else:
                quantidade = ler_quantidade()
                subtotal = calcular_subtotal(preco, quantidade)
                total = total + subtotal
                print(f"Subtotal: R$ {subtotal:.2f} | Total parcial: R$ {total:.2f}")

    return total


def calcular_percentual_desconto(total):
    if total < 50:
        return 0
    elif total >= 50 and total < 100:
        return 5
    else:
        return 10


def escolher_pagamento():
    forma = ""
    while forma == "":
        print("\n1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
        opcao = input("Forma de pagamento: ")
        match opcao:
            case "1":
                forma = "Dinheiro"
            case "2":
                forma = "PIX"
            case "3":
                forma = "Cartão"
            case _:
                print("Opção inválida!")
    return forma


def mostrar_resumo(nome, total, percentual, desconto, valor_final, pagamento):
    print("\n========== RESUMO ==========")
    print(f"Cliente: {nome}")
    print(f"Valor original: R$ {total:.2f}")
    print(f"Desconto aplicado: {percentual}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Pagamento: {pagamento}")
    print("============================")
    print("Obrigado pela preferência!")


def main():
    print("===== BEM-VINDO À BURGER =====")
    nome = ler_nome()
    total = realizar_pedidos()

    if total == 0:
        print("Nenhum item pedido. Atendimento encerrado.")
    else:
        percentual = calcular_percentual_desconto(total)
        desconto = total * percentual / 100
        valor_final = total - desconto
        pagamento = escolher_pagamento()
        mostrar_resumo(nome, total, percentual, desconto, valor_final, pagamento)


main()