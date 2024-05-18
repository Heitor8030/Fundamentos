def convert_units():
    """
    Função que converte diferentes unidades de medida.
    """
    print("Bem-vindo ao Conversor de Unidades de Medida!")

    while True:
        try:
            # Solicitar a unidade de entrada e o valor
            print("\nUnidades disponíveis:")
            print("1. Comprimento (metros, centímetros, milímetros, etc.)")
            print("2. Massa (quilogramas, gramas, miligramas, etc.)")
            print("3. Volume (litros, mililitros, etc.)")
            unit_type = int(input("Escolha o tipo de unidade (1-3): "))

            if unit_type == 1:
                unit_from = input("Digite a unidade de entrada (ex: metros): ")
                value_from = float(input("Digite o valor: "))
                unit_to = input("Digite a unidade de saída (ex: centímetros): ")
                conversion_factors = {
                    "metros": 1, "centímetros": 100, "milímetros": 1000, "quilômetros": 0.001
                }
            elif unit_type == 2:
                unit_from = input("Digite a unidade de entrada (ex: quilogramas): ")
                value_from = float(input("Digite o valor: "))
                unit_to = input("Digite a unidade de saída (ex: gramas): ")
                conversion_factors = {
                    "quilogramas": 1, "gramas": 1000, "miligramas": 1000000
                }
            elif unit_type == 3:
                unit_from = input("Digite a unidade de entrada (ex: litros): ")
                value_from = float(input("Digite o valor: "))
                unit_to = input("Digite a unidade de saída (ex: mililitros): ")
                conversion_factors = {
                    "litros": 1, "mililitros": 1000
                }
            else:
                print("Opção inválida. Tente novamente.")
                continue

            # Realizar a conversão
            if unit_from in conversion_factors and unit_to in conversion_factors:
                value_to = value_from * (conversion_factors[unit_to] / conversion_factors[unit_from])
                print(f"{value_from:.2f} {unit_from} equivalem a {value_to:.2f} {unit_to}.")
            else:
                print("Unidade de medida inválida. Tente novamente.")
                continue

            # Perguntar se o usuário deseja fazer outra conversão
            choice = input("Deseja fazer outra conversão? (s/n) ").lower()
            if choice != "s":
                print("Obrigado por usar o Conversor de Unidades!")
                break

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Executar o conversor
convert_units()