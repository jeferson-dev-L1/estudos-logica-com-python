import re

def validar_nome(nome):
    return len(nome.strip()) >= 3

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None

def validar_idade(idade):
    return idade.isdigit() and 18 <= int(idade) <= 120

def main():
    print("=== Validador de Dados de Cadastro ===")

    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    idade = input("Digite sua idade: ")

    print("\n📋 Resultado da Validação")

    print("✅ Nome válido." if validar_nome(nome) else "❌ Nome inválido.")
    print("✅ E-mail válido." if validar_email(email) else "❌ E-mail inválido.")
    print("✅ Idade válida." if validar_idade(idade) else "❌ Idade inválida (mínimo 18 anos).")

if __name__ == "__main__":
    main()

