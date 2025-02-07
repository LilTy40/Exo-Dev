# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:26:19 2025

@author: bruyere
"""

import pandas as pd
import numpy as np
import os
# choix du répertoire par défaut (à modifier)
os.chdir('F:\Repo TPs info\\TPs-Dev\\1ere annee\\R2_08_Statistiques\\Pandas')

###########################################
# importation du fichier ProfEntrants.csv #
###########################################


#profilsentrants=pd.read_table('ProfEntrants.csv',sep=";")


'''Vérifier que l’importation s’est correctement déroulée : 
il ne doit pas y avoir de message d’erreur et le DataFrame profilsentrants 
doit se trouver dans les variables de votre environnement (fenêtre variable explorer, normalement en haut à droite)
Il est possible de visualiser le contenu du DataFrame en cliquant sur son nom 
dans la fenêtre variable explorer (c’est l’un es intérêts de l’environnement Spyder)'''

#################
# Application 1 #
#################
# Importer le fichier « Poursuites.csv » en utilisant comme index la colonne « code ».
#•	Si vous n’avez pas changé les options dans le read_table, il y a un problème dans l’importation. Corrigez-le.
#•	Un « index » a été créé, il s’agit d’une colonne qui permet d’identifier les lignes. Tout DataFrame Pandas doit avoir un index.  En statistique, on parle de variable identificatrice (en BD, il s’agirait d’une clé primaire). Par défaut, si rien n’a été précisé au moment de l’importation, l’index correspond à une numérotation des lignes, mais il aurait été possible, au moment de la lecture du fichier texte (importation), de préciser quelle est la colonne, dans le fichier lu, qui contient les identifiant des lignes, quelle est la « variable identificatrice ».  
# Exercice : modifier les options de read_table (ou read_csv) pour que la variable Code soit considérée comme index (variable identificatrice)

poursuites=pd.read_table('Poursuites.csv',sep=";",encoding='windows-1252')

# Importer le fichier « Resultats.csv » en utilisant comme index la colonne « num ».
# Si vous n’avez pas changé les options dans le read_table, vous devez observer nouveau problème
# dans le DataFrame. Corrigez-le.

num=pd.read_table('Resultats.csv',sep=";",encoding='windows-1252')

# Importer directement les trois feuilles du fichier excel « Données Etudiants anonymisées - avec poursuites détudes.xlsx » en utilisant la fonction pd.read_excel. 
# Nom des feuilles : Profil entrant, Résultat, Poursuites d'études

#excel=pd.read_excel('Données Etudiants anonymisées - avec poursuites détudes.xlsx')


# QCM d'entrainement : https://elearn.univ-pau.fr/mod/quiz/view.php?id=604584

###############################
# Manipulation d'un dataframe #
###############################

# Dimensions du dataframe
'''profilsentrants.shape
profilsentrants.shape[0]
profilsentrants.shape[1]'''

##############################
# Les individus              #
# Index - changement d'index #
##############################

# importation du fichier ProfEntrants.csv
profilsentrants=pd.read_table('ProfEntrants.csv',sep=";")

# Num en index :
profilsentrants = profilsentrants.set_index("Num")
# Suppression de l’index :
profilsentrants = profilsentrants.reset_index()

'''for ind in profilsentrants.index :
    print(ind)'''

#################
# Les variables #
#################
num.astype({'UE11': 'float64'}).dtypes

profilsentrants.columns
profilsentrants.dtypes
var = profilsentrants['Bac']

###################################
# Accès aux éléments du dataframe #
# Méthodes loc et iloc            #
###################################

# Sélection d'un individu avec loc et iloc
profilsentrants.iloc[0,1]
profilsentrants.loc[140,'Bac']  
num.loc['16-17','AnnS2']
num
# Sélection d'un individu avec at et iat
profilsentrants.iat[0,0]                   	   
profilsentrants.at[140,'Bac']

# Sélection de plusieurs lignes et/ou plusieurs colonnes
profilsentrants.iloc[[1,2,3,4],[0,3]]
profilsentrants.iloc[1:5,[0,3]]
profilsentrants.loc[[18,196,83,30],['Bac','Serie']]

# Sélections d'individus
profilsentrants.iloc[1:5,:] 
profilsentrants.loc[[18,196,83,30],:]
profilsentrants.loc[profilsentrants['Serie'] == 'S',:]

#################
# Application 2 #
#################
#a.	Importer le DataFrame resultats à partir de resultat.csv ou de Données Etudiants anonymisées - avec poursuites détudes.xls 




#b.	Créer un DataFrame res1819 ne contenant que les résultats des étudiants de la promo 18-19




#c.	Créer un objet de type Series, ne contenant que les Décisions de passage de S2 pour les étudiants dont la moyenne au S2 est inférieure à 10.





# QCM d'entrainement : https://elearn.univ-pau.fr/mod/quiz/view.php?id=604604

###############################################
###############################################
## MANIPULATION DES VARIABLES D’UN DATAFRAME ##
###############################################
###############################################

############################################
# Afficher, modifier les noms de variables #
############################################
poursuites = pd.read_table('poursuites.csv', sep = ";", 
                            encoding = 'windows-1252', index_col = 0)

# Affichage des noms de variables
poursuites.columns
poursuites.columns[2]

# Renommer une variable
l=list(poursuites.columns)
l[2]='Formation'
poursuites.columns=l             

#######################
# Types des variables #
#######################
poursuites.dtypes
poursuites = poursuites.astype({'Situation' : 'category', 'Alternance' : bool})
poursuites.dtypes

###############################################
# Une idée rapide du contenu d’une variable ? #
###############################################

resultats=pd.read_table('resultats.csv',sep=';', encoding = 'windows-1252',index_col=0,decimal=',')
# Variable qualitative : modalités de la variable "Situation"
poursuites['Situation'].unique()
# Variable quantitative : indicateurs
resultats['MoyS2'].describe()

#######################################################
# Les variables qualitatives et le format categorical #
#######################################################

poursuites = pd.read_table('poursuites.csv', sep = ";", 
                            encoding = 'windows-1252', index_col = 0)
poursuites.dtypes
poursuites['Situation']=poursuites['Situation'].astype('category')
poursuites.dtypes
 
# Format categorical et variables qualitatives ORDINALES 
profilsentrants=pd.read_table('ProfEntrants.csv',sep=";")
profilsentrants['Mention'].unique()

profilsentrants['Mention']=pd.Categorical(profilsentrants['Mention'],
                                          categories=['Admis sans mention', 
                                                      'Admis mention Assez Bien',
                                                      'Admis mention Bien', 
                                                      'Admis mention Très Bien'], 
                                          ordered = True)
profilsentrants['Mention'].unique()


########################################################
# Des variables qualitatives particulières : les dates #
########################################################

df = pd.read_csv('testdate.csv', sep=";")
df.dtypes

df['date'] = pd.to_datetime(df['date'], format = "%m-%Y")
df.dtypes

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


########################################            
# Création et suppression de variables #
########################################

# Création
poursuites['nvlvar1']=0
poursuites['nvlvar2']=numpy.nan

# Suppression : méthode drop
# Suppression de variables (colonnes)
poursuites.drop(columns=['Situation','complement'],inplace = True)
# Suppression d’individus (lignes)
poursuites.drop(index=[106,149], inplace = True)

# Manipulations de variables quantitatives : transformation, mise en classes
# Transformation d’une variable quantitative par une fonction – APPLY

resultats = pd.read_table('Resultats.csv',sep=";", 
                          encoding = "windows-1252", 
                          index_col = 0, decimal = ",")
resultats.dtypes  
# Les trois instructions suivantes sont équivalentes : 
# racinecarreeA : on utilise apply avec la fonction racine carrée existante np.sqrt
resultats['racinecarreeA'] = resultats['MoyS2'].apply(np.sqrt)
# racinecarreeB : on utilise apply avec une fonction définie localement par lambda 
# « lambda x : np.sart(x) » : la fonction qui à tout x associe sa racine
resultats['racinecarreeB'] = resultats['MoyS2'].apply(lambda x : np.sqrt(x))
# il y avait moyen, ici, de ne pas utiliser apply en appliquant la fonction 
# directement sur la série resultats['MoyS2']
resultats['racinecarreeC'] = np.sqrt(resultats['MoyS2'])
resultats['racinecarreeD']=resultats['MoyS2'].apply(lambda x:np.sqrt(x) if x>=0 else np.sqrt(x))
resultats[['var1','var2']] = resultats.apply({'MoyS2':lambda x: x+1,'Moy':lambda x: x-1})
# racinecarreeA : on utilise apply avec la fonction racine carrée existante np.sqrt

#Exemples avec des fonction à plusieurs variables 
# somA :  on utilise apply avec la fonction existante sum
# axis = 1 : précise que l’on somme les colonnes (axis = 0 : les lignes)
resultats['somA'] = resultats[['Moy','MoyS2']].apply(sum, axis = 1)
# moyB :  on utilise apply avec une fonction localement définie par lambda
resultats['somB'] = resultats.apply(lambda x: x['Moy'] + x['MoyS2'], axis = 1)

# Et sans utiliser apply
resultats['MoyenneA'] = (resultats['Moy'] + resultats['MoyS2'])

##############################################
# Mise en classe d’une variable quantitative #
##############################################

# qcut pour des classes d’effectifs équilibrées
resultats["ClassMoy1"] = pd.qcut(resultats["MoyS2"],4)
resultats["ClassMoy2"] = pd.qcut(resultats["MoyS2"],4,labels = ["g1","g2","g3","g4"])  

# cut pour des classes personnalisées ou d’amplitudes égales
resultats["ClassMoy3"]=pd.cut(resultats["MoyS2"],3)
resultats["ClassMoy4"]=pd.cut(resultats["MoyS2"],3,right=False)

# Pour des classes personnalisées, il suffit de donner les bornes des classes (option bins)
resultats["ClassMoy5"]=pd.cut(resultats["MoyS2"],bins=[0,8,10,12,14,20])

##########################################
# Manipulation de variables qualitatives #
##########################################

# Recodage d’une variable 
# Importation
poursuites = pd.read_table('poursuites.csv', sep = ";", encoding = 'windows-1252', index_col = 0)
poursuites['Situation'] = pd.Categorical(poursuites['Situation'])

# Affichage des modalités
poursuites["Situation"].unique()
 

# Création du dictionnaire des correspondances
# dict_corresp : dict des correspondances entre les anciennes et nouvelles modalités
dict_corresp = {'Année sabbatique': 'Autre',
                'réorientation': 'Autre',
                'Etudes longues': 'Etudes longues',
                'Emploi / Recherche d\'emploi': 'Emploi / Recherche d\'emploi',
                'Licence Pro': 'Licence Pro'}

# Attribution des nouvelles modalités (dans la variable sit2)
poursuites['Situation2'] = poursuites['Situation'].replace(dict_corresp)
poursuites['Situation2'].unique()
 
poursuites.dtypes

###########################
# Concaténation de tables #
###########################

# Jointure (« concaténation horizontale »)
pd.merge(profilsentrants,
         resultats,
         left_index=True,
         right_index=True,
         how="inner")

#################
# Application 3 #
#################

# Manipulations du DataFrame profilsentrants.
# a.	Afficher les noms de variables de ce 



# b.	Renommer la variable « Serie » en « seriebac »



# c.	Afficher les modalités de la variable « seriebac ».



# d.	Créer une nouvelle variable nommée « bac », n’ayant plus de 3 modalités : « S », « STI2D », « Autre »



# e.	Créer une variable nommée « classcod1 » correspondant à la mise en classe de la variable de « Classement » en 5 classes de mêmes effectifs




# f.	Créer une variable nommée « classcod2 » correspondant à la mise en classe de la variable de « Classement » en 5 classes de même amplitude

# Manipulations du DataFrame resultats.
#a.	Afficher les noms de variables de ce DataFrame



#b.	Créer une variable Moyenne, correpondant à la moyenne des deux semestres.



#c.	Créer une variable progres prenant la valeur « oui » si la moyenne de S2 est strictement supérieure à celle de S1 et « non » sinon.

# Jointure. 
# Concaténer les trois tables profilsentrants, poursuites et resultats. 
# On ne gardera que les étudiants communs aux trois tables.
