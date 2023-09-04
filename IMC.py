#############################################################################
#############################################################################
#########################################################################Ŀ##
###Programa  #IMC# Autor # Vinicius Neisser         # Data #17/08/2023###
#########################################################################Ĵ##
###Descrição #CALCULO DE IMC                                              ###
###          #                                                            ###
#########################################################################Ĵ##
###Retorno   #Indice de Massa Corporal, numero decinal                   ###
#########################################################################Ĵ##
###Parametros#                                                            ###
###          #       Altura(mts)²                                         ###
###          #       Peso(Kg)                                             ###
#########################################################################Ĵ##
###                                                                       ###
#########################################################################Ĵ##
###          #               #                                            ###
##########################################################################ٱ#
#############################################################################
#############################################################################

print("############# CALCULO DE IMC #############")

altura = float(input("Digite sua altura(Exemplo: 1.8 .... 1.65)"))   #REQUISITANDO O USUARIO A DIGITAR SUA ALTURA

peso = float(input("Digite seu peso(Exemplo: 70 .... 56.7)"))       # REQUISITANDO O USUARIO A DIGITAR SEU PESO

imc = peso / (altura* altura) # FORMULA DO IMC

imc = round(imc, 2)  # SETANDO DUAS CASAS DEPOIS DA VIRGULA DO NUMERO DECIMAL

if(imc<= 18.5):  #RESULTADOS

    print('Seu IMC está abaixo do peso normal ')

elif(imc>18.5 and imc<=24.9):
 
    print('Seu peso está normal')

elif(imc>25 and imc<=29.9):
 
    print('Você está com excesso de peso')

elif(imc>30 and imc<=34.9):

    print('Você está com Obesidade I ',imc)

elif(imc>35 and imc<=39.9):

    print("Você está com Obesidade II ",imc)

else:

    print('Você está com Obesidade III ',imc)

print("Seu IMC é:",imc)

