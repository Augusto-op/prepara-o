#Solicita o nome do usuário
nome = input("Olá! Qual é o seu nome?")

#Solicita a distância percorrida (em km)
distancia = float(input("Digite a distância percorrida (em km):"))

#Solicita a quantidade de combustível gasto (em litros)
litros = float(input("Digite a quantidade de combustível gasto (em litros):"))

#calcular o comsumo medio
consumo_medio = distancia / litros

#exibe o consumo medio da ultima casa decimais
print(f"/n{nome}, o consumo medio do deu veiculo foi {consumo_medio:.2f}km/l.")

#classifique o consumo medio e exibe a mensagem correspondente
if consumo_medio < 8.0:
    print("Classificacao: alto consumo")
    print("recomenda-se revisar o motor ou calibrar os peneus.")
elif 8.0 <= consumo_medio <= 12.0:
    print("classificacao: consumo moderado")
else:
    print("classificacao economico")