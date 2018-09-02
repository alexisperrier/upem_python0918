

5 jours

- intro python, historique, versions [slides]
- Envt: Anaconda, session ipython et notebook jupyter, editeur atom
- programmation basic 1: variables, fonctions: type, range, arguments, declarer une fonction. pourquoi une fonction.
- programmation basic 2: loops, comprehensions, structures de donnees (list array, range), print et print format
- programmation basic 3: importing modules, strings operations, time, command line arguments https://www.python-course.eu/python3_passing_arguments.php
- pandas, numpy, I/O json, csv, excel
- git basic
- resources: stackoverflow
- projet: aggreger dataset bbc
- projet: dataset avec api twitter

* TP1 install: install anaconda, faire tourner un notebook jupyter, une session ipython, hello world, executer un script python, environement,

* TP2 variables et fonctions: exercices divers

* TP3 structures de donnees et loops sur texte:
    - prendre une liste de texte et transformer, filtrer.
    - mettre dans un dict tous les mots (liste) avec clefs = lettre de l'alphabet (split, dict, loop, lower()), rajouter la longueur des mots, filtrer sur la longueur (parcourir un dict)
    - mots uniques avec set
    - range
    - enlever les accents, la ponctuation (string.punctuation)
    - sur texte gutemberb ? (https://www.gutenberg.org/wiki/FR_Page_d%27Accueil), download avec wget, version html, enlever les tags ? (BeautifulSoup)


* TP4: file I/O sur fichier assemblé nationale
    - lire fichiers acteurs, nettoyer et aggreger
    - lire questions ecrites en json, gros fichier
    - est republicain cnrtl-fr: xml
    - fichiers: data.europa.zip, JOx_FMX_FR_2014.ZIP, zip dans zip + xml
    - mots les plus courants; stats simple sur acteurs

* TP5: pandas
    - load csv de tweets abeilles par exemple
    - stats,
    - plot: histogram, timeline,
    - conditions
    - value_counts
    -


# TP6: construire un dataset avec l'API twitter
- interroger une api
- Twitter api
-

# --------------------------------------------------------
# slides
# --------------------------------------------------------

# Jour 1:
* presentations
* programme des 2 semaines: programmation python, focus sur dataset texte reel
* pourquoi python, historique, https://en.wikipedia.org/wiki/Python_(programming_language)
* Zen of Python: import this, ce que j'en garde ..
* https://en.wikipedia.org/wiki/Spam_(Monty_Python) ?
* pythonic, Pythonists, Pythonistas, and Pythoneers
* whitespace vs tabs
* packages: As of March 2018, the Python Package Index (PyPI), the official repository for third-party Python software, contains over 130,000[94] packages
* duck typing: https://en.wikipedia.org/wiki/Duck_typing
* no compilation

## The language
* variables:
    * type: string, float, int, boolean, with type(). transformer une var en un autre type, print float with 2 decimals
    * test equality with ==
    * conditions
    * x if c else y
* keywords: and, as, assert, break, class, continue, def, del, elif, else,
except, False, finally, for, from, global, if, import, in, is,
lambda, None, nonlocal, not, or, pass, raise, return, True, try,
while, with, yield
* commentaires: # and triple quotes: quelqu'un d'autre va lire votre code. vous!
* Statements:
    * The if statement, which conditionally executes a block of code, along with else and elif (a contraction of else-if).
    * The for statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block.
    * The while statement, which executes a block of code as long as its condition is true.
    * The try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses; it also ensures that clean-up code in a finally block will always be run regardless of how the block exits.
    * The def statement, which defines a function or method.
    * The raise statement, used to raise a specified exception or re-raise a caught exception.
    * The assert statement, used during debugging to check for conditions that ought to apply.
    * The import statement, which is used to import modules whose functions or variables can be used in the current program. There are three ways of using import: import <module name> [as <alias>] or from <module name> import * or from <module name> import <definition 1> [as <alias 1>], <definition 2> [as <alias 2>], ....
    * The print statement was changed to the print() function in Python 3.[61]

* fonctions (https://www.python-course.eu/python3_functions.php)

# --------------------------------------------------------
# exercices
# --------------------------------------------------------
    * [list comprehension] Celsius to farenheit
    ```
        Celsius = [39.2, 36.5, 37.3, 37.8]
        Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
    ```
    * [list comprehension] A Pythagorean triple:  a2 + b2 = c2.
    ```
    [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
    ```


# --------------------------------------------------------
# resources
# --------------------------------------------------------
Python Loops Tutorial
https://www.datacamp.com/community/tutorials/loops-python-tutorial

# data assemblee nationale
* http://data.assemblee-nationale.fr
* textes, demographies http://www.assemblee-nationale.fr/opendata/Index_pub.html

# course
https://www.python-course.eu/


تشرق الشمس
