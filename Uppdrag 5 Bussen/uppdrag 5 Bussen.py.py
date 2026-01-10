import replit

# klass för Passagerare
class Passenger:
    def __init__(self, age):
        self.age = age 

    def __str__(self):
        return f"{self.age} år" 
    
    def get_age(self):
        return self.age

# klass för Buss
class Buss:
    def __init__(self):
        self.passengers = []  

    # Funktion för att köra programmet/ menyn
    def run(self):
        while True:
            replit.clear()
            print("Välkommen till Tor-Tors Buss-simulatorn")
            print("==========================================================")
            print("Välj ett nummer ifrån menyn och tryck Enter för att välja")
            print("==========================================================")
            print("1: Lägg till en ny passagerare")
            print("2: Visa ålder på samtliga passagerare")
            print("3: Beräkna totala åldern på alla passagerare")
            print("4: Beräkna genomsnittliga åldern på alla passagerare")
            print("5: Visa den äldsta passageraren")
            print("6: Sök efter en specifik ålder")
            print("7: Sortera bussen efter ålder")
            print("8: Avsluta programmet\n")
            
            # Funktion som gör så att man bara kan skriva in siffror och skriva in siffror mellan 1-8
            try:
                x = int(input("Var god och välj ett nummer från menyn: "))
            except ValueError:
                print("Ogiltig input! Vänligen välj ett nummer mellan 1 och 8.")
                input("Tryck Enter för att försöka igen.")
                continue

            # Anropa respektive funktion beroende på användarens val
            if x == 1:
                self.add_passenger()
            elif x == 2:
                self.print_bus()
            elif x == 3:
                self.calc_total_age()
            elif x == 4:
                self.calc_average_age()
            elif x == 5:
                self.max_age()
            elif x == 6:
                self.find_age()
            elif x == 7:
                self.sort_buss()
            elif x == 8:
                replit.clear()
                print("Du har valt att avsluta programmet")
                input("Tryck Enter för att avsluta.")
                return
            # Säger till om användaren inte valde ett giltigt alternativ
            else:
                replit.clear()
                print("Du gjorde inte ett giltigt val.\nGå tillbaka till menyn för att göra ett nytt val.")
                input("Tryck Enter för att gå tillbaka till menyn")



    # Funktion för att lägga till passagerare
    def add_passenger(self):
        while True:
            replit.clear()
            
            # Sätter ett max antal i bussen vilket är 25 och kollar om bussen är full
            if len(self.passengers) >= 25:
                print("Bussen är tyvärr full.")
                input("Tryck Enter för att gå tillbaka till menyn.")
                break
            else:
                try:
                    passenger_age = int(input("Hur gammal är passageraren du vill lägga till?: "))
                except ValueError:
                    print("Vänligen skriv in ett giltigt nummer för ålder.")
                    continue
            
            # Skapa en instans av Passenger och lägg till den i listan self.passengers
            new_passenger = Passenger(passenger_age)
            self.passengers.append(new_passenger)
            print(f"Passagerare med ålder {passenger_age} har lagts till.")

            # Ge användaren ett val om de vill lägga till fler passagerare eller gå tillbaka
            choice = input("Vill du lägga till en ny passagerare? (ja/nej): ").lower()
            if choice == "nej":
                break

    # Funktion för att skriva ut alla passagerare
    def print_bus(self):
        replit.clear()
       
        if  len(self.passengers) < 1:
            print("Det finns inga passagerare i bussen.")
            input("Tryck Enter för att gå tillbaka till menyn")
            return
        elif len(self.passengers) >=1:
            print("passagerare som finns i bussen är åldrarna:")
            for passenger in self.passengers:
                print(passenger)
            print("\nDet finns totalt", len(self.passengers), "passagerare i bussen.")
            input("Tryck Enter för att gå tillbaka till menyn")
    
    # Funktion för att beräkna den totala åldern på alla passagerare
    def calc_total_age(self):
        replit.clear()
        total_age = sum([passenger.age for passenger in self.passengers])  # Använd .age för att summera åldrarna
        print(f"Den totala åldern på alla passagerare är {total_age} år")
        input("Tryck Enter för att gå tillbaka till menyn")
  
    # Funktion för att beräkna den genomsnittliga åldern på alla passagerare
    def calc_average_age(self):
        replit.clear()
        if len(self.passengers) > 0:
            average_age = sum([passenger.age for passenger in self.passengers]) / len(self.passengers)
            print(f"Den genomsnittliga åldern på passagerarna i bussen är {average_age:.2f} år")
        else:
            print("Det finns inga passagerare i bussen\nLägg till passagerare först sen testa igen\n")
        input("Tryck Enter för att gå tillbaka till menyn")
    
    # Funktion för att hitta den äldsta passageraren
    def max_age(self):
        replit.clear()
        if self.passengers:
            max_age = max([passenger.age for passenger in self.passengers])  # Hitta max ålder
            print(f"Den äldsta passageraren i bussen är {max_age} år.")
        else:
            print("Det finns inga passagerare i bussen\nLägg till passagerare först sen testa igen\n")
        input("Tryck Enter för att gå tillbaka till menyn")
    
    # Funktion för att hitta en specifik ålder eller en åldersgrupp
    def find_age(self):
        while True:
            replit.clear()
            print("1: Sök efter en specifik ålder")
            print("2: Sök efter en åldersgrupp\n")
            try:
                y = int(input("Välj mellan alternativ 1 eller 2: "))
                break
            except ValueError:
                print("Vänligen skriv in ett giltigt nummer för ålder.")
        
        # Delen där man söker efter en speficik ålder
        if y == 1:
            age_one = int(input("Skriv in åldern du vill söka efter: "))
            found = False
           
            for passenger in self.passengers:
                if passenger.age == age_one:
                    print(f"Åldern {age_one} finns i bussen.")
                    found = True   
                    break
           
            # säger till om åldern inte finns i bussen
            if not found:
                print(f"Åldern {age_one} finns inte i bussen.")
            input("Tryck Enter för att gå tillbaka till menyn")
        
        # Delen där man söker efter en åldersgrupp
        elif y == 2:
            age_two = int(input("Skriv in den yngsta åldern i åldersgruppen: "))
            age_three = int(input("Skriv in den äldsta åldern i åldersgruppen: "))
            found = False
            
            for passenger in self.passengers:
                if age_two <= passenger.age <= age_three:
                    print(f"Åldern {passenger.age} finns i bussen.")
                    found = True
                    break
            
            # säger till om ingen passagerare matchade åldersgruppen
            if not found:
                print(f"Ingen passagerare matchade åldersgruppen {age_two}-{age_three}.")
            input("Tryck Enter för att gå tillbaka till menyn")
        
    # Funktion för att sortera bussen efter ålder
    def sort_buss(self):
        replit.clear()
        self.passengers.sort(key=Passenger.get_age)
        
        # Skriv ut passagerare om det finns några i bussen annars säger att det är tomt
        if len(self.passengers) < 1:
            print("Det finns inga passagerare i bussen.")
            
        elif len(self.passengers) >= 1:
            print("Passagerare i bussen sorterade efter ålder:")
            for passenger in self.passengers:
                print(passenger)
        
        input("\nTryck Enter för att gå tillbaka till menyn")

class Program:
    def __init__(self, *args):
        # Skapar ett objekt av klassen Buss och kör programmet
        minbuss = Buss()
        minbuss.run()
        input("Press Enter to continue . . . ")

# Kör programmet
if __name__ == "__main__":
    # skapa en instans (kopia) av klassen Program 
    my_program = Program()
