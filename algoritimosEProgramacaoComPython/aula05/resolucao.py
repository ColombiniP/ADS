#Para a zona norte da cidade, o percentual máximo é de 25%.
#Para as zonas leste e oeste da cidade, o percentual máximo é de 30%.
#Para a zona sul, menos povoada, o percentual máximo é de 40%.

# Variáveis
zona_norte = 25
zona_leste = 30
zona_sul = 40

# funções
def areaTerreno(largura, profundidade):
    return largura * profundidade

def areaGaragem(largura, profundidade):
    return largura * profundidade
    
def percentOcupacao(areaGaragem, areaTerreno):
    return (areaGaragem / areaTerreno) * 100

largura_garagem_metros = float(input("Qual a largura da garagem em metros: "))
profundidade_gararem_metros = float(input("Qual a profundidade da garagem em metros: "))
areaG = areaGaragem(largura_garagem_metros, profundidade_gararem_metros)

largura_terreno_metros = float(input("Qual a largura do terreno em metros: "))
profundidade_terreno_metros = float(input("Qual a profundidade do terreno em metros: "))
areaT = areaTerreno(largura_terreno_metros, profundidade_terreno_metros)

percentual_plano = percentOcupacao(areaG, areaT)
zona_terreno = input("qual a zona de habitação - (norte=n, sul=s ou leste=l): ")

print(" ")
print("Área da garagem %2.fM" % areaG)
print("Área do terreno %2.fM" % areaT)
print('percentual destinado a garagem %2.f por cento' % percentual_plano)
print(" ")

# Condição
if zona_terreno == "n" and percentual_plano <= 25:
    print ("Dentro do padrão")
elif zona_terreno == "l" and percentual_plano <= 30:
    print ("Dentro do padrão")
elif zona_terreno == "s" and percentual_plano <= 40:
    print ("Dentro do padrão")
else:
    print("Fora do padrão")