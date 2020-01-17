print ("FYPL Shell 1.0.0\nType \'Main.Interact.HelpMe()\' for support.")
import sys
import pickle
import time
import random
import copy
import keyword
#paradigm
textbuff = []
class Math:
        def Root(x, y):
                return x**(1/y)
        def Less(x, y):
                return min(x, y)
        def Great(x, y):
                return max(x, y)
        class SequenceGenerator:
                def Fibs(n):
                        a, b, c = 0, 1, None
                        for x in range(2, n+1):
                                c = a+b
                                a = b
                                b = c
                        return c
class Lists:
        def ClearList(x):
                while len(x)>0:
                        del(x[0])
class Logic:
        def Yesnt(x):
                return not x
        def And(x,y):
                return x and y
        def Or(x,y):
                return x or y        
class Interact:
        def HelpMe():
                print("FumeiYaziwaPyLang: an esotheric version of obfuscated toadpole (Java-like) Python\nVersion 1.0.0. Alfa-testing")
                print("Do not use in serious projects")
                print("WNet#FY:psk - the official site of corporation\nLOL! There's NO SITE! Suck 404 Not Found! YEAH!")
        def Print(x, sepi, endi):
                print(x, sep = sepi, end =endi)
        def Input(prompt):
                return input(prompt)
class Cipher:
        global basicline
        basicline = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`{|}~АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯв'''
        class GridCipher:
                def Encoding():
                        opentext = []
                        while True:
                                string = input()
                                if string != "///stop///":
                                        opentext.append(string)
                                else:
                                        break
                        for i in range(0, len(opentext)):
                                opentext[i] = opentext[i].upper()
                                if opentext[i] == 'Ь':
                                        opentext[i] = 'Ъ'
                        print(basicline)
                        for x in opentext:
                                for y in x:
                                        for z in basicline:
                                                if z != y:
                                                        print(" ", end = "")
                                                else:
                                                        print("*", end = "")
                                        print()
                                print((" "*100), "*")
                def Decoding():
                        print(basicline)
                        ciphertext = []
                        while True:
                                string = input()
                                if string != "///stop///":
                                        ciphertext.append(string)
                                else:
                                        break
                        for x in ciphertext:
                                if basicline[x.find("*")] == "в":
                                        print()
                                        continue
                                print(basicline[x.find("*")],end = "")
        class HashingQuadriplets:
                def Encoding():
                        opentext = []
                        ciphertext = []
                        while True:
                                string = input()
                                if string != "///stop///":
                                        opentext.append(string)
                                else:
                                        break
                        for i in range(0, len(opentext)):
                                opentext[i] = opentext[i].upper()
                                opentext[i] = opentext[i].replace('Ь', 'Ъ')
                                opentext[i] = opentext[i].expandtabs()
                        for x in opentext:
                                bytetext = ""
                                for y in x:
                                        symb = bin(basicline.find(y)).replace("0b","")
                                        symb = ("0"*(8-len(symb)))+symb
                                        bytetext = bytetext + symb
                                ciphertext.append(str(bytetext))
                        for x in ciphertext:
                                for i in range (0, len(x), 4):
                                        strb = x[i] + x[i + 1] + x[i + 2] + x[i + 3]
                                        print(basicline[int(strb, 2)], end = "")
                                print()
                def Decoding():
                        opentext = []
                        ciphertext = []
                        while True:
                                string = input()
                                if string != "///stop///":
                                        ciphertext.append(string)
                                else:
                                        break
                        for x in ciphertext:
                                bytetext = ""
                                for y in x:
                                        symb = bin(basicline.find(y)).replace("0b", "")
                                        symb = ("0"*(4-len(symb)))+symb
                                        bytetext = bytetext + symb
                                opentext.append(str(bytetext))
                        for x in opentext:
                                for i in range(0, len(x), 8):
                                        strb = x[i] + x[i + 1] + x[i + 2] + x[i + 3] + x[i + 4] + x[i + 5] + x[i + 6] + x[i + 7]
                                        print(basicline[int(strb, 2)], end = "")
                                print()
        class BaconCipher:
                def Encoding():
                        opentext = []
                        ciphertext = []
                        while True:
                                string = input()
                                if string != "///stop///":
                                        opentext.append(string)
                                else:
                                        break
                        # under construction until finding the most convenient way of ciphering (or ways, lol)
                def Decoding():
                        opentext = []
                        ciphertext = []
                        while True:
                                string = input()
                                if string != "///stop///":
                                        ciphertext.append(string)
                                else:
                                        break
                        # the same
