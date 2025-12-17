import os


def limpar_tela():
    """Limpa o terminal (Windows / Linux / Mac)."""
    os.system("cls" if os.name == "nt" else "clear")


def avaliar_senha(senha):
    pontos = 0

    if len(senha) >= 8:
        pontos += 1
    if any(c.islower() for c in senha):
        pontos += 1
    if any(c.isupper() for c in senha):
        pontos += 1
    if any(c.isdigit() for c in senha):
        pontos += 1
    if any(not c.isalnum() for c in senha):
        pontos += 1

    if pontos <= 2:
        classificacao = "Senha fraca"
    elif pontos <= 4:
        classificacao = "Senha média"
    else:
        classificacao = "Senha forte"

    return pontos, classificacao


def main():
    while True:
        limpar_tela()
        print("=== Avaliador de Senha Wi-Fi (WPA/WPA2) ===")
        print("1 - Avaliar senha")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("\nEncerrando o programa...")
            break

        elif opcao == "1":
            senha = input("\nDigite a senha do Wi-Fi: ")

            if not senha:
                print("\nNenhuma senha foi digitada.")
                input("\nPressione Enter para continuar...")
                continue

            pontos, resultado = avaliar_senha(senha)

            print(f"\nPontuação obtida: {pontos}/5")
            print(f"Resultado: {resultado}")

            input("\nPressione Enter para voltar ao menu...")

        else:
            print("\nOpção inválida.")
            input("\nPressione Enter para tentar novamente...")


if __name__ == "__main__":
    main()

