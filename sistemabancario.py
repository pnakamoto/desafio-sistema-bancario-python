menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Meta de Poupança
[5] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
meta_poupanca = None  # Funcionalidade extra implementada no desafio 
progresso_poupanca = 0

def format_currency(value):
    """Formata o valor como moeda brasileira."""
    return f"R$ {value:.2f}"

def verificar_meta():
    """Verifica se a meta de poupança foi atingida."""
    global progresso_poupanca, meta_poupanca
    if meta_poupanca is not None and progresso_poupanca >= meta_poupanca:
        print("\n******** PARABÉNS ********")
        print("Você atingiu sua meta de poupança!")
        print("***************************")
        # A meta é removida após atingir o objetivo
        meta_poupanca = None

while True:
    opcao = input(menu)

    if opcao == "1":  # Depósito
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: {format_currency(valor)}\n"
            print(f"Depósito realizado com sucesso: {format_currency(valor)}")
            
            # Atualiza o progresso da poupança se houver uma meta
            if meta_poupanca is not None:
                progresso_poupanca += valor
                print(f"Você avançou {format_currency(valor)} em direção à sua meta de poupança!")
                verificar_meta()
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":  # Saque
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {format_currency(valor)}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso: {format_currency(valor)}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":  # Extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {format_currency(saldo)}")
        print("==========================================")

    elif opcao == "4":  # Meta de Poupança
        if meta_poupanca is None:
            meta_poupanca = float(input("Informe o valor da sua meta de poupança: "))
            if meta_poupanca > 0:
                print(f"Meta de poupança definida: {format_currency(meta_poupanca)}.")
            else:
                print("Operação falhou! O valor da meta deve ser positivo.")
                meta_poupanca = None
        else:
            print("\n======== META DE POUPANÇA ========")
            print(f"Meta definida: {format_currency(meta_poupanca)}")
            print(f"Progresso atual: {format_currency(progresso_poupanca)}")
            restante = max(0, meta_poupanca - progresso_poupanca)
            if progresso_poupanca >= meta_poupanca:
                print("Parabéns! Você atingiu sua meta de poupança!")
            else:
                print(f"Falta: {format_currency(restante)} para atingir sua meta.")
            print("===================================")

    elif opcao == "5":  # Sair
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
