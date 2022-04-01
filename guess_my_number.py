## Number Guessing Magic Trick

## Global Variables
final_number = 0
subtract_original_number = """Take the number you have calculated up to this point. 
Then, subtract your original number 'x' from this number. The result is your final number.
(like this: number - x = final number)."""

## Answer Function
def final_answer(answer):
    if answer == "yes":
        return """MUHAHA. I dare you to play again! Press Ctrl+L to clear your terminal. Then, type 'python number_guessing_magic_game.py' and press Enter.
        .-._                                                   _,-,
  `._`-._                                           _,-'_,'
     `._ `-._                                   _,-' _,'
        `._  `-._        __.-----.__        _,-'  _,'
           `._   `#==="""           """===#'   _,'
              `._/)  ._               _.  (\_,'
               )*'     **.__     __.**     '*( 
               #  .==..__  ""   ""  __..==,  # 
Deelkar        #   `"._(_).       .(_)_."'   # """
    if answer == "no":
        return """Oops, something went wrong! Please play again and use a calculator. Press Ctrl+L to clear your terminal. Then, type 'python number_guessing_magic_game.py' and press Enter."""

## Program
print("Welcome to this Python 3 Magic Session.")
input("Press Enter to begin...")
print("""Please pick a number between 1 and 20. Let's call it 'x'.
Keep it to yourself. Do NOT enter it at any point during the session. 
Get ready to perform a series of simple calculations over the next few steps.""")
input("Press Enter to continue...")
input_1 = input("""Choose a number between 1 and 10, let's call it 'a'. Add it to the number you picked. 
Type 'a' here and press enter. """)
final_number += int(input_1)
input_2 = input("""Choose a number between 1 and 10, let's call it 'b'. Subtract it from the number you picked. 
Type 'b' here and press enter. """)
final_number -= int(input_2)
input_3 = input("""Choose a number between 1 and 10, let's call it 'c'. Add it to the number you picked. 
Type 'c' here and press enter. """)
final_number += int(input_3)
input_4 = input("""Choose a number between 1 and 10, let's call it 'd'. Subtract it from the number you picked. 
Type 'd' here and press enter. """)
final_number -= int(input_4)
print(subtract_original_number)
input("Press Enter to continue...")
input("Press Enter to reveal my guess for your final number.")
print(final_number)
yes_no = input("Is this correct? Type yes or no, then press enter. ")
print(final_answer(yes_no))
