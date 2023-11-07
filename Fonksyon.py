# 1. Nan yon chenn karaktè, mete tout karaktè yo an miniskil
chenn ="Mwen Avew fe on sel"
print(chenn.lower())

# 2. Nan yon chen karakte, Koupe chenn nan tout kote ki gen espas. Epi afiche yon liste ki gen chak eleman yo.
print(chenn.split())

# 3. Nan yon karakte, mete tout premye let yo an majiskil
majiskil = chenn.title()
print(majiskil)

# 4. Nan yon chenn karaktè, rekipere premye let chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
var_reprann = chenn.split()
inisyal_chenn = ""
for i in var_reprann:
    inisyal_chenn += i[0]
print(inisyal_chenn)

# 5. Ranplase tout karakte "a" ki nan yon chenn pa "@"
chenn_san_a = chenn.replace("a", "@")
print(chenn_san_a)

# 6. Mete yon chenn karakte devan deye, answit mete l an majiskil.
chenn2 = "JIS PASKE SE OU"
chenn2 = chenn2[::-1]
chenn2 = chenn2.upper()
print(chenn2)

# 7. Afiche endeks premye karakte "a" ki nan yon chenn.
chenn3 = "Ou se chimen reyisit ou"
if "a" in chenn3:
    print(chenn3.index("a"))
else:
    print("Pa gen 'a' nan chenn sa.")

# 8. Afiche total tout endeks karakte "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil).
total = 0
for i in range(len(chenn3)):
    if chenn3[i] == "a" or chenn3[i] == "A":
        total += i
print(total)

# 9. Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil).
list1 = []
for i in range(len(chenn3)):
    if chenn3[i] == "a":
        list1.append(i)
print(list1)

# 10. Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
chenn3 = chenn3.replace(" ", "")
print(chenn3)
