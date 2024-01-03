print("Seja bem vindo".center(20, '#').title())
print("Deseja utilizar nossos serviços?".center(30).title())
print(''' 
1---Sim
2---Não '''.strip())

option = int(input())
saldo = 0
extrato = ""
saque = 0
LIMITE_DE_SAQUE = 500
NUMERO_DE_SAQUES = 3

if option == 1:
    while True:
        print(''' 
    [D]---Depósito
[S]---Saque
[E]---Extrato
[Q]---Sair
'''.lstrip())
        menu = input().upper()

        if menu == "D":
            deposito = float(input("Digite o valor do depósito: "))
            saldo += deposito
            extrato += f'Depósito: +{deposito}\n'

        elif menu == "S":
            if saque < NUMERO_DE_SAQUES:
                valor_saque = float(input("Digite o valor do saque: "))
                if valor_saque <= saldo and valor_saque <= LIMITE_DE_SAQUE:
                    saldo -= valor_saque
                    extrato += f'Saque: -{valor_saque}\n'
                    saque += 1
                else:
                    print("Saque inválido. Verifique seu saldo e limite de saque.")
            else:
                print("Você atingiu o número máximo de saques.")

        elif menu == "E":
            print(f"Saldo: {saldo}")
            print("Extrato:")
            print(extrato)

        elif menu == "Q":
            print('Obrigado por utilizar nossos serviços.')
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")
else:
    print('Obrigado por utilizar nossos serviços.')
          
