import random
import string
import pyperclip


ask_length = int(input("What is your password length? (Minimum 8): "))
if ask_length >= 4:
    character_category = []
    # Here we are adding character category to an array for a later use of even distribution in round-robin method.
    yn_capital_letters = input("Include uppercase letters? (y/n): ")
    if yn_capital_letters == "y":
        character_category.append(list(string.ascii_uppercase))
        # string.ascii_uppercase gives uppercase letters and list converts into an array for categorisation.
    elif yn_capital_letters == "n":
        print("There will be no capital letters in password")
    yn_small_letters = input("Include lowercase letters? (y/n): ")
    if yn_small_letters == "y":
        character_category.append(list(string.ascii_lowercase))
        # string.ascii_lowercase gives lowercase letters and list converts into an array for categorisation.
    elif yn_small_letters == "n":
        print("There will be no small letters in password.")
    yn_numbers = input("Include numbers? (y/n): ")
    if yn_numbers == "y":
        character_category.append(list(string.digits))
        # string.digits gives numbers and list converts into an array for categorisation.
    elif yn_numbers == "n":
        print("There will be no numbers in password.")
    yn_symbols = input("Include symbols? (y/n): ")
    if yn_symbols == "y":
        character_category.append(list(string.punctuation))
        # string.punctuation gives punctuations and list converts into an array for categorisation.
    elif yn_symbols == "n":
        print("There will be no symbols in password.")
    if not character_category:
        # if no category selected this will print
        print("Select at least one character type.")
        exit()

    password = []

    while len(password) < ask_length:
        for category in character_category:
            # for loop will iterate every category like a round-robin method
            if len(password) < ask_length:
                # The if condition ensures that once the password reaches the desired length,
                # no more characters are added, even if the loop hasn't finished iterating over all categories.
                # This prevents adding extra characters and maintains the specified password length.
                password.append(random.choice(category))

    random.shuffle(password)
    final_password = "".join(password)
    print(f"Password {final_password} added to the clipboard.")
    pyperclip.copy(final_password)
    # this will copy the password to clipboard
else:
    print("This will be not a safe password, TRY AGAIN!")
