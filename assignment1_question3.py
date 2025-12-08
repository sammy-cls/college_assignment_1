# CODE REQUIREMENT 1 of 7 - welcome message with name and surname (pt-br: EXIGÊNCIA DO CÓDIGO 1 de 7 - mensagem de boas-vindas com nome e sobrenome)

print("Bem-vindo à Madeirereira do lenhador Samuel Alves Miranda!")

# CODE REQUIREMENT 2 of 7 - def of wood type (pt-br: def de tipo de madeira)

def escolha_tipo():
    # values of each type of wood per m³ (pt-br: valores de cada tipo de madeira por m³)
    valoresMadeira = {
        "PIN": 150.40, # pinho
        "PER": 170.20, # peroba
        "MOG": 190.90, # mogno
        "IPE": 210.10, # ipê
        "IMB": 220.70 # imbuia
    }

    while True:
        print("Opções de madeira disponíveis:")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peróba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")

        # wood type input with validation (pt-br: input do tipo de madeira com validação)
        tipo = input("Digite o tipo de mandeira desejado (PIN,PER,MOG,IPE,IMB): ")

        if tipo in valoresMadeira:
            return valoresMadeira[tipo]
        else:
            print("Escolha inválida, digite um modelo válido, por gentileza.")

# CODE REQUIREMENT 3 of 7 - amount_woods def (pt-br: def de qnt_toras)

def qtd_toras():

    while True:
        try:
            quantidade = float(input("Digite a quantidade de toras (m³): "))

            if quantidade > 2000:
                print("Não aceitamos pedidos com essa quantidade de todas.")
                print("Por favor, digite a quantidade novamente. (Máximo: 2.000)")
                continue

            if quantidade < 100:
                desconto = 0.00
            elif quantidade < 500:
                desconto = 0.04
            elif quantidade < 1000:
                desconto = 0.09
            elif quantidade <= 2000:
                desconto = 0.16
            else:
                desconto = 0.00
            
            return quantidade, desconto
        
        # CODE REQUIREMENT 6 of 7 - error handling for non-numeric values (pt-br: EXIGÊNCIA DO CÓDIGO 6 de 7 - tratamento de erros para valores não numéricos)
        except ValueError:

            print("Valor inválido! Tente novamente.")

# CODE REQUIREMENT 4 of 7 - def of transportation additional value (pt-br: EXIGÊNCIA DO CÓDIGO 4 de 7 - def do valor do adicional de transporte)

def transporte():

    valoresTransporte = {
        "1": 1000.00, # transporte rodoviario
        "2": 2000.00, # transporte ferroviario
        "3": 2500.00 # transporte hidroviario
    }

    while True:
        # input to select what type of transport (pt-br: input para seleção de que tipo de transporte)
        print("Opções de transporte:")
        print("1 - Transporte Rodoviário - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")
