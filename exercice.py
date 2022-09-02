#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ntpath import join


def majuscule(mot):
    # TODO completer la fonction ici
    
    # list ou stoker les lettres converties en majuscule
    letter=[]

#prendre chaque lettre du mot pour la convertir en code ASKII
    for element in mot:
        #convertir srting en int
       aski = ord(element)
       #ajouter la transfromation au int pour passer du ASKII miniscule a majuscule
       aski = aski - 32
       #convertir int en string en utilisant les ASKII
       aski = chr(aski)
       #mettre chaque lettre majuscule dans une liste
       letter.append(aski)

    #joindre les  lettres de la liste pour former le mot
    mot =''.join(letter)
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
