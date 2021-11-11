while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao nosso   ")
    print("   SIMULADOR DE INVESTIMENTO   ")
    print("-------------------------------")

    cliente = str(input("Você já é nosso cliente? s/n: "))

    if cliente == 'n':
        tarifa = 10
        juros = 0.04
    else:
        juros = 0.05
        tarifa = 0

    valor = int(input("Valor que deseja investir: "))

    if cliente == 's':
      soma = ((1 + 0.05) * valor)

      print("-------------------------------")
      print("   RESULTADO DA SIMULAÇÃO      ")
      print("      DE INVESTIMENTO          ")
      print("-------------------------------")
      print("Valor a resgatar: " ,soma)

    else:
      soma2 = ((1 + 0.04) * valor) - 10

      print("-------------------------------")
      print("   RESULTADO DA SIMULAÇÃO      ")
      print("      DE INVESTIMENTO          ")
      print("-------------------------------")
      print("Valor a resgatar: " ,soma2)

      opcao = str(input("Deseja realizar outra simulação? s/n "))

      if opcao == 'n':
          print("Simulação encerrada!")
          break