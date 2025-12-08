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

    # CODE REQUIREMENT 7 of 8 - add a copy of the dictionary to the list
    #(pt-br: EXIGÊCNIA DE CÓDIGO 7 de 8 - adicionar uma cópia na lista do dicionario)

    listaContatos.append(contato.copy())

    print(f"Contato '{nome}' cadastrado com sucesso1")

# CODE REQUIREMENT 4 of 8 - function to consult contacts
# (pt-br: EXIGÊCNIA DE CÓDIGO 4 de 8 - função para consultar contatos)

def consultarContatos():

    while True:
        print('-' * 12 + "Menu de Consulta" + '-' * 12)
        print("1 - Cadastrar Contato")
        print("2 - Consultar Contato(S)")
        print("3 - Remover Contato")
        print("4 - Sair")

        try:
            opcao = int(input("Escolha a opção desejada: "))

        except ValueError:
            print("Opção inválida! Digite um número.")

            continue

        if opcao == 1:
            if not listaContatos:
                print("Nenhum contato cadastrado.")
            else:
                print("-" * 13 + "Todos os Contatos" + "-" * 13)
                for contato in listaContatos:
                 print(f"ID: {contato['id']}")
                 print(f"Nome: {contato['nome']}")
                 print(f"Atividade: {contato['atividade']}")
                 print(f"Telefone: {contato['telefone']}")
                 print("-" * 64)

        elif opcao == 2:

            try:
                idBusca = int(input("Digite o ID do Contato: "))
                encontrado = False

                for contato in listaContatos:
                    if contato['id'] ==idBusca:
                        print("\n--- Contato Encontrado ---")
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        encontrado = True
                        break

                    if not encontrado:
                        print("Contato não encontrado.")

            except ValueError:
                print("ID inválido. Tente novamente.")

        elif opcao == 3:

            atividadeBusca = input("Digite a atividade para busca: ")
            encontrado = []
            
            for contato in listaContatos:
                if contato['atividade']() == atividadeBusca:
                    encontrado.append(contato)

            if not encontrado:
                print(f"Nenhum contato encontrado com a atividade '{atividadeBusca}'")

            else:
                print("Contatos com atividade '{atividadeBusca}:'")

                for contato in encontrado:
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print("-" * 64)

        elif opcao == 4:
            return
        
        else:
            print("Opção inválida!")


# CODE REQUIREMENT 5 of 8: function to remove contact
# (pt-br: EXIGÊNCIA DE CÓDIGO 5 de 8: função para remover contato)

def removerContato():

    while True:
        
        try:
            idRemover = int(input("Digite o ID do contato que deseja remover: "))

            # procurar id

            contatoEncontrado = None
            for contato in listaContatos:
                if contato['id'] == idRemover:
                    contatoEncontrado = contato
                    break

            