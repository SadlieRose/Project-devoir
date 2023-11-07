#Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
diksyonè = {'J25': 'lendi1', 'S302': 'mercredi2'}
lis_valè = list(diksyonè.values())
print("Liste valè yo: \n ", lis_valè)

#Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
valè = input(f"Rantre yon vale: \n ")
if valè.startswith("{") and valè.endswith("}"):
    print("Valè a gen akolad devan ak dèyè.")
else:
    print("Valè a pa gen akolad devan ak dèyè.")

#Pakouri yon diksyonè, epi afiche tout kle yo.
diksyonè = {'kle9': 'valè9', 'M23': 'val2'}
kle = list(diksyonè.keys())
print(f" Afiche tout kle yo: \n ", kle)

#Pakouri yon diksyonè, epi afiche tout valè yo
diksyonè = {'kle9': 'valè9', 'V12': 'val12'}
valè = list(diksyonè.values())
print(f"Liste valè yo: \n ", valè)

#Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
diksyonè_òrijinal = {'kle1': 'valè1', 'Kle2': 'vale2'}
kopi = diksyonè_òrijinal.copy()
print("Diksyonè òrijinal: \n", diksyonè_òrijinal)
print("Kopi a: \n", kopi)

#Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo. E
diksyonè = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 123, 'kle4': 'valè4'}
for kle, valè in diksyonè.items():
    if isinstance(valè, str):
        diksyonè[kle] = f"_{valè}_"
print(f"Afiche: {diksyonè} \n")

#Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman.
diksyonè_orijinal = {'kle1': '123', 'kle2': '456', 'kle3': '789', 'kle4': 'abcdef'}
diksyonè_nouvo = {kle: valè for kle, valè in diksyonè_orijinal.items() if valè.isdigit()}
print(f"Kreye yon nouvo diksyone:{diksyonè_nouvo} \n")

#Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè)
diksyonè = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
lis_tipl = [(kle, valè) for kle, valè in diksyonè.items()]
print(f"Afiche sou fom tipl:{lis_tipl} \n")

#Pakouri yon lis tipl, pou w mete l sou fòm diksyonè. Ekzanp:
lis_tipl = [('kle1', 'valè1'), ('kle2', 'valè2'), ('kle3', 'valè3')]
diksyonè = dict(lis_tipl)
print(f" Metel sou fom diksyone:{diksyonè} \n")

#Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo:
diksyonè1 = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
diksyonè2 = {'kle2': 'valè4', 'kle4': 'valè5', 'kle5': 'valè6'}

# Kole 2 diksyonè ansanm nan yon nouvo diksyonè
diksyonè_kole = {kle: valè for diksyonè in [diksyonè1, diksyonè2] for kle, valè in diksyonè.items()}
print(f"Nouvo diksyone:{diksyonè_kole} \n")

