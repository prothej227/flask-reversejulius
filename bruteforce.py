import func_decrypt as d
from pathlib import Path
import os
import re
from random import randint as r


def findMaximum(word, pos):
    li=word.split()
    li=list(li)
    op=[]
    for i in li:
        op.append(len(i))
    if pos == 'max':
        l=op.index(max(op))
    elif pos == 'random':
        l  = r(0, len(op) - 1)
    return (li[l])

def StripNumeric(strInput):
    return ''.join([i for i in strInput if not i.isdigit()])

def WordHopping(strInput):
    li = list(strInput.split())
    if len(li) <= 10:
        sensitivity = 1
    else:
        sensitivity = 0.75
    selectedWords = []
    count = int(sensitivity*len(li))
    for i in range(count):
        selectedWords.append(re.sub(r'[^\w\s]','',li[r(0, len(li)-1)]).lower()) 
    return selectedWords
    
def SuccessCount(strList, dictionary):
    success_count = 0
    for word in strList:
        if word in dictionary:
            success_count += 1
    return success_count

def ShiftBrute(strInput, dictionary):
        SR_LIST = []
        for i in range(26):
            soln = StripNumeric(strInput[i])
            SR_LIST.append(SuccessCount(WordHopping(soln), dictionary))
        return SR_LIST

def SolnSpace(caesarTxt):
    liSolnSpace = []
    for i in range(0,26):
        liSolnSpace.append(d.Decrypt(caesarTxt,i)) 
    return liSolnSpace

def Bruteforce(solnSpace, brute_dict):
    key = 0
    if brute_dict == "en_us":
       dictionary = open(os.getcwd() + '\words_alpha.txt', 'r').read()
    elif brute_dict == "tl_ph":
       dictionary = open(os.getcwd() + '\words_tl.txt', 'r', errors='ignore').read()   
    for soln in solnSpace:
        soln = StripNumeric(soln)
        if (re.sub(r'[^\w\s]','',soln.split(' ')[soln.split(' ').index(findMaximum(soln, "max"))].lower()) in dictionary) and (len(re.sub(r'[^\w\s]','',soln.split(' ')[soln.split(' ').index(findMaximum(soln, "max"))].lower())) > 6):
            return key, re.sub(r'[^\w\s]','',soln.split(' ')[soln.split(' ').index(findMaximum(soln, "max"))].lower())
        else:
            key = key + 1
            
    #Enforce Forced Hopping
    SR_LIST = ShiftBrute(solnSpace, dictionary)
    return SR_LIST.index(max(SR_LIST)), (str("Forced Word Hopping"))