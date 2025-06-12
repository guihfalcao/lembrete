import datetime

def calcular_dias_restantes_e_fim_estoque(quantidade, uso_diario):
    dias_restantes = quantidade // uso_diario
    hoje = datetime.date.today()
    data_fim_estoque = hoje + datetime.timedelta(days=dias_restantes)
    return dias_restantes, data_fim_estoque

def verificar_vencimento(data_vencimento):
    hoje = datetime.date.today()
    dias_vencimento = (data_vencimento - hoje).days
    if dias_vencimento <= 7:
        return f"  Atenção: Sua receita vence em {dias_vencimento} dia(s)! Revalide com seu médico."
    else:
        return f" Receita válida por mais {dias_vencimento} dia(s)."

medicamentos = []

print("==== Cadastro de Medicamentos ====")

while True:
    nome = input("\nDigite o nome do medicamento: ")
    quantidade = int(input("Quantos comprimidos você tem? "))
    uso_diario = int(input("Quantos comprimidos você toma por dia? "))
    data_venc_input = input("Digite a data de vencimento da receita (DD-MM-AAAA): ")
    data_vencimento = datetime.datetime.strptime(data_venc_input, "%d-%m-%Y").date()

    dias_restantes, data_fim_estoque = calcular_dias_restantes_e_fim_estoque(quantidade, uso_diario)

    vencimento_msg = verificar_vencimento(data_vencimento)

    medicamento = {
        "nome": nome,
        "quantidade": quantidade,
        "uso_diario": uso_diario,
        "data_vencimento": data_vencimento,
        "dias_restantes": dias_restantes,
        "data_fim_estoque": data_fim_estoque
    }

    medicamentos.append(medicamento)

    continuar = input("Deseja adicionar outro medicamento? (s/n): ").lower()
    if continuar != 's':
        break

print("\n==== Relatório de Medicamentos ====\n")

for med in medicamentos:
    print(f" Medicamento: {med['nome']}")
    print(f" - Estoque: {med['quantidade']} comprimido(s)")
    print(f" - Uso diário: {med['uso_diario']} comprimido(s)")
    print(f" - Dura por mais {med['dias_restantes']} dia(s)")
    print(f" - Data estimada de fim do estoque: {med['data_fim_estoque'].strftime('%d/%m/%Y')}")
    print(vencimento_msg)
    
    if med["dias_restantes"] <= 5:
        print("Alerta: Estoque de remédio baixo. Reabasteça em breve!")
    
    print(" Simulação dos lembretes diários:")
    for dia in range(1, med["dias_restantes"] + 1):
        print(f"  Dia {dia}: Tomar {med['uso_diario']} comprimido(s) de '{med['nome']}'.")
    
    print("\n--------------------------------------\n")

print("Fim do relatório.")
