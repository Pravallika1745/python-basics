Telugu = float(input("Enter Telugu marks: "))
Hindi = float(input("Enter Hindi marks: "))
English = float(input("Enter English marks: "))
Maths = float(input("Enter Maths marks: "))
Science = float(input("Enter Science marks: ")) 
Social = float(input("Enter Social marks: "))
total = Telugu+Hindi+English+Maths+Science+Social
percentage =(total/600)*100
print("Your total marks are: "+str(total))
print("Your percentage is: " +str(percentage))
if(percentage>=90):
    print("A grade")
elif(percentage>=80):
    print("B grade")
elif(percentage>=70):
    print("C grade")
elif(percentage>=60):
    print("D grade")
elif(percentage>=40):
    print("E grade")
else:
    print("You are failed")


    


