senha_certa = "senha99"
tentativa = input("Digite a senha:")

while tentativa != senha_certa:
    print("Senha incorreta. Tente novamente.")
    tentativa = input("Digite a senha:")

print("Senha correta")