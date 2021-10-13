#Alexander den Otter   -   99067410
#Imports
import random
import sys
import os
#Imports

#Variabelen
score = 0
AantalGeraden = 0
RandomNummer = random.randint(0,1000)
Ronde = 1
boven50 = RandomNummer + 50
onder50 = RandomNummer - 50
boven20 = RandomNummer + 20
onder20 = RandomNummer - 20
#Variabelen

#Code
while Ronde < 20:
    
    DoorgaanRonde = input('Wilt u doorgaan met de game? (Ja/Nee)\n---> ')
    if DoorgaanRonde == "Ja":
        print('Veel succes met de '+(str(Ronde))+'e ronde!')
    
        while AantalGeraden < 10:
            Gok1 = int(input('------------------------\nGok een nummer tussen de 1-1000\n---> '))
            AantalGeraden = AantalGeraden + 1
            print('------------------------\nDit is je '+ str(AantalGeraden)+'e gok\n------------------------')

            if Gok1 == RandomNummer:
                score = score + 1
                AantalGeraden = 0
                Ronde = Ronde + 1
                print('------------------------\nGoedzo! Je hebt het nummer geraden!')
                print('Je hebt nu een score van: '+str(score)+'\n------------------------')
                break

            elif AantalGeraden == 10:
                AantalGeraden = 0
                Ronde = Ronde + 1
                print('------------------------\nHelaas! Je hebt het nummer niet kunnen raden!')
                print('Je hebt een score van: '+str(score)+'\n------------------------')
                break
                
            elif Gok1 != RandomNummer:
                print('Helaas! Je hebt het niet geraden!')
                if Gok1 <= boven20 and Gok1 >= onder20:
                    print('Je bent heel warm!')
                elif Gok1 <= boven50 and Gok1 >= onder50:
                    print('Je bent warm')

                if Gok1 < RandomNummer:
                    print('Je moet hoger gokken!')
                elif Gok1 > RandomNummer:
                    print('Je moet lager gokken!')
    else:
        break

print('------------------------------------------------------------------------\nBedankt voor het spelen! U heeft een eindscore van: '+(str(score))+' punten\n------------------------------------------------------------------------')
#Code



        
    








    
