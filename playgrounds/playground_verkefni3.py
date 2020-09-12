max_abundance = int(input("Input the max number to check: "))
print("Abundant numbers:")
print("-----------------")
if max_abundance >= 12:
    for sequence_count in range(1,max_abundance+1):
        #Runan telur upp í max_abundance, fer síðan í aðrar lúppur og tékkar hvort talan sé deilanleg með öllum að neðan
        counter = 0
        for divisor_count in range(1,sequence_count):
            if sequence_count % divisor_count == 0:
                counter += divisor_count
                #Ég vil að runan vistar töluna í rununni og bætir henni við counter 2, sem á að safnast saman í >16 til að vita að talan er abundant
            else:
                continue
        if counter > sequence_count:
            print(sequence_count)
else:
    pass