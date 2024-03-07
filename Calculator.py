''' Iremos construir uma Calculadora para realizar as operações basicas, na construção
usaremos kargs, na mesma, iremos inserir dois numeros e qual tipo de operação
iremos realizar (Adição, subtração, multiplicação ou divisão), em seguida ele deverá retornar o
respectivo resultado
'''

def Calculator(**kwargs):
    if "operation" in kwargs.keys():
        if kwargs["operation"] == "soma" or kwargs["operation"] == "Soma":
            return kwargs["num1"] + kwargs["num2"]
        elif kwargs["operation"] == "subtracao" or kwargs["operation"] == "Subtracao":
            return kwargs["num1"] - kwargs["num2"]
        elif kwargs["operation"] == "multiplicacao" or kwargs["operation"] == "Multiplicacao":
            return kwargs["num1"] * kwargs["num2"]
        elif kwargs["operation"] == "divisao" or kwargs["operation"] == "Divisao":
            if kwargs["num1"] == 0 or kwargs["num2"] == 0:
                return "Não é possivel realizar a divisão por 0"
            return kwargs["num1"] / kwargs["num2"]

#Exemplo de execução no seu arquivo "main.py"

variavel = Calculator(operation="divisao",num1=50,num2=3)
print(variavel)