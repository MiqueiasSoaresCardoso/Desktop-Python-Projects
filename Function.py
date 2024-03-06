'''
Com as funções você organiza o seu programa em blocos ou modulos
e pode utilizar essas funções onde quiser, sem a repetição de
códigos, além disso deixa o código mais legivel
'''

def requestdata():
    import time
    for i in range(3):
        print("Solicitando dados....")
        time.sleep(5)
    else:
        print("Opps! Não foi possivél acessar os dados")

'''
é possivel termos valores pré-definidos nos argumentos, e caso o 
usuário não insira nada, já teremos um valor padrão
'''
def calculate_average(qtdsoma = 3):
    nota = 0
    for i in range(qtdsoma):
        insercao = float(input("Insira a {} nota!>>".format(i+1)))
        nota = nota + insercao
    print("O seu CAC é {}".format(nota/qtdsoma))
    if nota/qtdsoma >= 7:
        print("Candidato classificado")
    else:
        print("Candidato não classificado =(")

#Nesta função estamos trabalhando com Argumentos e o Return
def percentage(numero, porcentagem):
    result = (porcentagem/100 * numero)
    return result

''' O Return nos permite retornar dados de uma função, de forma que você pode armazenar
e manipular esse dado da forma que desejar, em qualquer lugar, utilizando de acordo
com a sua regra de negócio'''

#Trabalhando com args

#O Args nos permite inserir uma infinidade de argumentos,sem limite pré-definido
def soma(*args):
    #os dados são aramzenados em forma similar a uma lista,e podem ser de varios tipos
    soma = 0
    #para acessar cada um individualmente podemos utilizar uma estrutura de repetição como o for
    if args != None:
        for arg in args:
            soma += arg
    if soma != None:
        return soma

#Temos também o Kargs que atua armazenando os dados como um dicionário

def dataperson(**kwargs):
    if "action" in kwargs.keys():
        if kwargs["action"] == "soma":
            return kwargs["num1"] + kwargs["num2"]
        elif kwargs["action"] == "subtracao":
            return kwargs["num1"] - kwargs["num2"]
        if kwargs["action"] == "divisao":
            return kwargs["num1"] / kwargs["num2"]
        elif kwargs["action"] == "multiplicacao":
            return kwargs["num1"] * kwargs["num2"]

#Teste assim no seu arquivo main.py
'''result = dataperson(action="soma",num1=12,num2=12)
print(result)'''

