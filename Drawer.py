'''
O programa irá sortear um numero entre 1 e 1000, você como
usuário deve tentar advinhar qual é esse numero com base nas
orientações sobre o numero inserido, se ele é maior ou menor do que
o numero sorteado, use este joguinho para treinar o seu pensamento estratégico
tente acertar com a menor quantidade de tentativas possivel
'''

def drawer():
    import random
    rand = random.randint(1,1000)
    numero = 0
    contador = 0
    print("Bem-vindo ao Sorteador! para encerrar a qualquer momento, digite 0")
    user = input("Qual é o seu nome?")
    try:
        dados = open(f"Arquivo{user}.txt", "a")
    except:
        dados = open(f"Arquivo{user}.txt", "w")
    finally:
        while numero != rand:
            contador += 1
            print("Insira o seu palpite abaixo")
            numero2 = int(input(">>"))
            if numero2 == 0:
                dados.close()
                break
            if numero2 > rand:
                print("Você inseriu um numero maior =( tente novamente!")
            elif numero2 < rand:
                print("Você inseriu um numero menor =( tente novamente!")
            else:
                dados.write(f"\nUSER: {user} -- TENTATIVAS: {contador}")
                print("Uhuu! Você acertou, o numero era {}".format(rand))
                print("Numero de tentativas:{}".format(contador))
                continue
