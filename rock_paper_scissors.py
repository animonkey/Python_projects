import random
user_option = int(input("Enter 1 for Rock, 2 for Paper and 3 for scissors:"))
if user_option == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user_option == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif user_option == 3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("error")
comp = random.randint(1,3)
print("-----------------------")
if comp == 1:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
elif comp == 2:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")  
else:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    
if user_option == 1 and comp == 1:
    print("You won!")
elif user_option == 1 and comp == 2:
    print("It's a tie!")
elif user_option == 1 and comp == 3:
    print("You lost!")
elif user_option == 2 and comp == 1:
    print("You lost!")
elif user_option == 2 and comp == 2:
    print("You won!")
elif user_option == 2 and comp == 3:
    print("It's a tie!")
elif user_option == 3 and comp == 1:
    print("It's a tie!")
elif user_option == 3 and comp == 2:
    print("You lost!")
elif user_option == 3 and comp == 3:
    print("You won!")
else:
    print("error")
