 # -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:59:11 2021

@author: ettor
"""
import random

def randomWord_by_letters(string_of_letters,times):
    b = []
    final = ""
    invented = []
    for i in range(1,int(times)):
        for i in string_of_letters:
            b.append(i)
        
        for letters in string_of_letters:
            a = random.randint(0, len(b)-1)
            final+=b[a]
            del b[a]
            
        #print(final)
        invented.append(final)
        final = ""
        # print(used_words)
    return invented
# parola = input("Inserisci la parola ")
# parola1 = input("Inserisci Il numero ")
# a = randomWord_by_letters(parola,parola1)
# find = input("FIND ")
# if find=="show":
#     print(a)
# for letters in a:
#     if letters == find:
#         print(letters)
        