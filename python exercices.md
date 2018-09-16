
# Exercices

## Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Palyndrome

print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# inverser les mots d'une phrase
Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My

# enlever les mots en doublons

Write a Python program to remove duplicates from a list.


# trois lettres
soit une phrase
ecrire un script qui parcours la phrase et qui met dans une liste
toutes les sequences de 3 lettres
sans les espaces

a partir d'un texte
par exemple

Construire la liste des mots (utiliser split)

Enlever la ponctuation (utiliser string.punctuation)
et mettre en minuscule

construire la liste des mots uniques
utiliser list(set())
ex: list(set([1,2,1,2,1])) -> [1,2]

Calculer pour chaque mot unique le nombre d'apparition dans la liste de l'etape 2

Quelle est la moyenne d'apparition, le median, le 90 percentile
utiliser la librairie numpy et les fonctions suivantes

import numpy as np
a = [1,2,3,4,5]
np.mean(a)
np.median(a)
np.percentile(a, 90)

Construire une liste plus restreinte de mots en ne gardant que les mots qui apparaissent plus que le median.
