#Vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.


texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

print(" ".join([texto] * numero))
