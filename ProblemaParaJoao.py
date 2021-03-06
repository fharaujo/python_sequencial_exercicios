"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na
variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com
o conteúdo ZERO."""

#autor: @fharaujo
#data: 28/10/2016
#Projeto: APrendendo Python - Estrutura Sequencial

print("""Você tem um limite Estadual de 50kg de pescado.
Após isso, será cobrado um valor de R$ 4.00 por kg excedente\n""")
kg_permitido = 50
peso = float(input("Digite o peso do pescado: "))

if peso > kg_permitido:
    excesso = peso - kg_permitido
    multa = excesso * 4.00
    print("O excesso de %i kg, gerou uma multa de: R$ %.2f" % (excesso, multa))
elif peso <= kg_permitido:
    multa = 0
    excesso = 0
    print("O excesso de %i kg, gerou uma multa de: R$ %i" % (excesso, multa))
else:
    print("Digite um valor válido!")