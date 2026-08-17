from cryptography.fernet import Fernet

# Carrega a chave gerada anteriormente
with open("chave.key", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

fernet = Fernet(chave)

# Lê o conteúdo original do arquivo
caminho_arquivo = "arquivo.txt"
with open(caminho_arquivo, "rb") as arquivo:
    conteudo_original = arquivo.read()

# Criptografa os dados
conteudo_cifrado = fernet.encrypt(conteudo_original)

# Grava os dados protegidos de volta no arquivo
with open(caminho_arquivo, "wb") as arquivo:
    arquivo.write(conteudo_cifrado)

print("Arquivo protegido com criptografia.")
                                                         
