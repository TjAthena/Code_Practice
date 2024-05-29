#string palindrome 

#code = input("enter a string : ")
#a=code[0]
#b=code[-1]
#print(a)
#print(b)
#if(a==b):
#    print("number is palindrome ")
#else:
#    print("not palindrom")

################################################################################################4
code = "Hello"
guess=""
guess_count = 0
guess_limit = 3
Out_of_Guess = False 
while(guess_count<guess_limit):
    if(guess!=code and not Out_of_Guess):
        guess=input("enter a guess : ")
        guess_count+=1
    else:
        Out_of_Guess = True
if Out_of_Guess:
    print("you lose") 
else:
    print("you win ")

