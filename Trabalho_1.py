# CODE REQUIREMENT 1 of 6 - welcome message with name and surname (pt-br: EXIGÊNCIA DO CÓDIGO 1 de 6 - mensagem de boas-vindas com nome e sobrenome)
print("Bem-vindo ao sistema da Sammy Health! Desenvolvido por Samuel Alves Miranda.")

# CODE REQUIREMENT 2 of 6 - price based on age (pt-br: EXIGÊNCIA DO CÓDIGO 2 de 6 - preço baseado na idade)

# request the base value of the heath plan (pt-br: solicitar o valor base do plano de saúde)
valorBase = float(input("Digite o valor base do plano: R$ "))
porcentagem = 0

# request the client age (pt-br: solicitar a idade do cliente)
idade = int(input("Digite a idade do cliente: "))

# CODE REQUIREMENT 3 of 6 - implementation of value rules (pt-br: EXIGÊNCIA DO CÓDIGO 3 de 6 - implementação de regras de valor)
# CODE REQUIREMENT 5 of 6 - use of if, elif and else (pt-br: EXIGÊNCIA DO CÓDIGO 5 de 6 - uso de if, elif e else)
# Requirement 4 is right below; I've combined requirements 3 and 5 because they are complementary.

if idade >= 0 and idade < 19:
    porcentagem = 100 # 100%

elif idade >= 19 and idade < 29:
    porcentagem = 150 # 150%

elif idade >= 29 and idade < 39:
    porcentagem = 225 # 225%

elif idade >= 39 and idade < 49:
    porcentagem = 240 # 250%

elif idade >= 49 and idade < 59:
    porcentagem = 350 # 350%

else:
    porcentagem = 600 # 600%
