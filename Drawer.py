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
    user = input("Qual é o seu nome?")
    dados = open(f"Arquivo{user}.txt", "w")
    while numero != rand:
        contador += 1
        print("Insira o seu palpite abaixo")
        numero2 = int(input(">>"))
        if numero2 > rand:
            print("Você inseriu um numero maior =( tente novamente!")
        elif numero2 < rand:
            print("Você inseriu um numero menor =( tente novamente!")
        else:
            dados.write(f"USER: {user} -- TENTATIVAS: {contador}")
            print("Uhuu! Você acertou, o numero era {}".format(rand))
            dados.close()
            print("Numero de tentativas:{}".format(contador))
            continue