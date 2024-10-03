# if = do some code only if some condition is true
# It is not necessary to give else condition.

age = int(input("Enter your age : "))
if (age >=18):
  print("You can vote.")
elif (age<18):
  print("You cannot vote.")
else :
  print("Enter a valid age")

name = input("Enter your name : ")
if (name == ""):
  print("You did not type your name")
else :
  print(f"Hello {name}")
