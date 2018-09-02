# read folder content
import glob
iumport os

FOLDER_PATH  = '/Users/alexis/amcp/inra_bees/data/'

files = glob.glob(FOLDER_PATH + '*.txt')
target = 'network/urls_expanded.csv'

df = pd.DataFrame(columns = ['expanded', 'original', 'status'])

for file in files:
