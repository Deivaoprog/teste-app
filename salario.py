print("\n*** mostra o desconto do inss!****")
salario = float(input('Entre com o salario:'))
if salario <= 1693.72:
    inss = float(salario *0.08)
elif salario >= 1693.73 and salario  <= 2822.90:
    inss = salario * 0.09
elif salario >= 2822.91 and salario <= 5645.80:
    inss = salario * 0.11
else: 
    inss = 621.04

print("O desconto do inss será de : \n", "%.2f" % inss)

input("Pressione enter para sair")