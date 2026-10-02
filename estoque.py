def cadastraProduto(estoque):
    nomeProdutoNovo = input("Insira o nome do produto:")
    categoriaProdutoNovo = input("Insira a categoria do produto:")
    qtdeProdutoNovo = int(input("Insira a quantidade do produto:"))
    precoProdutoNovo = float(input("Insira o preço do produto:"))
    codigoProdutoNovo = input("Insira o código do produto:")

    produto = {
        'nome': nomeProdutoNovo,
        'categoria': categoriaProdutoNovo,
        'qtde': qtdeProdutoNovo,
        'preço': precoProdutoNovo,
        'código': codigoProdutoNovo
    }
    
    estoque.append(produto)
    print(estoque)