def calcular_desconto(produto):
    match produto:
        case "livro":
            desconto = 0.1
        case "eletrônico":
            desconto = 0.2
        case "roupa":
            desconto = 0.15
        case _:
            desconto = 0.0
    return desconto

# Exemplo de uso
produto1 = "livro"
produto2 = "eletrônico"
produto3 = "móvel"

desconto1 = calcular_desconto(produto1)
desconto2 = calcular_desconto(produto2)
desconto3 = calcular_desconto(produto3)

print(f"Desconto para o produto '{produto1}': {desconto1 * 100}%")
print(f"Desconto para o produto '{produto2}': {desconto2 * 100}%")
print(f"Desconto para o produto '{produto3}': {desconto3 * 100}%")