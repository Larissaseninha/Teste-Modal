import csv
import datetime
def exibir_menu():
    print("\nMODAL GR - GERENCIAMENTO")
    print("1. Aniversariantes do Mes")
    print("2. Emprestimo")
    print("3. Sair")

while True:
    exibir_menu()
    opcao = input("Insira a opção desejada: ")

    if opcao == "1":
        print("\nVocê escolheu a Opção Aniversariantes do Mes")

        data_atual = datetime.datetime.now()
        mes_atual = data_atual.month

        arquivo_saida = f'aniversariantes_do_mes_{mes_atual}.txt'

        with open(arquivo_saida, 'w', newline='') as saida:
            writer = csv.writer(saida, delimiter='|')

            with open('consultores.txt', 'r') as entrada:
                reader = csv.reader(entrada, delimiter='|')

                next(reader)

                for linha in reader:
                    nome, _, data_nascimento = linha[0], linha[1], linha[2]
                    _, mes_nascimento, _ = data_nascimento.split('/')
                    mes_nascimento = int(mes_nascimento)

                    if mes_nascimento == mes_atual:
                        writer.writerow([nome, data_nascimento])

        print(f"O Arquivo com os aniversariantes do mês {mes_atual} foi salvo em: {arquivo_saida}")


    elif opcao == "2":
        print("\n******Você escolheu a Opção Emprestimo******\n")
        print("Digite seu nome: ")
        nome = input()
        print("Digite seu tempo de casa (apenas numeros inteiros): ")
        tempo = int(input())
        if tempo < 5:
            print("Agradecemos seu interesse,",nome,",mas voce não atende os requisitos minimos do programa!")
            break
        salario = float(input("Digite seu salario: "))


        if salario % 2 == 0 or salario % 5 ==0:
            print("[Escolha o tamanho das notas que deseja sacar]")
            print("1-Notas de maior valor")
            print("2-Notas de menor valor")
            print("3-Notas meio a meio")
            tamanho_cedulas = int(input("Escolha o tamanho das Cedulas: "))

            emprestimo = salario*2
            notas_100 = 0
            notas_50 = 0
            notas_20 = 0
            notas_10 = 0
            notas_5 = 0
            notas_2 = 0

            if tamanho_cedulas == 1:
                while emprestimo >= 100:
                    notas_100 +=1
                    emprestimo -=100

                while emprestimo >= 50:
                    notas_50 += 1
                    emprestimo -= 50

                while emprestimo >= 20:
                    notas_20 += 1
                    emprestimo -= 20

                while emprestimo >= 10:
                    notas_10 += 1
                    emprestimo -= 10

                while emprestimo >= 5:
                    notas_5 += 1
                    emprestimo -= 5

                while emprestimo >= 2:
                    notas_2 += 1
                    emprestimo -= 2

                print("\n")
                print(f"Simulacao do Emprestimo no valor de: {salario * 2}")
                print(f"Notas de 100 reais: {notas_100}")
                print(f"Notas de 50 reais: {notas_50}")
                print(f"Notas de 20 reais: {notas_20}")
                print(f"Notas de 10 reais: {notas_10}")
                print(f"Notas de 5 reais: {notas_5}")
                print(f"Notas de 2 reais: {notas_2}")


            if tamanho_cedulas == 2:

                while emprestimo >= 2:
                    notas_2 += 1
                    emprestimo -= 2

                while emprestimo >= 5:
                    notas_5 += 1
                    emprestimo += 5

                while emprestimo >= 10:
                    notas_10 += 1
                    emprestimo -= 10

                while emprestimo >= 20:
                    notas_20 += 1
                    emprestimo -= 20

                while emprestimo >= 50:
                    notas_50 += 1
                    emprestimo -= 50

                while emprestimo >= 100:
                    notas_100 += 1
                    emprestimo -= 100

                print("\n")
                print(f"Simulacao do Emprestimo no valor de: {salario * 2}")
                print(f"Notas de 100 reais: {notas_100}")
                print(f"Notas de 50 reais: {notas_50}")
                print(f"Notas de 20 reais: {notas_20}")
                print(f"Notas de 10 reais: {notas_10}")
                print(f"Notas de 5 reais: {notas_5}")
                print(f"Notas de 2 reais: {notas_2}")

            if tamanho_cedulas == 3:
                print(f"\nSimulacao do Emprestimo no valor de: {salario * 2}")
                emprestimo_meta = (emprestimo/2)

                while emprestimo_meta >= 100:
                    notas_100 +=1
                    emprestimo_meta -=100

                while emprestimo_meta >= 50:
                    notas_50 += 1
                    emprestimo_meta -= 50

                while emprestimo_meta >= 20:
                    notas_20 += 1
                    emprestimo_meta -= 20

                while emprestimo_meta >= 10:
                    notas_10 += 1
                    emprestimo_meta -= 10

                while emprestimo_meta >= 5:
                    notas_5 += 1
                    emprestimo_meta -= 5

                while emprestimo_meta >= 2:
                    notas_2 += 1
                    emprestimo_meta -= 2

                print("\n")
                print(f"Notas de 100 reais: {notas_100}")
                print(f"Notas de 50 reais: {notas_50}")
                print(f"Notas de 20 reais: {notas_20}")
                print(f"Notas de 10 reais: {notas_10}")
                print(f"Notas de 5 reais: {notas_5}")
                print(f"Notas de 2 reais: {notas_2}")

                while emprestimo_meta >= 2:
                    notas_2 += 1
                    emprestimo_meta -= 2

                while emprestimo_meta >= 5:
                    notas_5 += 1
                    emprestimo_meta += 5

                while emprestimo_meta >= 10:
                    notas_10 += 1
                    emprestimo_meta -= 10

                while emprestimo_meta >= 20:
                    notas_20 += 1
                    emprestimo_meta -= 20

                while emprestimo_meta >= 50:
                    notas_50 += 1
                    emprestimo_meta -= 50

                while emprestimo_meta >= 100:
                    notas_100 += 1
                    emprestimo_meta -= 100

                print("\n")
                print(f"Notas de 100 reais: {notas_100}")
                print(f"Notas de 50 reais: {notas_50}")
                print(f"Notas de 20 reais: {notas_20}")
                print(f"Notas de 10 reais: {notas_10}")
                print(f"Notas de 5 reais: {notas_5}")
                print(f"Notas de 2 reais: {notas_2}")

        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Insira um valor válido!")
        break;