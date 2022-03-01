from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
from base64 import b64encode


class Encriptador:

    def encriptar(self, message, iv, key):
        cifra = AES.new(key, AES.MODE_CBC, iv=iv)
        return cifra.encrypt(pad(message, AES.block_size))

    def decriptar(self, ciphertext, iv, key):
        cifra = AES.new(key, AES.MODE_CBC, iv=iv)
        plaintext = cifra.decrypt(ciphertext)
        return unpad(plaintext, AES.block_size)
    
    def inserir_chave(self):
        key = b''
        aux = ''

        tam_key = 0
        op = 0
        while(op!=1 and op!=2 and op!=3):
            op = int(input("Escolha o tamanho da chave: \n1. 128\n2. 192\n3. 256\n"))
            if op==1:
                tam_key = 128
            elif op==2:
                tam_key = 192
            elif op==3:
                tam_key = 256
            else:
                print('Opção inválida! Digite novamente.')

        print("Insira uma chave (" + str(int(tam_key/8)) + " caracteres): ")
        while(len(aux) != int(tam_key/8)):
            aux = str(input())
            if(len(aux) != int(tam_key/8)):
                print('CHAVE SECRETA COM TAMANHO DIFERENTE DE ' + str(int(tam_key/8)) +'. DIGITE NOVAMENTE: ')
            else:
                key = aux.encode('utf-8')
        return key

    def inserir_iv(self):
        iv = '-'
        while(len(iv) != 0 and len(iv) != 16):
            iv = str(input("\nInsira o IV (16 caracteres). Não desejando, pressione Enter: \n"))
            if len(iv) == 0:
                return 'encryptionIntVec'.encode('utf-8')
            elif len(iv) == 16:
                return iv.encode('utf-8')
            else:
                print("IV INVÁLIDO (16 CARACTERES)!")
        
enc = Encriptador()

while True:
    op = int(input("1. Criptografar.\n2. Descriptografar.\n3. Sair.\n"))
    if op == 1:
        msg = str(input("Digite a mensagem a ser criptografada: \n")).encode('utf-8')
        iv = enc.inserir_iv()
        with open('AES/iv.txt', 'wb') as file:
            file.write(iv)

        key = enc.inserir_chave()
        with open('AES/chave.txt', 'wb') as file:
            file.write(key)

        m_encriptada = b64encode(enc.encriptar(msg, iv, key))
        print("\nMensagem encriptada: ", m_encriptada.decode('utf-8'), '\n')
    elif op == 2:
        cifra = str(input("Digite a mensagem a ser descriptografada: \n")).encode('utf-8')
        iv = enc.inserir_iv()
        key = enc.inserir_chave()
        m_decriptada = enc.decriptar(b64decode(cifra), iv, key)
        print("\nMensagem decriptada: ", m_decriptada.decode('utf-8'), '\n')
    elif op == 3:
        exit()
    else:
        print("Opção inválida.")