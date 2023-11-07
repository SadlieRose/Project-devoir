# Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n = 10
list1 =[]
list1 = [ i for i in range(n + 1) if i % 2 == 0]
print (f"Lis eleman divizib pa 2 yo se:{list1} \n")

# Ou gen yon lis antye, konvèti l an yon lis chenn.
chenn1 = ''.join(map(str, list1))
print(f"Afiche lis chenn:{chenn1} \n")

#Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis_miniskil = ["it's never to late to do better \n"]
lis_majiskil = [mo_ki_majiskil.upper() for mo_ki_majiskil in lis_miniskil]

print(f"Afiche lis chenn en majiskil:{lis_majiskil} \n")

#Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
list2=[]
lis_orijinal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nouvo_lis = [eleman for i, eleman in enumerate(lis_orijinal) if i % 3 == 0]

print(f"Endeks ki divizib pa 3 yo se:{nouvo_lis} \n")

#Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl
lis_orijinal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

nouvo_lis = [lis_orijinal[i:i+3] 
for i in range(0, len(lis_orijinal), 3)]

print(f"Afiche nouvo lis eleman ki gwoupe ansanm yo:{nouvo_lis} \n")
#Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
lis_av_doublon = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
lis_san_doublon = list(set(lis_av_doublon))
print(f"Nonb ki nesese yo :{lis_san_doublon} \n")

#Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo
list1 = [0,1, 2, 3, 4, 5,6,7,8,9,10]
list2 = [3, 4, 5, 6, 7]
lis_komen = list(set(list1) & set(list2))
print(f"lis komen an se: {lis_komen} \n")

#Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo
lis1 = [0,1, 2, 3, 4, 5,6,7,8,9,10]
lis2 = [3, 4, 5, 6, 7]
lis_distenge = list(set(lis1) ^ set(lis2))
print(f"Lis distenge a se: {lis_distenge} \n")

#Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.

diksyonè = {'Sadlie': 26, 'Jims': 17, 'Bernard': 16, 'Bren': 23}
lis_kle = list(diksyonè.keys())
lis_valè = list(diksyonè.values())
print("Liste kle yo: \n", lis_kle)
print("Liste valè yo: \n", lis_valè)

#Reyini 3 lis ansanm, san okenn doublon.
list1 = [0,1, 2, 3, 4, 5,6,7,8,9,10]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

lis_reyini= lis1 + lis2 + list3  
lis_san_doublon = list(set(lis_reyini))
print(f"Afiche lis ki san okenn doublon: {lis_san_doublon} \n")
  


