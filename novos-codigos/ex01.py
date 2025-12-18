# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.

# Sistema de cadastro de frutas

# Lista que armazena várias strings (frutas)
frutas = []

while True:
    print("\n1 - Adicionar fruta")
    print("2 - Listar frutas")
    print("3 - Buscar fruta")
    print("4 - Remover fruta")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        fruta = input("Digite o nome da fruta: ").strip()

        if fruta:
            frutas.append(fruta)
            print(f"✅ Fruta '{fruta}' adicionada com sucesso!")
        else:
            print("⚠️ Nome inválido. Tente novamente.")

    elif opcao == "2":
        if frutas:
            print("\n📋 Frutas cadastradas:")
            for fruta in frutas:
                print(f"- {fruta}")
        else:
            print("⚠️ Nenhuma fruta cadastrada.")

    elif opcao == "3":
        busca = input("Digite o nome da fruta para buscar: ").strip()

        if busca in frutas:
            print(f"🔍 Fruta '{busca}' encontrada na lista.")
        else:
            print(f"❌ Fruta '{busca}' não encontrada.")

    elif opcao == "4":
        remover = input("Digite o nome da fruta para remover: ").strip()

        if remover in frutas:
            frutas.remove(remover)
            print(f"🗑️ Fruta '{remover}' removida com sucesso.")
        else:
            print(f"❌ Fruta '{remover}' não está na lista.")

    elif opcao == "5":
        print("👋 Encerrando o programa...")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")
