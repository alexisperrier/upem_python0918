# librairie a importer
import glob

# path vers le repertoire ciblé
FOLDER_PATH  = '/Users/alexis/amcp/upem/python0918/data/'

# la liste des fichiers avec extension txt
files = glob.glob(FOLDER_PATH + '*.txt')

# liste sur laquelle on peut iterer
for file in files:
    <lire le fichier>


import os
for file in os.listdir(FOLDER_PATH):
    if os.path.isfile(FOLDER_PATH + file):
        print(file)
