from cryptography.fernet import Fernet
chave_secreta = Fernet.generate_key()
fernet = Fernet(chave_secreta)

def criptografar(senha):
    return fernet.encrypt(senha.encode()).decode()


chave_secreta = str(input("Digite sua chave secreta: "))
senha_criptografada = criptografar(chave_secreta)


print(f'Senha Criptografada com sucesso!: {senha_criptografada}')

op = input('Deseja visualizar a chave secreta? s/n...\n')
if op == 's':
        print(f'Chave Secreta: {chave_secreta}')
elif op =='n':
        print("Até logo!")
