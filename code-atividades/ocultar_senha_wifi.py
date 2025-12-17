def ocultar_senha(senha):
    """
    Recebe uma senha e retorna a versão oculta,
    exibindo apenas os dois últimos caracteres.
    """
    if len(senha) <= 2:
        return "*" * len(senha)
    return "*" * (len(senha) - 2) + senha[-2:]


def main():
    print("=== Ocultador de Senha Wi-Fi ===")

    rede_wifi = input("Digite o nome da rede Wi-Fi: ")
    senha_wifi = input("Digite a senha do Wi-Fi: ")

    senha_oculta = ocultar_senha(senha_wifi)

    print("\nResultado:")
    print(f"Rede Wi-Fi: {rede_wifi}")
    print(f"Senha Oculta: {senha_oculta}")


if __name__ == "__main__":
    main()