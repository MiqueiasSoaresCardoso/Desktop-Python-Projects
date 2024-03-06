'''
banner = "O Emac 2024 vem aí!"
igreja_sede = "IEC TANCREDO NEVES"
data = "15 de Novembro de 2024"
banner.lower()
# deixa tudo em minuscúlo
print(banner.lower())
# deixa tudo em caixa alta

# com o replace é possivel alterar um determinado dado de uma String
print(banner.replace("2024", "2025"))
# com o rfind ele busca de traz para frente o texto selecionado
print(banner.rfind("Emac"))
# com o find ele faz a busca de forma linear, natural, ambos mostram o indice que a variavel se inicia
print(banner.find("Emac"))

# essa função inverte todo o meu texto
# banner = banner[::-1]
print(banner)

# neste caso eu estou fazendo a concatenação desse texto 10 vezes
# banner = banner * 10
print(banner)

# podemos multiplicar ou concatenar textos
concatenacao = banner + igreja_sede + data
print(concatenacao)

num1 = 7
num2 = 10
resultado = num1 / num2
#elevado a
print(resultado ** 2)'''

# nome = input("Inira o nome do evento: ")
# data = input("Insira a data")
# valor = float(input("Qual é o valor da entrada?"))
# juros = float(input("Qual é a taxa de juros do cartão?"))
# total = valor + (juros/10)
# print("EVENTO: " + nome + " DATA: " + "VALOR: {} VALOR NO CARTÃO  {}".format(valor,total))


# numero = int(input("Insira um numero >"))
#
# if numero >= 3:
#     print("Parabéns, seu curso é bem avalidao!")
#
# elif numero < 3:
#     print("Você não te a qualificação necessária +(")
# else:
#     print("Nota invalida")

# dados = input("Insira um dado: ")
#
# if dados.isalpha():
#     print("é um texto!")
#
# if dados.isnumeric():
#     print("é um número")
#

#Exercicio 1 - 29/02/2024

# exc 01

# num1 = int(input("Insira um numero: "))
# num2 = int(input("Insira outro numero: "))
#
# if num1 > num2:
#     print("{} é maior que {}" .format(num1,num2))
# else:
#     print("o numero {} é o maior".format(num2))

#exc 02

# linguagem = input("Insira a sua linguagem de programação preferida:")
# linguagemof = linguagem.isupper()
# if linguagemof != "PYTHON" :
#     print("Opps! Opção incorreta.")
# else:
#     print("Show")

# idade = int(input("Digite a sua idade>"))
# tembolsa = bool(input("Tem bolsaFamilia?"))
# temCadUnico = bool(input("Tem cadÚnico?"))
#
# if idade >= 18 and idade < 25 and (tembolsa == True or temCadUnico == True):
#     print("Parabéns! Você pode solictar o seu Id Jovem!")
# else:
#     print("Opps! Você não pode solicitar esse beneficio =(")

# lista = ["Java", "Python","C#", "C","Javascript"]
# print(lista)
# lista.append("Ruby") #adiciona itens a lista
# print(lista)
# #lista.sort() #ordena os itens de forma crescente/alfabetica
# print(lista)
# print(lista.index("Ruby")) #exibe o indice do objeto selecionado
# print(lista[2])
# print(lista[1:4])
#
# print(len(lista))
# lista2 = ["Lua","Elixir","Portugol","Egua"]

# produtos = ["mouse gtx", "teclado multi", "Webcam Intel","Adptador bluetooh","suporte de note"]
# print(produtos)
# print("Itens Disponivéis, selecione os que voce deseja (03 itens)")
# carrinho = []
# item1 = input("1 >")
# item2 = input("2 >")
# item3 = input("3 >")
# carrinho.append(item1)
# carrinho.append(item2)
# carrinho.append(item3)
# print("deseja finalizar?")
# resposta = bool(input())
# if resposta == True:
#     final = ["Notebook Dell Inspiron 153000"]
#     final.extend(carrinho)
#     print("SEGUE O SEU HISTÓRICO DE COMPRAS {}".format(final))

#tuplas são listas imutáveis onde eu posso armazenar dados que eu não quero que sofra alteração

# tupla = (1,45,78,54,890,900)
# print(tupla)
# print(len(tupla)) #tamanho da tupla
# print(max(tupla)) #qual é o seu maior item
# print(min(tupla)) #qual é o seu menos item
# print(tupla.count(1)) #quantos itens desse tipo eu tenho?

