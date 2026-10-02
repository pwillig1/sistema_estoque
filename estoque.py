#menuEstoque: Opções de operações para o user
def menuSistema():
    print("-----Sistema de Gestão de Estoque-----")
    print("--Menu de Operações--")
    respostaMenu = input("1- Relatório Estoque Atual\n3- Cadastrar Novo Produto\n4- Excluir Produto\n5- ")
    if respostaMenu == "P":
        respostaSubMenu = input("1- Consultar Produto\n2- Atualizar Informações\n3-Excluir Produto")            ##Acoplar funções de modificação/visualização de produto logo abaixo do print da consulta do produto.
#verificaEstoqueExistente
#verificaProdutoExistente
#listaProdutoSeExistente
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

#excluirProduto
#atualizarEstoque
#modificarAtributo    