#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
from bs4 import BeautifulSoup as bs
from nltk import WordPunctTokenizer
from collections import Counter
import matplotlib.pyplot as plt

f = urlopen("http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0040.shtml")
data = f.read().decode("cp1251")
f.close()

text = bs(data).get_text()
tokens = WordPunctTokenizer().tokenize(data)
cnt = Counter(tokens).most_common()

# draw plot
X = range(len(cnt))
Y = [y[1] for y in cnt]
plt.loglog(X, Y)
plt.show()
