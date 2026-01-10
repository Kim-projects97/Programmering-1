

from random import randint 

# stoppar användaren ifrån att skriva in något annat än int
def take_input(s):
  while True != int:
    number = input(s)
    try:
      int(number)
      break
    
    except ValueError:
      print("Du måste ange ett tal")
    
  return int(number)

# ifall användaren skriver in 0(noll) så används denna funktion med funktionen på rad 23
def zero():
  return randint(1, 1000) 

# omvandlar fahr till cel eller anropar zero() om användaren angav 0(noll)
def fahr_to_cel(i):
  if i == 0:
    i = zero()
    print(f"Talet får inte vara 0 så vi slumpar det till {i}")
  
  return float((i - 32) * 5 / 9)

# Användaren skriver in Fehrenheit grader.
fahrenheit = take_input("Ange ett heltals värde i Fahrenheit: ") 

# Anropa metoden och omvandla Fahrenheit till Celsius
celsius = fahr_to_cel(fahrenheit)  
 
# kollar om värmen är lagom, för kallt eller för varmt, upprepas till värmen är lagom
def bastu_warmth(celsius):
  cold = 82
  hot = 87 
  bastu_warmth = True
  bastu_celsius = celsius
 
  while bastu_warmth:

# Skriver ut om det är för kallt i bastun och hur många grader det är i celsius
    if bastu_celsius < cold:
      print(f"Det är för kallt, det är bara {bastu_celsius:.2f} grader i bastun")
      bastu_fahrenheit = take_input("Testa höj värmen: ")
      bastu_celsius = fahr_to_cel(bastu_fahrenheit)

# Skriver ut om det är för varmt i bastun och hur många grader det är i celsius
    elif bastu_celsius > hot:
      print(f"Det är för varmt, det är hela {bastu_celsius:.2f} grader i bastun")
      bastu_fahrenheit = take_input("Testa sänk värmen: ")
      bastu_celsius = fahr_to_cel(bastu_fahrenheit)

#  skriver ut om det är lagom värme i bastun
    else:
      print(f"Nu är det lagom värme i bastun, det är {bastu_celsius:.2f} grader")
      bastu_warmth = False
    print()


bastu_warmth(celsius)


# Användaren som är en amerikan skriver in bastutemperatur i fahrenheit. Temperaturen skrivs in som heltal. ///////////
# Din metod fahr_to_cel omvandlar Fahrenheit till Celsius och returnerar värdet som decimaltal. Detta kallas typomvandling.  ///////////
# Ditt program kontrollerar om temperaturen är i intervallet 82-87 och svarar med ett meddelande ///////////
# ”Det är för varmt” /////////
# ”Det är för kallt” ////////////
# ”Temperatren är lagom” ////////////
# Koden upprepas tills temperaturen är lagom ////////////////
# Programmet fungerar korrekt, är kommenterad och strukturerad  //////////////
# Du har implementerat metoden korrekt även om metoden returnerar heltal  ////////
# Undantagshanteringen är implementerat på ett godtagbart sätt ///////////
# Metoden tar emot ett värde (argument) som är heltal och returnerar ett värde som är decimaltal /////////
# Upprepningen av koden, loopen fungerar korrekt //////////////
# Undantagshanteringen är implementerad och korrekt placerad ////////////////////
# Du ska arbeta med ytterligare en metod och som ska fungera som en överlagrad metod (eng: "overloaded methods"). Om användaren skriver in 0(noll) istället 
# för ett värde så ska den nya metoden användas istället på ett lämpligt sätt.
# Python: Den nya metoden ska slumpa fram ett tal och därefter i sin tur returnera värdet till den ursprungliga metoden (med argument) för omvandling mellan Fahrenheit och Celsius. 