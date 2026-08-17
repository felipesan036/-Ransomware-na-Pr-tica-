from cryptography.fernet import Fernet

# Gera uma chave aleatória e segura
chave = Fernet.generate_key()

# Salva a chave em um arquivo para uso posterior
with open("chave.key", "wb") as arquivo_chave:
    arquivo_chave.write(chave)

print("Chave gerada e salva com sucesso.")
