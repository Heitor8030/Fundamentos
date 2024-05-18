# Inicializa a variável de controle
contador = 0

# Executa o bloco de código enquanto a condição for verdadeira
while contador < 5:
    print(f"O valor do contador é: {contador}")
    # Incrementa o contador para que a condição eventualmente se torne falsa
    contador += 1

# Após a saída do loop, o valor final do contador será 5
print(f"O loop terminou com o contador em: {contador}")