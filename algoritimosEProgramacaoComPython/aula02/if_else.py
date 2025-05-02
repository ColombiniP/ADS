print(" ---------- ELEGÍVEL AO VOTO ------------------\n")
print("Regras para votar: ")
print("- Idade até 15 anos, não pode votar")
print("- Idade a partir de 16 até 17 anos, voto facultativo")
print("- Idade a partir de 18 até 64 anos, voto obrigatório")
print("- Idade a partir de 65 anos, voto facultativo\n")
print("-----------DADOS PESSOAIS---------------------\n")

nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))

if idade <= 15: 
    print(f"Olá {nome}, você ainda não pode votar!")

elif idade >= 16 and idade <= 18 or idade >= 65:
    print(f"Olá {nome}, seu voto é facultativo")

else:
    print(f"Olá {nome}, seu voto é obrigatório!")