import random

# Slumpa 10 tal mellan 1 och 20 och lagra dem i en lista
# random.sample skapar en lista direkt och unvdiker dupletter.
bingo_numbers = random.sample(range(1, 21), 10)

print("Välkommen till BINGO! I det här Bingo spelet får du bara gissa på tal mellan 1 och 20. Du kommer få skriva in 10 olika siffror i din bingo bricka\n")
# Skapa en lista för användarens tal
user_bingo_list = []

# Låter användaren ange 10 tal
for guess in range(1, 11):
    
     while True:
        bingo_guess = int(input(f"Ange tal på plats {guess}: "))
        
        #stoppar användaren ifrån att gissa på tal som inte ingår i bingot och låter användaren skriva in nytt tal
        if bingo_guess < 1 or bingo_guess > 20:
            print("Du får skriva in nummer mellan 1 och 20 i det här bingo spelet!\n")
        
        elif bingo_guess in user_bingo_list:
            print("Det talet har du redan valt! Välj ett annat tal.\n")
        
        #om talet inte gissat på tidigare och är inom 1-20 så läggs den till i användarens lista
        else:
            user_bingo_list.append(bingo_guess)
            break

# Skriver ut både användarens och de slumpade bingo talen
print("Dina gissningar:", user_bingo_list)
print("Bingo talen är:", bingo_numbers)

# Jämför gissningen och slumpade talen och skriv ut "Bingo" för varje matchning 
bingo_points = 0
for bingo_guess in bingo_numbers:
    
    if bingo_guess in user_bingo_list:
        
        print(f"Bingo {bingo_guess}")
        
        bingo_points += 1

print(f"Du fick {bingo_points} poäng.")



#Slumpa fram ett tal.  ///////////////////////

#Skapa sedan en lista med plats för tio tal ////////////////////

#Iterera genom de tio platserna i listan och låt användaren ange ett tal som skrivs in på respektive position i listan.  /////////////////

#Iterera genom din lista med tal och jämför med det slumpade talet. Programmet skriver ut ”Bingo” om det slumpade talet finns i listan  ///////////////

#Koden är lättläst, lätt att förstå och skriven enligt instruktioner  ///////////////

#Koden är kommenterad och strukturerad/logisk indelad  ///////////////////

#Variablerna är korrekt namngivna   /////////////////

#Slumpa fram tio tal och lagra dem i en lista ////////////////////

#Skapa en lista/array med plats för tio tal /////////////////////////

#Låt användaren fylla på listan genom att skriva in 10 tal ///////////////////////////

#Jämför de slumpade talen med de inskrivna talen  ////////////////////////

#Programmet skriver ut ”Bingo” för varje tal som finns i båda listorna ////////////////////////

#Implementera en tvådimensionell bricka för bingoraden så att den mer efterliknar en Bingobricka.  

#Brickan ska ha dimensionerna 5x5 och du ska då istället slumpa fram tal mellan 1 och 25. 

#Inga bollar visar samma tal mer än en gång, samt att användaren inte kan ange samma tal mer än en gång. 
#Varje gång användaren matar in ett tal ska en träff markeras som X på 5x5 brickan. Detta så man se om det är träff: vågrätt, lodrätt eller diagonalt. Är det ingen träff ska inget markeras.
#Användaren får ”Bingo” först när han får fem ”samma tal” vågrätt, lodrätt eller diagonalt. 