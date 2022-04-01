## Number Guessing Magic Trick

## Global Variables
final_number = 0
enter_continue = input("Press Enter to continue...")
input_1 = input("""Choose a number between 1 and 10, let's call it 'a' and add it to the number you picked. 
Type 'a' here and press enter.""")
input_2 = input("""Choose a number between 1 and 10, let's call it 'b' and subtract it from the number you picked. 
Type 'b' here and press enter.""")
input_3 = input("""Choose a number between 1 and 10, let's call it 'c' and subtract it from the number you picked. 
Type 'c' here and press enter.""")
input_4 = input("""Choose a number between 1 and 10, let's call it 'd' and add it to the number you picked. 
Type 'd' here and press enter.""")
subtract_original_number = """Take the number you have calculated up to this point. 
Then, subtract your original number 'x' from this number. The result is your final number.
(like this: number - x = final number)."""
last_step = input("Press Enter to reveal my guess for your final number")

## Answer Function
def final_answer(answer):
    print(input("Is this correct? Type yes or no, then press enter."))
    if answer == "yes":
        print("""MUHAHA. I dare you to play again! Press Ctrl+L to start over.
        .-._                                                   _,-,
  `._`-._                                           _,-'_,'
     `._ `-._                                   _,-' _,'
        `._  `-._        __.-----.__        _,-'  _,'
           `._   `#==="""           """===#'   _,'
              `._/)  ._               _.  (\_,'
               )*'     **.__     __.**     '*( 
               #  .==..__  ""   ""  __..==,  # 
Deelkar        #   `"._(_).       .(_)_."'   # """)
    if answer == "no":
        print("Oops, something went wrong! Please play again and use a calculator. Press Ctrl+L to start over.")

## Program
print("Welcome to this Python 3 Magic Session.")
print(input("Press Enter to begin..."))
print("""Please pick a number between 1 and 20. Let's call it 'x'.
Keep it to yourself. Do NOT enter it at any point during the session. 
Get ready to perform a series of simple calculations over the next few steps.""")
print(enter_continue)
print(input_1)
final_number += input_1
print(input_2)
final_number -= input_2
print(input_3)
final_number += input_3
print(input_4)
final_number += input_4
print(subtract_original_number)
print(last_step)
print(final_number)
print(final_answer)
