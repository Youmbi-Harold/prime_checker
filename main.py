#Write your code below this line ๐
def prime_checker(number):
  check = True
  for a in range(2, number):
    if number % a == 0:
      check = False
    if check:
      print("it is a Prime number")
    else :
      print("It is not Prime number ")
      
    
  
  
    
    
  




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



