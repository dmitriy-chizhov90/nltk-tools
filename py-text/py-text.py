#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ispras import texterra
from nltk import WordPunctTokenizer
from nltk import SnowballStemmer

def lemmatizationWordsTexterra(t, aText):
    result = t.lemmatizationAnnotate(aText)
    return [(a['value']) for a in result['annotations']['lemma']]

def stemmWordsNltk(aText):
    result = WordPunctTokenizer().tokenize(aText)
    return [(SnowballStemmer("russian").stem(w)) for w in result]

print('Running...')
t = texterra.API('2eca112748d13582aef0751b7ce9d317b04bc1e2', 'texterra', 'v1')

raw = """ Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина и
    приближенная  императрицы  Марии  Феодоровны,  встречая важного и  чиновного
    князя  Василия,  первого  приехавшего  на  ее вечер. Анна  Павловна  кашляла
    несколько  дней, у  нее был грипп, как она говорила (грипп  был тогда  новое
    слово, употреблявшееся только  редкими).  В записочках, разосланных  утром с
    красным лакеем, было написано без различия во всех:
         "Si vous n'avez rien de mieux à faire, M. le comte (или mon prince), et
    si la perspective de passer la soirée chez une pauvre malade ne vous effraye
    pas  trop,  je serai charmée de vous  voir chez moi  entre 7 et  10  heures.
    Annette Scherer"."""

print(lemmatizationWordsTexterra(t, raw))
print()
print(stemmWordsNltk(raw));

