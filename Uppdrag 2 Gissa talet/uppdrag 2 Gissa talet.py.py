# Stores the random number between 1 and 100 in the variable 'number'. Taget ifrån Pythonspot.com
from random import randint

random_number = randint(1, 100) 

#visar siffran i terminal för kontrollkoll av koden.
print(random_number) 

print("Välkommen till gissa talet!")
print ("Du ska gissa på ett tal mellan 1 till 100, så varsågod att gissa på ett tal, du får 3 gissningar!")

#Ger användaren 3 försök
for guess in range(3):
  number = int(input(f"Försök {guess+1}: "))

#Låser spelet för gissningar över 100
  if number >= 101:
    print("Du får bara gissa på tal mellan 1 till 100! Försök igen.")
  elif number <= 0:
    print("Du får bara gissa på tal mellan 1 till 100! Försök igen.")
#kollar om det gissandet numret är samma som random number
  elif number == random_number:
    print("Du gissade rätt! Bra jobbat!")
    
    #break avbryter resten av elif satserna ifall användaren gissade rätt.
    break
#Kollar om gissningen +/- 2 ifrån random number.
  elif abs(number - random_number) <= 2:
     
     #här säker ställer vi om gissningen är lite för högt eller lite för lågt.
     if number < random_number:
        print("Du är nära men inte riktigt, försök gissa på ett lite HÖGRE tal.")
     
     else:
        print("Du är nära men inte riktigt, försök gissa på ett lite LÄGRE tal.")

#meddelare användaren om talet är för stort eller för litet.
  elif (number - random_number) <= 1: 
    print("Ditt tal är för litet, försök igen.")

  elif (number - random_number) >= 1:
    print("Ditt tal är för stort, försök igen.")

else:
  print("Du har försök 3 gånger nu, GAME OVER")























