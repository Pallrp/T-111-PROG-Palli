import math

#Forritið reiknar og skrifar út niðurstöður úr þvi að kalla á tiltekin stærðfræðileg föll
#sýnir 4 valmöguleika, biður um endurtekið um input þar til 'x' er slegið.
#ef óleifilegt val er slegið þá prentar forritið út villukóða
#biður notandann um heiltölu sem tengist sérhverju vali
#skrifar niðurstöðuna, sem er annaðhvort villa eða tölulegt gildi

#sum_natural(n_str): Þetta fall tekur streng, sem stendur fyrir tölulegt gildi n >= 2,
#sem viðfang og skilar summu fyrstu n talnanna.
#Ef viðfangið er ekki leyfilegt þá skilar fallið None.
def sum_natural(inpt):
    the_sum = 1
    #Runan er einföld, hún byrjar á öðrum reit því það má ekki velja undir 1
    #Hún telur upp að insslegni tölu og leggur allt saman vil the_sum
    for numb in range(2,inpt+1):
        the_sum += numb
    return the_sum

#sum_fibonacci(n_str):  Þetta fall tekur streng, sem stendur fyrir tölulegt gildi n >= 2, 
#sem viðfang og skilar summu fyrstu n Fibonacci-talnanna. 
#Ef viðfangið er ekki leyfilegt þá skilar fallið
def sum_fibonacci(inpt):
    the_sum = 0
    #Til að gera fallið aðeins hraðari lét ég fremstu "if" yrðinguna setja í gang rununa
    if inpt > 2:
        #Runan byrjar á þriðju endurtekningu
        #Gildin sem komu fyrr í rununni eru skilgreind hér
        last_count2 = 0
        last_count1 = 1
        this_count = 0
        the_sum = 1
        for num in range(2,inpt):
            this_count = last_count1 + last_count2
            last_count2 = last_count1
            last_count1 = this_count

            the_sum += this_count
        #Fallið skilar síðan út summuna af fibonacci rununni
        return the_sum
    #Ef aðrar tölur undir 3 eru valdnar þarf ekki rununa
    elif inpt == 1:
        return 0
    elif inpt == 2:
        return 1

#approximate_euler(n_str): Þetta fall tekur streng, 
#sem stendur fyrir tölulegt gildi n >= 2, sem viðfang og skilar nálgun fyrir Euler töluna 
#(talan e sem er grunnur fyrir náttúrulegan lógariþma)  
#Hin útreiknaða tala er námunduð með 5 aukastöfum áður en henni er skilað. 
#Ef viðfangið er ekki leyfilegt þá skilar fallið None.  
#Í útfærslunni má nota math.factorial() fallið.
def approximate_euler(inpt):
    the_sum = 1
    for iteration in range(1,inpt):
        current_num = 1/math.factorial(iteration)
        the_sum += current_num
    return round(the_sum,5)

#Ég ákvað einnig að setja fjórða fallið, sem verður notað í hvert skipti sem spurt er notanda
#Um að slá inn tölu. Fallið er skothelt og skilar bara út jákvæðum heiltölum
#Ef eitthvað annað er slegið, neikvæð tala, float eða ekki tala; skilar fallið villuboð
def num_choice():
    func_choice = input("Enter N: ")
    if func_choice.isdigit() == True:        
        func_choice = int(func_choice)
        if func_choice > 1:
            return func_choice
        else:
            print("Error: {} was not a valid number.".format(func_choice))
            return 0

    else: 
        print("Error: {} was not a valid number.".format(func_choice))
        #Fallið má ekki skila út None, því þá virka yrðingar eins og "<", meðal annars, ekki fyrir neðan
        return 0
    


#Hér byrjar aðalforritið að keyra
print("Please choose one of the options below:")
print("a. Display the sum of the first N natural numbers. ")
print("b. Display the sum of the first N Fibonacci numbers. ")
print("c. Display the approximate value of e using N terms.")
print("x. Exit from the program.\n")
the_loop = 0
choice2 = 0

while the_loop != 'This loop will break WHEN I SAY SO, DAMN IT!':

    choice = input("Enter option: ").lower()
    if choice == "a":
        choice2 = num_choice()
        if type(choice2) != str: #Ef num_choice() myndi returna None, virka þessi föll ekki
            if choice2 > 1:         
                print("Natural number sum: {} \n".format(sum_natural(choice2)))

    elif choice == "b":
        choice2 = num_choice()
        if type(choice2) != str:
            if choice2 > 0:
                print("Fibonacci sum: {} \n".format(sum_fibonacci(choice2)))


    elif choice == "c":
        choice2 = num_choice()
        if type(choice2) != str:
            if choice2 >= 2:
                print("Euler approximation: {} \n".format(approximate_euler(choice2)))

    #Lúppan mun bara brotna ef X er valið
    elif choice == "x":
        break
    #Ef ekkert af valmöguleikunum er slegið inn minnir forritið notanda aftur á valmöguleika
    else:
        print("Unrecognized option {}".format(choice))
        print("Please choose one of the options below:")
        print("a. Display the sum of the first N natural numbers. ")
        print("b. Display the sum of the first N Fibonacci numbers. ")
        print("c. Display the approximate value of e using N terms.")
        print("x. Exit from the program.\n")
