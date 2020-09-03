n = int(input("Enter the length of the sequence: ")) # Do not change this line

#1
#2=1+1
#3=2+1
#6=3+2+1
#11=6+3+2
#20=11+6+3
#37=20+11+6
last_num1 = 1
last_num2 = 1
last_num3 = 1
latest_num = 1

for i in range(0,n):
    


    if i == 0:# = 1
        print(latest_num)

        last_num1 = latest_num
    elif i == 1: # = 2
        latest_num = last_num1 + last_num2
        
        print(latest_num)
        last_num3 = 1
        last_num2 = last_num1
        last_num1 = latest_num
    elif i == 2: # = 3
        latest_num = last_num1 + last_num3 
        
        print(3)
        last_num3 = last_num2
        last_num2 = last_num1
        last_num1 = latest_num
    else:
        latest_num = last_num3 + last_num2 + last_num1
        print(latest_num)
        last_num3 = last_num2
        last_num2 = last_num1
        last_num1 = latest_num

