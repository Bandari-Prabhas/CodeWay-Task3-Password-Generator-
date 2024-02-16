# First We need to import the random module to generate the random pattern
import random 
# Since the password must be in combination any one form of letters,numbers,symbols we are taking all of them into the lists
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','.','/']
print("****************** W-E-L-C-O-M-E T-O P-A-S-S-W-O-R-D G-E-N-E-R-A-T-O-R: ******************")
# Asking the user to Enter the no.of letters for password and storing it in a no_of_letters variable
no_of_letters=int(input("Enter the no.of letters you want in your password:"))


# Asking the user to Enter the no.of letters for password and storing it in a no_of_numbers variable
no_of_numbers=int(input("Enter the no.of numbers you want in your password:"))


# Asking the user to Enter the no.of letters for password and storing it in a no_of_symbols variable
no_of_symbols=int(input("Enter the no.of Symbols you want in your password:"))



# first taking the one empty list
password_list=[]
# from the specified number of letters it will take some random letters and append it to the empty list
for i in range(1,no_of_letters+1):
     char=random.choice(letters)
     password_list+=char

# from the specified number of numbers it will take some random letters and append it to the empty list
for i in range(1,no_of_numbers+1):
     char=random.choice(numbers)
     password_list+=char

# from the specified number of symbols it will take some random letters and append it to the empty list
for i in range(1,no_of_symbols+1):
     char=random.choice(symbols)
     password_list+=char

# after appendig all those then we have to suffle them  and printing it 
random.shuffle(password_list)
password=""
for i in password_list:
     password+=i
print("Your Password is Successfully Generated:",password)
     

     