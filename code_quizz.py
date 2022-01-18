# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:43:07 2022

@author: Jean
"""
import pandas as pd
import random
import numpy as np
import time

#%% 
#Créé une liste de chiffre entier aléatoire entre deux bornes
def questions_alea(nbre_questions, taille):
    liste = []
    list_bis = []
    [liste.append(i) for i in range(1,taille + 1)]
    for i in range(0, nbre_questions):
        alea = random.choice(liste)
        list_bis.append(alea)
        liste.remove(alea)
    return list_bis

# %%

#Init. BDD des questions
questions = pd.read_csv(r"C:\Users\Jean\Documents\Projets python\
                        Jedha QUIZZ\QCM.csv") 
#Choix du nombre de questions à poser + tirage des questions via questions_alea
nbre_questions = 4
list_question = questions_alea(nbre_questions, len(questions))
#Init. des variables et du temps
compteur_bonne = 0
compteur_fausse = 0   
t0 = time.time()
print("--------------------------------------------")
print("BIENVENUE DANS CE QUIZ SUR LES DATA SCIENCES")
print("--------------------------------------------\n")
#L'utilisateur entre son pseudonyme
pseudo = input("Quel est votre pseudo ? ")
print("")
#Boucle pour afficher les questions/réponses après input utilisateur
for i in range(0, len(list_question)):
    if len(list_question)-1 == 1: #ajoute ou enlève un S à question
        stri = "question"
    else:
        stri = "questions"
    print(questions.iloc[list_question[0]-1]['Question'])
    print("A :", questions.iloc[list_question[0]-1]['Answer A'])
    print("B :",questions.iloc[list_question[0]-1]['Answer B'])
    print("C :", questions.iloc[list_question[0]-1]['Answer C'])
    if not pd.isna(questions.iloc[list_question[0]-1]['Answer D']) :
        print("D :",questions.iloc[list_question[0]-1]['Answer D'])
    reponse = input("Quelle est votre réponse ?... ")
    #Si la réponse n'est pas a, b,c ou d, redemande un input
    while reponse.lower() not in ["a", "b", "c", "d"]:
        print("Vous devez répondre par : A, B, C ou D, ré-essayez ! :)")
        reponse = input("Quelle est votre réponse ?... ")
    #Incrémente le compteur si bonne réponse ou mauvaise réponse
    if reponse.lower() != questions.iloc[list_question[0]-1]['Answer'].lower():
        print("Mauvaise réponse... :(, encore", 
              len(list_question)-1, stri,"!\n")
        compteur_fausse += 1
    else :
        print("Bien joué, bonne réponse, encore", 
              len(list_question)-1, stri,"!\n")
        compteur_bonne += 1
    del list_question[0]
    
# %%

#Calcule le temps nécessaire à la complétion du questionnaire
t1 = time.time()
temps_total = t1-t0
pourcentage_bonne_rep = (compteur_bonne/(compteur_bonne+compteur_fausse))*100
#Calcul du temps total/question
pourcentage_temps = round(temps_total,2)/nbre_questions

print("Vous avez eu", pourcentage_bonne_rep, "% de bonnes réponses en" , 
      round(temps_total,2),"secondes, soit,", 
      round(pourcentage_temps,2),"secondes /question.")
#Créé une ligne à append au dataframe "rank.csv"
rank = pd.DataFrame({'Pseudo': [pseudo],
                    'pct_rep': [pourcentage_bonne_rep],
                    'pct_temps': [pourcentage_temps]})
#Append
rank.to_csv('rank.csv', mode='a', index=False, header=False)
#Lecture du fichier contenant le classement des utilisateurs
classement = pd.read_csv("rank.csv")
#Tri du fichier classement, par bonne réponse et par temps
classement_sorted = classement.sort_values(["pct_rep", "pct_temps"], 
                                           ascending = (False, True))
#Récupération des positions des pseudos et conversion array -> list
arr_classement = pd.unique(classement_sorted['Pseudo'])
list_classement = arr_classement.tolist()
#Rang final correspondant à la position dans la liste
rang_final = list_classement.index(pseudo) + 1

print('Vous êtes classé n°',rang_final)
        


    