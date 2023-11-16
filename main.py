from namePresidents import *
from cleanText import *

def cleanTextes():
    files_name = list_of_files('speeches', 'txt')
    for file in list_of_files:
        lowercasedtext = toLowerCases(file)
    