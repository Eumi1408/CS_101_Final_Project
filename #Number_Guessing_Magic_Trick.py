#Number_Guessing_Magic_Trick

## Prework
final_number = 0
enter_continue = input("Press Enter to continue...")

def final_answer(answer):
    print("Is this correct? Type yes or no, then press enter.")
    if answer == "yes":
        print()

## Program
print("Welcome to this Python 3 Magic Session.")
print(input("Press Enter to begin..."))
print("""Please pick a number between 1 and 10.
Do NOT enter it at any point during the session and do not write it down. 
If you need to write it down, you can cover your webcam to make sure I don't cheat!
Get ready to perform a series of simple calculations over the next few steps.""")
print(enter_continue)
print("Add 6 to your number.")
final_number += 6
print(enter_continue)
print("Subtract 2.")
final_number -= 2
print(enter_continue)
print("Add 4.")
final_number += 4
print(enter_continue)
print("Subtract 3.")
final_number -= 3
print(enter_continue)
print("Add 1.")
final_number += 1
print(enter_continue)
print("Now, subtract your original number from the number you have calculated over these past few steps.")
print(enter_continue)
print("The number you are currently on is 6!")