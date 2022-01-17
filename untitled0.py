# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:43:07 2022

@author: Jean
"""
import pandas as pd
import random
import numpy as np
import time

questions = pd.read_csv(r"C:\Users\Jean\Downloads\QCM.csv")

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
list_question = questions_alea(4, len(questions))
compteur_bonne = 0
compteur_fausse = 0   
t0 = time.time()
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
print("Vous avez eu", compteur_bonne, "reponses justes et", compteur_fausse, "réponses fausses en", round(total,2),"secondes !")
    