#Écrivez une fonction qui prend une liste 
#de nombres entiers en entrée et renvoie True si tous les nombres sont positifs, False sinon.

lst_1 = [1, 2, 3, 4, 5]#True
lst_2 = [1, 2, -3, 4, 5]#False
lst_3 = [-1, -2, -3, -4, -5]#False
lst_4 = []#True
lst_5 = [123, 45]
lst_6 = ["Bonjour Je Suis h4cK3rM4n°4", "qsd"]
lst_7 = ["Bonjour Je Suis h4cK3rM4n°4", "qsd"]
lst_8 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
		31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
		79, 83, 89, 97, 101, 103, 107, 109, 113,
		127, 131, 137, 139, 149, 151, 157, 163,
		167, 173, 179, 181, 191, 193, 197, 199,
		211, 223, 227, 229]
lst_9 = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

def function_1(liste):
	new_lst = []
	for i in liste:
		if i < 0:
			return False
	return True
	if liste == []:
		return True


#Écrivez une fonction qui prend une liste de
#nombres réels en entrée et renvoie True si la somme des nombres est supérieure à 50, False sinon.

def function_2(liste):
	v = sum(liste)
	if v > 50:
		return True
	else:
		return False

#Écrivez une fonction qui prend deux listes de mots en 
#entrée et renvoie True si tous les mots de la première liste se trouvent dans la seconde liste, False sinon.

def function_3(liste_1, liste_2):
	if liste_1 == liste_2:
		return True
	else:
		return False

#Écrivez une fonction qui prend une liste de nombres entiers en entrée et renvoie True si tous les nombres sont premiers, False sinon.