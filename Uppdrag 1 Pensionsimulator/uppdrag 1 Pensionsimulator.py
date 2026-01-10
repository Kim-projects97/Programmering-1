print("Välkomna till denna pensionsimulator!")

print("Vad heter du i förnamn?")
name = input()

#input blir till int direkt för lättare användning senare
print("Hur gammal är du?")
age = int(input())

#satte 70 som pensionsålder men går att ändra, glöm ej ändra rad 16 om ändring görs
pension = 70

years_untill_pension = pension - age

#Kollar om åldern är i pensions åldern redan
if age >= 70:
  print ("Du är gammal nog att gå i pension om du inte redan har gjort det, njut av pensionen!")

else: print("Hej " + name + ","  " du kommer gå i pension om " + str(years_untill_pension) + "år, fortsätt kämpa!")

input("Press any key to continue. . . ")



