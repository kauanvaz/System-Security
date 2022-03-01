from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode
from base64 import b64encode

def gerar_chaves(tamanho_key):

    chave_privada = RSA.generate(tamanho_key)
    chave_priv = chave_privada.exportKey()

    chave_publica = chave_privada.publickey()
    chave_publi = chave_publica.exportKey()

    with open('RSA/chave_publica.txt', 'wb') as arq1:
        arq1.write(chave_publi)
    with open('RSA/chave_privada.txt', 'wb') as arq2:
        arq2.write(chave_priv)

while True:
    op = int(input("1. Gerar chaves\n2. Criptografar.\n3. Descriptografar.\n4. Sair.\n"))
    if op == 1:
        tam_key = 0
        op = 0
        while(op!=1 and op!=2 and op!=3):
            op = int(input("Escolha o tamanho da chave: \n1. 1024\n2. 2048\n3. 4096\n"))
            if op==1:
                tam_key = 1024
            elif op==2:
                tam_key = 2048
            elif op==3:
                tam_key = 4096
            else:
                print('Opção inválida! Digite novamente.')
        
        gerar_chaves(tam_key)
        print("CHAVES GERADAS!\n")
    elif op == 2:
        msg = str(input("Digite a mensagem a ser encriptada:\n")).encode('utf-8')
        f = open('RSA/chave_publica.txt', 'rb')
        key = f.read()
        f.close()
        encryptor = PKCS1_v1_5.new(RSA.import_key(key))
        encrypted = b64encode(encryptor.encrypt(msg))
        print("\nMensagem encriptada:\n", encrypted.decode('utf-8'), '\n')
    elif op == 3:
        m_encriptada = input("Digite a mensagem a ser descriptografada: \n").encode('utf-8')
        f = open('RSA/chave_privada.txt', 'rb')
        key2 = f.read()
        f.close()
        decriptor = PKCS1_v1_5.new(RSA.import_key(key2))
        decriptada = decriptor.decrypt(b64decode(m_encriptada), "Erro ao decriptar")
        print('\nMensagem decriptada:\n', decriptada.decode('utf-8'), '\n')
    elif op == 4:
        exit()
    else:
        print("Opção inválida.")