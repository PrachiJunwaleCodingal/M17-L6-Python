#leap year
  
def leap(Y):   
  if((Y % 400 == 0) or  (Y % 100 != 0) and  (Y % 4 == 0)):   
    print("Its a leap Year");   
  else:  
    print ("Its not a leap Year")  

Y = int(input("Enter the year: "))  
leap(Y)