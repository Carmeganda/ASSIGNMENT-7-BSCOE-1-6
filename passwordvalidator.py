#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex. input: P@ssw0rd+P@ssw0rd
#ouput: Valid
#Tip: loop through each character of the input then process it letter by letter

#STEPS:
#1. Ask for the password:
print("Good day, kindly input your password below\U0001F601")
password = input("\n\33[3mYour password\33[0m: ")
print("\33[94mGood day, kindly input your password below\U0001F607.")
password = input("\n\33[3m\33[35mYour password\33[0m:\33[36m ")

#2. Give the conditions:
def passwordValid(password):

    characters = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '/', ":", ";", '"', "'", '<', '>', '.', "?", ',']
    val = True

    if len(password) < 15: #a. Greater than 15 letters
      val = False

    if not any(char.isupper() for char in password): #b. Have at least one capital letter
      val =False

    if not any(char.isdigit() for char in password): #c. Have at least one number
      val =False 

    if not any(char in characters for char in password): #d. Have at least one special char (!@#$%^&*()_+ etc)
      val =False

    if val:
      return val

def main():
    if (passwordValid(password)):
        print("Welcome! Your password is valid.")
        print("\n\33[1m\33[34mWelcome! Your password is valid.\33[0m\U0001F601")

    else:
        print("Sorry, it seems like you entered an invalid password.")
        print("\nYour password must be gretater than 15 letters and contains at least one number, captail letter, and special characters")
        print("\n\33[1m\33[31mSorry, it seems like you entered an invalid password.\33[0m\U0001F600")
        print("It must be grater than \33[3m\33[1m\33[92m15 letters\33[0m and contains at least \33[3m\33[1m\33[92mone number\33[0m, \33[3m\33[1m\33[92mcapital letter\33[0m, and \33[3m\33[1m\33[92mspecial characters\33[0m.")

main()