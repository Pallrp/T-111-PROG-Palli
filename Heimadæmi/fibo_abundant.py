

#Þetta forrit gefur val á að:
#Reikna frá 0 upp í innsláða tölu í fibonacci runu
#Eða reikna hvaða tölur frá 0 upp í valdna tölu, eru abundant
#Eða bæði
val = input("Input f|a|b (fibonacci, abundant or both): ")

#Hér byrjar fibonacci runan ef það er valið input
if val == "f" or val == "b":
    max_fibonacci = int(input("Input the length of the sequence: "))
    counter2 = 0
    print("Fibonacci Sequence:")
    print("-------------------")

    #Fibonacci runan ákvarðast af því að fyrstu tvær tölurnar eru 0 og 1 en
    #eftir það er sérhver tala í rununni summa næstu tveggja á undan.
    for num in range(0,max_fibonacci):
        
        if num == 0:
            #Fyrsta talan mun prenta 0 út 
            print(0)
        elif num == 1:
            #Þegar loopan kemur á 1 setur hún gildið "this_count" sem telur nýjasta gildið
            this_count = 1
            print(this_count)
            #Síðan mun hún setja "last_count1" sem gildið sem kom seinast
            last_count1 = 1
            #Og "last_count2" gildið sem kom á undan því
            last_count2 = 0
        else:
            #Þegar runan er komin á 3ju eða seinni lotur byrjar hún að leggja saman
            #Seinustu og þarseinustu runu
            this_count = last_count1 + last_count2
            print(this_count)
            #Eftir það þarf að breyta seinustu og þarseinustu runum
            #Það gerir það í öfugri röð svo last_count2 ruglast ekki sem this_count
            last_count2 = last_count1
            last_count1 = this_count

#Hér byrjar abundant number runan ef það er valið input
if val == "a" or val == "b":
    max_abundance = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    #"Abundant" tala hefur þá eiginleika að summa eiginlegra deila (e. proper divisor) hennar er stærri en talan sjálf.
    #Eiginlegir deilar tiltekinnar heiltölu n eru allar tölur sem eru deilanlegar með n, nema talan sjálf.  

    #Runan byrjar bara að telja ef hæðsta valin tala er 12 eða yfir
    #Því allar tölur undir 12 eru ekki abundant
    if max_abundance >= 12:

        for sequence_count in range(12,max_abundance+1):
            #Runan telur upp í max_abundance og tekur hverja tölu milli 12 - max_abundance í aðra runu sem athugar hvað eru margir deilanlegar tölur við hana
            counter = 0
            #"sequence_count" er í þessu tilfelli hvaða tala í rununni á að athuga hvaða tölur í næstu runu eru deilanlegar með henni
            #Runan sem athugar hvaða tölur eru deilanlegar tekur bara helminginn (round up) af sequence_count til að gera hana hraðari
            #Þá þarf hún ekki að athuga t.d. tölur yfir 12 ef sequence_count er 24. Allar tölur yfir helming eru ekki deilanlegar
            for divisor_count in range(1,(sequence_count//2)+1):
                if sequence_count % divisor_count == 0:
                    #Ef talan er deilanleg þá bætir hún tölunni við í "counter"
                    counter += divisor_count
            #Síðan ef "counter" er stærri tala en talan sjálf þá prentar hún abundant töluna
            if counter > sequence_count:
                print(sequence_count)
