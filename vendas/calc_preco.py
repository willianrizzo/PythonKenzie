from vendas.formata.format_preco import format_real  #importação relativa

def aumento(valor, porcentagem, formata=False):
    resultado = valor +(valor *(porcentagem / 100))

    if formata:
        resultado = format_real(resultado)
    
    return resultado

def reducao(valor, porcentagem, formata=False):
    resultado = valor - (valor * (porcentagem / 100) )

    if formata:
        resultado = format_real(resultado)

    return resultado