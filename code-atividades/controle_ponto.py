from datetime import datetime


JORNADA_PADRAO = 8  # horas


def ler_horario(mensagem):
    while True:
        horario = input(mensagem)
        try:
            return datetime.strptime(horario, "%H:%M")
        except ValueError:
            print("❌ Formato inválido. Use HH:MM (24h). Exemplo: 08:00")


def validar_ordem(horarios):
    for i in range(len(horarios) - 1):
        if horarios[i] >= horarios[i + 1]:
            return False
    return True


def calcular_horas_trabalhadas(entrada, saida_almoco, volta_almoco, saida_final):
    periodo_manha = saida_almoco - entrada
    periodo_tarde = saida_final - volta_almoco

    total_segundos = periodo_manha.seconds + periodo_tarde.seconds
    return total_segundos / 3600


def analisar_jornada(horas):
    if horas > JORNADA_PADRAO:
        extra = horas - JORNADA_PADRAO
        return f"Horas trabalhadas: {horas:.2f}h | Horas extras: {extra:.2f}h"
    elif horas < JORNADA_PADRAO:
        falta = JORNADA_PADRAO - horas
        return f"Horas trabalhadas: {horas:.2f}h | Faltaram: {falta:.2f}h"
    else:
        return f"Horas trabalhadas: {horas:.2f}h | Jornada completa"


def main():
    print("=== Controle de Ponto com Intervalo de Almoço ===")
    print("Formato de horário: HH:MM (24h)\n")

    entrada = ler_horario("Horário de entrada: ")
    saida_almoco = ler_horario("Saída para almoço: ")
    volta_almoco = ler_horario("Volta do almoço: ")
    saida_final = ler_horario("Saída final: ")

    horarios = [entrada, saida_almoco, volta_almoco, saida_final]

    if not validar_ordem(horarios):
        print("\n❌ Erro: os horários devem estar em ordem cronológica.")
        return

    horas_trabalhadas = calcular_horas_trabalhadas(
        entrada, saida_almoco, volta_almoco, saida_final
    )

    resultado = analisar_jornada(horas_trabalhadas)

    print("\n📊 Resultado do Dia")
    print(resultado)


if __name__ == "__main__":
    main()
