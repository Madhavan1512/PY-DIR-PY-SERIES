from typing import TYPE_CHECKING


x = input("Enter a number x ")
y = input("Enter a number y ")

try :
    z = int(x)/int(y) 
    

except ZeroDivisionError as e :
    print("Exception occured" , e )
    z = None

except TypeError as e :
    print('Exception type ' , type(e).__name__ )
    z = None 
print("Division is ", z)