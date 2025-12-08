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

    while True
        try:
            quantidade = float(input("Digite a quantidade de toras (m³): "))

            if quantidade > 2000:
                print("Não aceitamos pedidos com essa quantidade de todas.")
                print("Por favor, digite a quantidade novamente. (Máximo: 2.000)")
                continue

            if 