# sets = {1,4,6,4,7,9,90,67,4} #variavél semelhante a lista, porém que não permite variaveis repetidas
# print(sets)
# #adicionando itens
# sets.add(45)
# print(sets)
# #removendo itens
# sets.remove(1)
# '''neste caso ele irá buscar o item a todo o custo e
# caso não o encontre, ele exibirá um erro
# '''
# sets.discard(1)
# '''neste caso, se o item existir ele removerá
# se não, ele contiará o seu caminho sem a exibição de erros
# '''

# print("Digite 05 numeros entre 1 e 5")
# lista = []
# num01 = int(input("NUM01>"))
# if num01 > 1 and num01 < 5:
#     lista.append(num01)
# else:
#     print("Numero Inválido")
#
# num01 = int(input("NUM01>"))
# if num01 > 1 and num01 < 5:
#     lista.append(num01)
# else:
#     print("Numero Inválido")
#
# num01 = int(input("NUM01>"))
# if num01 > 1 and num01 < 5:
#     lista.append(num01)
# else:
#     print("Numero Inválido")
#
# print(lista)

# lista = ["Python", "Análise de Dados", "Power BI"]
# linguagem = input("Adicione a sua linguagem de Programação")
# if linguagem not in lista:
#     lista.append(linguagem)
#     print("Adicionado com sucesso!")
#     print(lista)
# else:
#     print("Opps! Já temos está opção!")
#
# #nova versão
#
#
# if input("Adicione a sua linguagem de Programação") not in lista:
#     print("Não está na lista")

#dictionary
#é uma estrutura que armazena dados com keys e values

# usuario = {"name": "Miqueias", "Age": 20, "profession": "Teacher and developer", "Conviction": "Yes","fault": "yes"}
# print(usuario)
# usuario["Age"] = 21
# print(usuario)
# print(usuario["profession"])
#
# # data removal
#
# #del
# print(usuario)
# #presents errors
# del usuario["Conviction"]
# print(usuario)
# # removal data,trata os errors
# usuario.pop("fault",print("Não há mais fault"))
# usuario.pop("date", None)
# print(usuario)
#
# lista =["Java","Ruby"]
# print(lista)
# #lista.remove("python")
# lista.pop(1)
# print(lista)
#
# #exibir todas as keys, ou todos os values
# print(usuario.keys())
# print(usuario.values())
# biography = {"description": "Cristão Reformado, Analista de Sistemas pelo Unifip e Mestrando pelo IFPB", "instagram": "@miqueiassoarescardoso"}
# print(biography)
# #juntando
# usuario.update(biography)
# print(usuario)

#criando uma lista com o Range

#crescente
# numeros_0_100 = range(0,100)
# print(list(numeros_0_100))
#
# #decresente
# numeros_0_100d = range(100,0,-1)
# print(list(numeros_0_100d))
#
# #escolhe os passos
# numeros_0_100_de_02 = range(0,100,2)
# print(list(numeros_0_100_de_02))



#Usando o While True
# soma = 0
# while True:
#     numeros = float(input("Insira um numero(Para realizar a soma digite 0)>>"))
#     if numeros == 0:
#         break
#     soma += numeros
# print("total:{} ".format(soma))

# soma = 0
# for i in range(4):
#     numero = int(input("insira numeros entre 1 e 5>"))
#     if numero > 5 or numero < 1:
#         continue
#         print("teste")
#
#     soma += numero
# print(soma)



dicionary = {"Nome": "Miqueias Soares", "Age": 20, "Sex": "Masculino", "Profession": "Teacher and developer"}

#lendo o dictionary a partir de um for

#imprimindo os dados
# for keys in dicionary.keys():
#     print(keys)
#
# for dados in dicionary:
#     print(dados)
#
# for values in dicionary.values():
#     print(values)
#
# for data in dicionary.items():
#     print(data)
#
# for data,data2 in dicionary.items():
#     print(data,data2)
#o Import com o * importa tudo
from Function import *

# from  Function import calculate_average
calculate_average(6)
# porcentagem = percentage(100,20)
# print(f"Impostos sobre os produtos {porcentagem} % ")
#requestdata()
#
# import Drawer
#
# Drawer.drawer()