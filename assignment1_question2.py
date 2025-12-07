# CODE REQUIREMENT 1 of 8 - welcome message with name, surname, and menu (pt-br: EXIGÊNCIA DO CÓDIGO 1 de 8 - mensagem de boas-vindas com nome, sobrenome e menu)

print("=" * 64)
print('=' * 8 + " Bem-vindo à Pizzaria do Samuel Alves Miranda! " + '=' * 9)
print("=" * 64)
print('-' * 28 + "Cardápio" + '-' * 28)
print("-" * 64)
print('=' * 8 + "| Tamanho | Pizza Salgada(PS) | Pizza Doce(PD) |" + '=' * 8)
print('-' * 8 +  "|    P    |      R$ 30.00     |    R$ 34.00    |" + '-' * 8)
print('-' * 8 +  "|    M    |      R$ 45.00     |    R$ 48.00    |" + '-' * 8)
print('-' * 8 +  "|    G    |      R$ 60.00     |    R$ 66.00    |" + '-' * 8)
print("=" * 64)

# I could use def, but this assignment is only content from leason 4. (pt-br: eu poderia usar def, mas esta tarefa contém apenas o conteúdo da aula 4.)

# CODE REQUIREMENT 5 of 8 - accumulator to sum the values ​​of orders (pt-br: EXIGÊNCIA DO CÓDIGO 5 de 8 acumulador para somar valores dos pedidos)
# requirement 5 comes before the others in the logical order because we need to declare the variable before using it in the loop.
# pt-br: essa exigência vem antes das outras, precisamos declarar a variável antes de usar no loop.

totalPedido = 0.0

# CODE REQUIREMENT 7 of 8 - use while, break, continue structures (pt-br: usar estruturas while, break, continue)
# the main loop is where start collecting request (pt-br: o loop principal é onde começa a coletar os pedidos)

while True:
    # CODE REQUIREMENT 2 of 8 - favor input with validation (pt-br: input do sabor com validação)
    while True:
        sabor = input("Qual o sabor desejado? (PS/PD): ")

        if sabor == "PS" or sabor == "PD":
            break
        else:
            print("Sabor inválido. Tente novamente, por gentileza.")
            continue # CODE REQUIREMENT 7 of 8 use continue (pt-br: usar continue)

    # CODE REQUIREMENT 3 of 8 - size input with validation (pt-br: input do tamanho com validação)
    while True:
        tamanho = input("Qual o tamanho desejado? (P/M/G): ")

        if tamanho == "P" or tamanho == "M" or tamanho == "G":
            break
        else:
            print("Tamanho inválido. Tente novamente, por gentileza.")
            continue # CODE REQUIREMENT 7 of 8 use continue (pt-br: usar continue)

# CODE REQUIREMENT 4 of 8 - implement if, elif, and/or else statements. (pt-br: implementar if, elif e/ou else.)

    valorPizza = 0.0

    if sabor == "PS": # Flavor PS (Sabor PS)
        if tamanho == "P":
            valorPizza = 30.00
        elif tamanho == "M":
            valorPizza = 45.00
        elif tamanho == "G":
            valorPizza = 60.00
    else: # Flavor PD (Sabor PD)
        if tamanho == "P":
            valorPizza = 34.00
        elif tamanho == "M":
            valorPizza = 48.00
        elif tamanho == "G":
            valorPizza = 66.00

    sabor_texto = "Pizza salgada" if sabor == "PS" else "Pizza doce"
    print(f"Você pediu uma {sabor_texto} no tamanho {tamanho}: R$ {valorPizza:.2f}")

    # CODE REQUIREMENT 5 of 8 - accumulator system (pt-br: sistema de acumulação)
    # Add the current pizza price to the total order price (pt-br: Somar o valor da pizza atual com o total do pedido)

    totalPedido += valorPizza

    # CODE REQUIREMENT 6 of 8 - add more pizzas (pt-br: adicionar mais pizzas)
    # loop with Y/N validation (pt-br: loop com validação de S/N)

    while True:
        continuar = input("Deseja mais alguma coisa? (S/N): ")
        if continuar == "S" or continuar == "N":
            break
        else:
            print("Por favor, responda com S para Sim ou N para não.")
            continue

    if continuar == "N":
        break

# CODE REQUIREMENT 6 of 8 - final accumulate total value - (pt-br: valor total final acumulado)

print("=" * 64)
print("-" * 14 + f"| Valor total do pedido: R$ {totalPedido:.2f} |" + "-" * 15)
print("=" * 64)

# CODE REQUIREMENT 8 of 8 - relevant comments (added throughout the code) (pt-br: EXIGÊNCIA DO CÓDIGO 6 de 6 - comentários relevantes (adicionados ao longo do código))