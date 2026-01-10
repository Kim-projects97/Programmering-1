# Stores the random number between 1 and 100 in the variable 'number'. Taget ifrån Pythonspot.com
from random import randint



def game_round():
  random_number = randint(1, 100) 

#visar siffran i terminal för kontrollkoll av koden.
  print(random_number)

  print("Välkommen till gissa talet!")
  print ("Du ska gissa på ett tal mellan 1 till 100, spelet fortsätter tills du gissar rätt!(max 10 gissningar)")
   
  
  guess = 0
  game_on = True
  #La till variabel för lättare att jobba med och ifall man vill öka antalet rundor
  attempts = 10
  
#Ger kör igenom spelet till 10 försök om inte användaren träffar rätt
  while game_on and guess < attempts:
    number = int(input(f"Försök {guess+1}: "))
    
    guess += 1
    
#Låser spelet för gissningar över 100
    if number >= 101 or number <= 0:
      print("Du får bara gissa på tal mellan 1 till 100! Försök igen.")

#kollar om det gissandet numret är samma som random number
    elif number == random_number:
      print(f"Du gissade rätt! Bra jobbat! Det tog dig {guess} antal försök")
      game_on = False
    
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

    if guess == attempts:
        print("Du har gissat fel för många gånger, GAME OVER")
        game_on = False

    
  return guess  # Returnerar antal försök


#funktion om användaren väljer att spela vidare eller avsluta
def play_more():
  guess_history = []
  play_again = True
  
  while play_again:
    #kör en runda och sparar antalet gissningar
    guess_count = game_round()
    guess_history.append(guess_count)
    
    #Frågar om användaren vill spela en omgång till
    player_answer = input("Vill du spela en omgång till? Ja eller nej: ").lower()
  
    #Om användaren skriver nej så avslutas spelet
    if player_answer != "ja":
      play_again = False  
      print()
    
    #Visar användaren den minsta gissningen som behövdes för att hitta rätt tal
    if guess_history:
      best_guess = min(guess_history)
      print(f"Tack för du spelade! Din bästa gissning var {best_guess} antal förök!")  
      
play_more()
#Koden ska upprepa inmatningen till man gissat rätt. /////////////////////////

#Du använder en bool-variabel för att fastslå när talen är lika /////////////////////////////////

#Du jämför talen direkt mot varandra i while-satsen.  ////////////////////////////////

#Programmet håller reda på hur många gånger koden upprepats och skriver ut det på skärmen ////////////////////////////

#Programmet/Spelet avslutas efter tio gissningar. //////////////////////////////////////

#Programmet ska hantera flera spelomgångar. När en spelomgång är slut så kan man välja att spela ytterligare en omgång. Eller att man avslutar spelet. /////////////////////////

#Du ska hålla reda på vilken spelomgång som du har gissat minst antal gånger för. När spelaren väljer att avsluta programmet så ska rekordet visas. ////////////////////
