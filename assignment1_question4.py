# Business Contact Management Software

# CODE REQUIREMENT 1 of 8 welcome message with name and surname
# (pt-br: EXIGÊNCIA DO CÓDIGO 1 de 8 - mensagem de boas-vindas com nome e sobrenome)

print('=' * 4 + " Bem-vindo à lista de Contatos do Samuel Alves Miranda! " + '=' * 4)
print("=" * 64)
print('-' * 25 + "Menu Principal" + '-' * 25)

# CODE REQUIREMENT 2 of 8 - list of contacts and variable id_global with RU value
# (pt-br: EXIGÊNCIA DO CÓDIGO 2 de 8 - lista_contatos e a variável id_global com valor igual ao número de meu RU)

listaContatos = []
id_global = 5517944

# CODE REQUIREMENT 3 of 8 - function to register contact
# (pt-br: EXIGÊNCIA DO CÓDIGO 3 de 8- função para cadastrar contato

def cadastrarContato(id):

    print('-' * 21 + f"Id do contato: {id}" + '-' * 21)
    nome = input("Por favor, digite o nome do Contato:")
    atividade = input("Por favor, digite a Atividade do contato: ")
    telefone = input("Por favor, digiteo Telefone do contato: ")

    contato= {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }