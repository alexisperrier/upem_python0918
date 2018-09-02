# exemple de fonctions

def clean_text(text):
    '''
    Cette fonction remplace certains caractères dans un texte.
    La liste des caractères est: ['\xa0', '…', '«', '»', '’']
    Input: text: string qui peut contenir les
    Output: text: string
    '''
    text = text.replace('\xa0','')
    text = text.replace('…','')
    text = text.replace('«',' ')
    text = text.replace('»',' ')
    text = text.replace('’',"'")
    return text

def remove_punctuation(text):
    '''
    Cette fonction prend un text en input et en enleve tous les signes
    de ponctuations definis dans le module string.ponctuation
    '''
    import string
    for s in string.punctuation:
        text = text.replace(s,' ')
    return text


def sort_trim(lst):
    '''
    Cette fonction traite une liste
    - enleve les elements = ''
    - prends les elements uniques
    - sort les elements
    - retourne une liste

    '''
    return [l for l in list(sorted(set(lst))) if l != '']


agrumes = ['orange', 'citron']
def detect(fruits):
    '''
    Cette fonction enleve certains fruits d'une liste de mots
    '''
    for agr in agrumes:
        if agr in fruits:
            print("- {} detecté".format(agr))
            fruits.remove(agr)
    return fruits

fruits =  ['banane', 'pomme', 'poire', 'citron', 'fraise']
detect(fruits)

# compter la longueur des mots
[len(mot) for mot in liste_de_mots]

# mettre en minuscule tous les mots d'une phrase

phrase = "Une phrase avec DES Majuscules à la MauVAISE plaCe."
tokens = [ mot.lower() for mot in phrase.split(' ')  ]
phrase = ' '.join(tokens)
