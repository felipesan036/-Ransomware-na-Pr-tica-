from cryptography.fernet import Fernet

# Carrega a mesma chave
with open("chave.key", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

fernet = Fernet(chave)

# Lê o arquivo criptografado
caminho_arquivo = "arquivo.txt"
with open(caminho_arquivo, "rb") as arquivo:
    conteudo_cifrado = arquivo.read()

# Descriptografa os dados
conteudo_decriptado = fernet.decrypt(conteudo_cifrado)

# Restaura o arquivo ao estado original
with open(caminho_arquivo, "wb") as arquivo:
    arquivo.write(conteudo_decriptado)

print("Arquivo restaurado ao estado original.")
