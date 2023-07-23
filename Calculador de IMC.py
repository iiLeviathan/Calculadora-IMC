# Projeto Calculador de IMC
# Feito em Python
# Pretendo continuar no futuro e adicionar uma interface
# Feito apenas por mim, sem ajuda (graças a Deus).

def calculador_de_imc(altura, peso, sexo):
    if sexo == 1:
        imc_homem = peso / (altura ** 2)
        print(f"Seu IMC é: {imc_homem}")
        definidor_de_imc_homem(imc_homem)
    elif sexo == 2:
        imc_mulher = peso / (altura ** 2)
        print(f"Seu IMC é: {imc_mulher}")
        definidor_de_imc_mulher(imc_mulher)

def definidor_de_imc_homem(imc_homem):
    if imc_homem <= 18.5:
        print("Você está abaixo do peso.")
    elif 18.6 <= imc_homem <= 24.9:
        print("Você está no peso ideal, parabéns!")
    elif 25.0 <= imc_homem <= 29.9:
        print("Você está levemente acima do peso.")
    elif 30 <= imc_homem <= 39.9:
        print("Você está em uma fase de obesidade moderada.")
    else:
        print("Você está em uma fase de obesidade mórbida. Procure ajuda médica.")

def definidor_de_imc_mulher(imc_mulher):
    if imc_mulher <= 19:
        print("Você está abaixo do peso.")
    elif 19.1 <= imc_mulher <= 23.9:
        print("Você está no peso ideal, parabéns!")
    elif 24.0 <= imc_mulher <= 28.9:
        print("Você está levemente acima do peso.")
    elif 29 <= imc_mulher <= 38.9:
        print("Você está em uma fase de obesidade moderada.")
    else:
        print("Você está em uma fase de obesidade mórbida. Procure ajuda médica.")

def informacao():
    altura = float(input("Digite a sua altura (em metros): "))
    peso = float(input("Digite seu peso (em kg): "))
    sexo = int(input("Digite 1 se for homem ou 2 para mulher: "))

    calculador_de_imc(altura, peso, sexo)

informacao()