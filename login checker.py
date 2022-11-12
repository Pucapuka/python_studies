#logIn function
def logIn():
  while True:
    userName = input("User Name: \033[32m")
    password = input("\033[33mPassword: \033[32m")
    if userName == 'paul' and password == 'myfavedude':
      print("\033[33mWELCOME TO REPLIT!!!")
      break
    else:
      print("\033[33mWhoa, Whoa, Whoa! Only authorised people can pass here. Back off!!!")
      continue

#Main Function

print ("\033[33mREPLIT LOGIN SYSTEM\n\n")

logIn()
