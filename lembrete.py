import datetime

def calcular_dias_restantes(qtd_total, qtd_dia):
    if qtd_dia == 0:
        return 0
    return qtd_total // qtd_dia

def verificar_vencimento(data_vencimento, dias_aviso=7):
    hoje = datetime.date.today()
    dias_restantes = (data_vencimento - hoje).days
    if dias_restantes <= dias_aviso:
        print(f" Atenção: Sua receita vence em {dias_restantes} dia(s)! Revalide com seu médico.")
    else:
        print(f" Sua receita ainda é válida por {dias_restantes} dia(s).")

nome_remedio = input("Digite o nome do medicamento: ")
quantidade = int(input("Quantos comprimidos você tem? "))
uso_diario = int(input("Quantos comprimidos você toma por dia? "))
data_venc_input = input("Digite a data de vencimento da receita (formato AAAA-MM-DD): ")

data_vencimento = datetime.datetime.strptime(data_venc_input, "%Y-%m-%d").date()

dias_restantes = calcular_dias_restantes(quantidade, uso_diario)

print(f"\n Relatório do medicamento '{nome_remedio}':")
print(f" Você possui comprimidos suficientes para {dias_restantes} dia(s).")

if dias_restantes <= 5:
    print("⚠️ Alerta: Seu estoque de remédio está baixo. Reabasteça em breve!")

verificar_vencimento(data_vencimento)

print("\nSimulação dos lembretes diários:")

for dia in range(1, dias_restantes + 1):
    print(f" Dia {dia}: Tomar {uso_diario} comprimido(s) de '{nome_remedio}'.")

print("\n Fim da simulação.")
