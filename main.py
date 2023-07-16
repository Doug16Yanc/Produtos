"Um varejista on-line vende cinco produtos cujos preços no varejo são como a seguir:"
"produto 1, R$ 2,98; produto 2, R$ 4,50; produto 3, R$ 9,98; produto 4, R$ 4,49 e produto 5, US$ 6,87."
"By: Douglas"
def main():

    somaFinal = 0.0
    valorFinal1 = 1
    valorFinal2 = 1
    valorFinal3 = 1
    valorFinal4 = 1
    valorFinal5 = 1

    print("Bem-vindo(a) ao sistema de varejo online:  \n")
    print("============================================\n")
    print("     |         Produto 1 : R$ 2,98         |\n")
    print("     |         Produto 2 : R$ 4,98         |\n")
    print("     |         Produto 3 : R$ 9,98         |\n")
    print("     |         Produto 4 : R$ 4,49         |\n")
    print("     |         Produto 5 : R$ 6,87         |\n")

    produto = int(input("Digite o número do produto (0 para finalizar):\n"))

    while produto != 0:

        if produto != 0:

            if produto == 1:
                quantidade = int(input("Digite a quantidade vendida:\n"))

                valorFinal1 = 2.98*quantidade

                print(f"O valor das vendas do produto 1 é igual a R$ ${valorFinal1:.2f}")

            elif produto == 2:
                quantidade1 = int(input("Digite a quantidade vendida:\n"))

                valorFinal2 = 4.49 * quantidade1

                print(f"O valor das vendas do produto 2 é igual a R$ ${valorFinal2:.2f}")

            elif produto == 3:
                quantidade2 = int(input("Digite a quantidade vendida:\n"))

                valorFinal3 = 9.98 * quantidade2

                print(f"O valor das vendas do produto 3 é igual a R$ ${valorFinal3:.2f}")
            elif produto == 4:
                quantidade3 = int(input("Digite a quantidade vendida:\n"))

                valorFinal4 = 4.49 * quantidade3

                print(f"O valor das vendas do produto 4 é igual a R$ ${valorFinal4:.2f}")
            elif produto == 5:
                quantidade4 = int(input("Digite a quantidade vendida:\n"))

                valorFinal5 = 6.87 * quantidade4

                print(f"O valor das vendas do produto 5 é igual a R$ ${valorFinal5:.2f}")
            else:
                print("Produto inexistente (provavelmente não armazenado no sistema).")

            produto = int(input("Digite o número do produto (0 para finalizar):\n"))


    somaFinal = valorFinal1 + valorFinal2 + valorFinal3 + valorFinal4 + valorFinal5

    print(f"O valor total das vendas de todos os produtos é igual a R$ ${somaFinal:.2f}")

if __name__:
    main()