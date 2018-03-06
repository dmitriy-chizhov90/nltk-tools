#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as bs
import re
import nltk
from ispras import texterra

f = request.urlopen("http://az.lib.ru/g/gomer/text_0030.shtml")
data = f.read().decode("cp1251")
f.close()

soup = bs(data, "html.parser")

def print_tag(aTag):
    print (len(aTag.contents))
    print ([(c.name if c.name else c) for c in aTag.contents])

def lemmatizationWordsTexterra(aText):
    t = texterra.API('2eca112748d13582aef0751b7ce9d317b04bc1e2', 'texterra', 'v1')
    result = t.lemmatizationAnnotate(aText)
    return [(a['value']) for a in result['annotations']['lemma']]

find_result = soup.find_all(string = re.compile("Гнев, богиня, воспой Ахиллеса, Пелеева сына,"))

if len(find_result) != 1:
    print (find_result)
    print ("Len of result is strange: ", len(find_result))
    sys.exit();

dict = lemmatizationWordsTexterra(find_result[0])

print (dict)



