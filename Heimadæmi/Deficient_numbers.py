inpt = int(input("Input to which number to check for Natural numbers"))



print("Abundant numbers:")
print("-----------------")
#"Abundant" tala hefur þá eiginleika að summa eiginlegra deila (e. proper divisor) hennar er stærri en talan sjálf.
#Eiginlegir deilar tiltekinnar heiltölu n eru allar tölur sem eru deilanlegar með n, nema talan sjálf.  
#Runan byrjar bara að telja ef hæðsta valin tala er 12 eða yfir
#Því allar tölur undir 12 eru ekki abundant
for sequence_count in range(1,inpt+1):
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
    if counter == 1:
        print(sequence_count)
