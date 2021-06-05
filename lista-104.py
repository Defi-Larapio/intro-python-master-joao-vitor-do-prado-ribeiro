
lista1 = [1,2,3]
lista2 = [1,2,3]
lista3 = [3,2,1]
string1 = 'ovo'
string2 = 'ovo'
string3 = 'egg'
string4 = 'luz azul'
string5 = 'luz azul'

###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
# 
def function1(lista1,lista2):
	if lista1[::] == lista2[::]:
		return print(True)
	else:
		return print(False)
        
function1(lista1,lista2)
function1(lista1,lista3)
	

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
def function2(string1,string2):
	string1 = string1.lower()
	string1 = string1.replace(" ", "")
	string2 = string2.lower()
	string2 = string2.replace(" ", "")
	if string1 == string2 and string1[::-1] == string2[::-1]:
		return print(True)
	else:
		return print(False)

function2(string1,string2)
function2(string1,string3)
function2(string4,string5)
	
# OBS.: Utilize apenas o que foi estudado ate agora
