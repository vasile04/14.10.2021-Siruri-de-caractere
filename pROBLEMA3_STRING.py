#PROGRAMEAZĂ! Elaboraţi un program care propune elevului să introducă de
#la tastatură, în două linii:
#	 – numele şi prenumele elevului/elevei;
#	 – profesia la care el/ea aspiră.
np=str(input('introdu numele prenumele: \n' ))
pr=str(input('introdu profesia: \n'))
print("""Te numesti: {numeprenume}.  \n 
Iti place profesia: {profesie}. """. format(numeprenume=np, profesie=pr))