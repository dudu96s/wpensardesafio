import csv


def cadastro_produtos():

    continuar = True
    tabela = []

    while continuar == True:

        produto = []

        produto.append(str(input('Insira o nome do Produto: ')))
        produto.append(float(input('Insira o preço do Produto: ').replace(',','.')))

        tabela.append(produto)

        resposta = int(input('Deseja adicionar mais um produto?\n(1) - Sim\n(0) - Não\n'))

        if resposta == 0:
            print('Progama Encerrado')
            break
    
    with open('produtos.csv', 'w', newline='') as file:

        writer = csv.writer(file)

        for linha in tabela:
            writer.writerow(linha)
def comprar_produto():
    compras = []
    tabela = []

    while True:
         produto = input("Produto: ")
         quantidade = int(input("Quantidade: "))
         preço = float(input("Preço: "))
         resposta = int(input('Deseja adicionar mais um produto?\n(1) - Sim\n(0) - Não\n'))
         if resposta == 0:
                print('Progama Encerrado')
                break
         compras.append([produto, quantidade, preço])
    soma = 0.0

    tabela.append(compras)


    for e in compras:
         print("%20s x%5d %5.2f %6.2f" % (e[0],
                         e[1],e[2],
                         e[1] * e[2]))
         soma += e[1] * e[2]
    print("Total: %7.2f" % soma)

    with open('compras.csv', 'w', newline='') as file:

        writer = csv.writer(file)

        for linha in compras:
            writer.writerow(linha)      
            