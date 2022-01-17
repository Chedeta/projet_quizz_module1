# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:43:07 2022

@author: Jean
"""
import pandas as pd
import random
import numpy as np
import time

questions = pd.read_csv(r"C:\Users\Jean\Documents\Projets python\Jedha QUIZZ\QCM.csv")

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
nbre_questions = 4
list_question = questions_alea(nbre_questions, len(questions))
compteur_bonne = 0
compteur_fausse = 0   
t0 = time.time()
print("--------------------------------------------")
print("BIENVENUE DANS CE QUIZ SUR LES DATA SCIENCES")
print("--------------------------------------------\n")
pseudo = input("Quel est votre pseudo ? ")
print("")
for i in range(0, len(list_question)):
    if len(list_question)-1 == 1:
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
    while reponse.lower() not in ["a", "b", "c", "d"]:
        print("Vous devez répondre par : A, B, C ou D, ré-essayez ! :)")
        reponse = input("Quelle est votre réponse ?... ")
    if reponse.lower() != questions.iloc[list_question[0]-1]['Answer'].lower():
        print("Mauvaise réponse... :(, encore", len(list_question)-1, stri,"!\n")
        compteur_fausse += 1
    else :
        print("Bien joué, bonne réponse, encore", len(list_question)-1, stri,"!\n")
        compteur_bonne += 1
    del list_question[0]

t1 = time.time()
total = t1-t0
pourcentage_bonne_rep = (compteur_bonne/(compteur_bonne+compteur_fausse))*100
pourcentage_temps = round(total,2)/nbre_questions

print("Vous avez eu", pourcentage_bonne_rep, "% de bonnes réponses en" , round(total,2),"secondes, soit,", pourcentage_temps, "secondes / question.")

rank = pd.DataFrame({'Pseudo': [pseudo],
                    'pct_rep': [pourcentage_bonne_rep],
                    'pct_temps': [pourcentage_temps]})

rank.to_csv('rank.csv', mode='a', index=False, header=False)

classement = pd.read_csv("rank.csv")

classement_sorted = classement.sort_values(["pct_rep", "pct_temps"], ascending = (False, True))

for index, row in classement_sorted.iterrows():
    if row['Pseudo'] == pseudo:
        previous_pourcentage_bonne_rep = row['pct_rep']
        previous_pourcentage_temps = row['pct_temps']
        index = index
        break 

print('Vous êtes désormais classé n°',index)
        


    