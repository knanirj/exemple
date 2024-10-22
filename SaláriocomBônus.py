# coding: utf-8
# Exercício: Salário com Bônus
def salbon(salario,totalvendas):
    comissão= totalvendas * 0.15
    totalareceber=salario+comissão
    return(comissão,totalareceber)
for i in range (3):
    nomedevendeur=str(input("entrer le nom de vendeur:"))
    salario=float(input("entrer le salaire fixe:"))
    totalvendas=float(input("entrer le total de vente en real:"))
    comissão,totalareceber=salbon(salario,totalvendas)
    print(f"a comissão e{comissão},e o totalareceber e {totalareceber}, para vendedor : {nomedevendeur}")
