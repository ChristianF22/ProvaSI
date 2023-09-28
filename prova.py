import os
from cryptography.fernet import Fernet
import hashlib

path = r'C:\Users\1-2022122060\Desktop\ProvaSegurança\prova2.txt.txt'

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chaveparadesbloquear.txt", "wb") as chave_arquivo:
        chave_arquivo.write(chave)

def carregar_chave():
    if os.path.isfile("chaveparadesbloquear.txt"): 
        with open("chaveparadesbloquear.txt", "rb") as chave_arquivo:
            return chave_arquivo.read()
    else:
        gerar_chave()
        return carregar_chave() 

def criptografar_mensagem(mensagem, chave):
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    return mensagem_criptografada

if os.path.isfile(path): 
    with open(path, "r") as arquivo:
        mensagem = arquivo.read()

    print(f"A mensagem no arquivo: {path} foi criptografada com sucesso!")

    chave = carregar_chave()

    mensagem_criptografada = criptografar_mensagem(mensagem, chave)

    hash_mensagem_criptografada = hashlib.sha256(mensagem_criptografada).hexdigest()
    
    print(f"O hash da mensagem que foi criptografada: {hash_mensagem_criptografada}")

else:
    print(f"O arquivo {path} não foi encontrado.")
