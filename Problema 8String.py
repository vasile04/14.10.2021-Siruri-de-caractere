#PROGRAMEAZĂ! Se consideră şiruri de caractere formate din 
# literele mari ale alfabetului latin şi spaţiu. 
# Elaboraţi un program care afişează şirurile în studiu după următoarele reguli:
#– fiecare literă de la ’A’ până la ’Y’ se înlocuieşte prin următoarea literă din alfabet;
#– fiecare literă ’Z’ se înlocuieşte prin litera ’A’;
#– fiecare spaţiu se înlocuieşte prin ’-’
a=str(input("""Introdu sirul de caractere: \n"""))
b="  "
for i in range(0, len(a)):
    if ord(a[i])!=len(a)-1:
        z=a.replace(chr(ord(a[i])), chr(ord(a[i])+1))
        c=a.replace('Z', 'A')
        d=a.replace(' ', '-')
    print("""Inlocuirea literei din sir prinlitera urmatoare din alfabet si varianta posibila: """, z)
print('SIRUL DE CARACTERE IN CARE Z ESTE INLOCUIT PRIN A','\033[95m',  c)
print(d)