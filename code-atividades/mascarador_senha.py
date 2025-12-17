def mascarar_senha(valor):
    return "*" * (len(valor) - 2) + valor[-2:]


def mascarar_wifi(valor):
    return "*" * (len(valor) - 2) + valor[-2:]


def mascarar_cpf(valor):
    return f"***.***.***-{valor[-2:]}"


def mascarar_cartao(valor):
    return "**** **** **** " + valor[-4:]


def mascarar_email(valor):
    try:
        usuario, dominio = valor.split("@")
        return usuario[0] + "***@" + dominio
    except ValueError:
        return "❌ E-mail inválido"


def mascarar_telefone(valor):
    if len(valor) < 10 or not valor.isdigit():
        return "❌ Telefone inválido"

    ddd = valor[:2]
    final = valor[-4:]
    return f"({ddd}) *****-{final}"


def menu():
    print("\n=== Mascarador de Dados Sensíveis ===")
    print("1 - Senha")
    print("2 - Wi-Fi")
    print("3 - CPF")
    print("4 - Cartão de Crédito")
    print("5 - E-mail")
    print("6 - Telefone")
    print("0 - Sair")

    opcao = input("Escolha o tipo de dado: ")

    if opcao == "0":
        return False

    valor = input("Digite o valor a ser mascarado: ")

    if opcao == "1":
        print("Resultado:", mascarar_senha(valor))
    elif opcao == "2":
        print("Resultado:", mascarar_wifi(valor))
    elif opcao == "3":
        if len(valor) != 11 or not valor.isdigit():
            print("❌ CPF inválido")
        else:
            print("Resultado:", mascarar_cpf(valor))
    elif opcao == "4":
        print("Resultado:", mascarar_cartao(valor))
    elif opcao == "5":
        print("Resultado:", mascarar_email(valor))
    elif opcao == "6":
        print("Resultado:", mascarar_telefone(valor))
    else:
        print("❌ Opção inválida")

    return True


def main():
    while True:
        continuar = menu()
        if not continuar:
            print("\n👋 Encerrando o programa.")
            break


if __name__ == "__main__":
    main()
