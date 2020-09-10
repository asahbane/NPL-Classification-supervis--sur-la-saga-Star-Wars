import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import os 
import matplotlib.pyplot as plt
from matplotlib.pyplot import hist



## fonction pour enlever les répititions 
def unique(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res



## cette fonction va prendre une chaine de caractères
## et va sortir une liste des vocabulaire important dans cette chaie de caractères
def filtre(str):
    if type(str) == float:
        return [' ']
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    ## on va mettre tout en miniscule
    str = str.lower()
    ## on va créer un 'pattern' 
    ## \w désigne un alphanumerique
    ## c à d qu'on cheche tout morceaux composé d'alphanumériques
    tokenizer = RegexpTokenizer(r'\w+')
    ## on va sépparer la chaine de caractère 
    words = tokenizer.tokenize(str)
    ## on va enlever les "stopwords"
    filtered_sentence = [w for w in words if not w in stop_words]
    ## par une boucle on va trouver les mots apparteneant au même champ lexicale
    for i in range (len(filtered_sentence)):
        filtered_sentence[i] = lemmatizer.lemmatize(filtered_sentence[i])
    ## on va enlever les répitition 
    filtered_sentence = unique(filtered_sentence)
    return filtered_sentence



def magic2(df):
    temp = []
    for i in range(len(df)):
        temp.append(' '.join(filtre(df['parole'][i])))
    df['paroles_traités']= temp
    return df



from collections import Counter
def count(liste, col1_name, col2_name):
    """prend une liste et renvoie une 'pandas dataframe', 
    avec chaque element de la liste et son nombre d'occurence dans la liste"""
    
    x = pd.DataFrame.from_dict(Counter(liste), orient='index').reset_index()
    ## renommer les colonnes
    x = x.rename(columns={'index':col1_name, 0:col2_name})
    ## trier par nombre d'occurence
    x = x.sort_values(by=[col2_name], ascending=False)
    return x



from wordcloud import WordCloud
def wordcloud(liste):
    """prend une liste de chaines de cractères, et renvoie le 'wordcloud' de tous les mots de cette liste """
    ## constriure la liste des mots
    words = []
    for i in liste:
        words.append(i)
    words = ' '.join(words)

    ## constriure le 'wordcloud'
    wordcloud = WordCloud(width = 800, height = 800, min_font_size = 10).generate(words) 

    ## afficher le wordcloud    
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.show() 
    

    
def histo(D):
    fig = plt.figure(figsize=(15,9))
    ax = fig.add_subplot(111)
    hist(D.iloc[:, 0], weights=D.iloc[:, 1],density=False, bins = 264)
    y_pos = range(len(D.iloc[:, 0]))
    plt.xticks(y_pos, D.iloc[:, 0], rotation=90)
    plt.tight_layout()
    ax.set_xlabel('Prénom')
    ax.set_ylabel('Nombre de paroles')
    
    
    
    
def getpath(i):
    os.path.join(os.getcwd(), '..')
    tmp = os.path.abspath(os.path.join(os.getcwd(), '..'))
    path = os.path.join(tmp, 'Data', 'Data_Clean', 'SW'+str(i)+'_clean.csv')
    return path
    

    
    
def design_matrix(df):
    d = df.copy()
    
    ## certaint prénoms contient des espaces au début ou à la fin 
    ## on va les enlever (par exemple :'THERIPIO ' --> 'THERIPIO')
    for i in range(len(d)):
        d['Name'][i] = d['Name'][i].strip()
    
    ## netoyage des paroles (enlever les stopwords)
    D = magic2(d)
    
    ## on va enlever les lignes où y'a pas de paroles
    lis = []
    for i in range(len(D)):
        if D['paroles_traités'][i] in ['', ' ']:
            lis.append(i)
    D = D.drop(lis)
    D.reset_index(drop=True, inplace=True)
    
    ## on va rajouter une colonne de nombre de paroles
    x = Counter(D['Name'])
    D['nb_paroles'] = D['Name'].map(x)
    
    ## on va fusionner les paroles pour chaque personnage
    D = D.groupby(['Name', 'nb_paroles'])['paroles_traités'].apply(' '.join).reset_index()

    ## on va rajouter une colonne de pourcentage de nombre de paroles
    D['perc_parole']= D['nb_paroles']/D['nb_paroles'].sum()

    ## on va rajouter une colonne de nombre de mots 
    nb_mots = []
    for i in D['paroles_traités']:
        nb_mots.append(len(i.split()))

    D['nb_mots'] = nb_mots

    ## on va rajouter une colonne de pourcentage de nombre de mots
    D['perc_mots']= D['nb_mots']/D['nb_mots'].sum()
    
    ## gérer l'ordere des colonnes
    D = D[['Name','paroles_traités', 'nb_paroles',  'perc_parole', 'nb_mots', 'perc_mots']]
    
    return D