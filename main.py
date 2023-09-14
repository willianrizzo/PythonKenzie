from vendas.calc_preco import aumento
from vendas.calc_preco import reducao

def main(): #criando função
    # print(__name__)
    preco = 49.90
    preco_com_aumento = aumento(preco, 15, True)
    preco_com_reducao = reducao(preco, 15, True)

    print(preco_com_aumento)
    print(preco_com_reducao)
    
if __name__ == "__main__":
    main()