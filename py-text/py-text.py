#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib, re

print ('Running...')
pattern = r"[0-9]+"
number_re = re.compile(pattern)
print (number_re.findall("122 234 65435"))



print ('End')
