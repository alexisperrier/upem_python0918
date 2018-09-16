'''
Ce script explore le dataset les-arbres.csv
https://opendata.paris.fr/explore/dataset/les-arbres/
'''
# required libraries
import pandas as pd
import urllib2
import matplotlib.pyplot as plt

# function declarations

def download_dataset(download_url):
    response = urllib2.urlopen(download_url)
    if response.code == 200:
        content = response.read()
    else:
        print("[{}] could not download url {}".format(code, download_url))
    return content


# global variables and constants

DATA_PATH = '/Users/alexis/amcp/upem/python0918/data/'
URL = 'https://opendata.paris.fr/explore/dataset/les-arbres/download/?format=csv&timezone=America/New_York&use_labels_for_header=true'

if __name__== '__main__':
    # main code

    # check if file exists
    if ~os.path.isfile(DATA_PATH + 'les-arbres.csv'):
        download_dataset(URL)
        # some code to unzip the file if needed


    # read data into a dataframe
    df = pd.read_csv(DATA_PATH + 'les-arbres.csv', error_bad_lines = False, delimiter = ';')
    print("le dataset a {} rows ".format(df.shape[0]))
    print(df.head())
    print()
    print(df.describe())

    # histogram des hauteurs de arbres
    fig, ax = plt.subplots(1,1)
    df['HAUTEUR (m)'].hist(bins = 100)
    plt.show()

    # histogram des circonferences de arbres
    df['CIRCONFERENCEENCM'].hist(bins = 100)

    print("enlever les arbres trop haut > 100m  ou trop large > 10m")
    df = df[df['HAUTEUR (m)'] < 100]
    df = df[df['CIRCONFERENCEENCM'] < 1000]

df.describe()
df['HAUTEUR (m)'].hist(bins = 100)
plt.show()
df[df['HAUTEUR (m)'] > 100].shape
df[df['HAUTEUR (m)'] > 50].shape
df[df['HAUTEUR (m)'] > 50].head()
plt.show()
df['HAUTEUR (m)'].hist(bins = 100)
df['CIRCONFERENCEENCM'].hist(bins = 100)
plt.plot(df['CIRCONFERENCEENCM'], df['HAUTEUR (m)'])
plt.show()
plt.plot(df['CIRCONFERENCEENCM'], df['HAUTEUR (m)'], '.')
plt.plot(df['CIRCONFERENCEENCM'], df['HAUTEUR (m)'], '.', alpha = 0.4)
df.head()
df['ESPECE'].value_counts()
plt.show()
cond = df['ESPECE' == 'hippocastanum']
cond = df['ESPECE'] == 'hippocastanum'
plt.plot(df[cond]['CIRCONFERENCEENCM'], df[cond]['HAUTEUR (m)'], '.', alpha = 0.4)
cond = df['ESPECE'] == 'japonica'
plt.plot(df[cond]['CIRCONFERENCEENCM'], df[cond]['HAUTEUR (m)'], '.', alpha = 0.4)
plt.show()
df['ARRONDISSEMENT'].value_counts()
plt.bar(df['LIBELLEFRANCAIS'].value_counts().keys(), df['LIBELLEFRANCAIS'].value_counts().values)


df['DOMANIALITE'].value_counts()
type d'arbre par DOMANIALITE

df['REMARQUABLE'].value_counts(dropna = False)
