print("Hello!")

age_user = int(input("How old are you?: "))

def pay(earnings):
    if earnings > 10000:
        print("Congratulations, you are rich!")
    elif 10000 > earnings > 5000:
        print("You are just about average:")
    elif 5000 > earnings > 0:
        print("You are poor!")
    else:
        print("That is not possible!")
        pay(earnings = int(input("How much do you earn a month?: ")))

def test(age):
    if age >= 18:
        print("You are of a good age!")
        earnings_user = int(input("How much do you earn a month?: "))
        pay(earnings_user)
    elif age <= 0:
        print("Please enter a valid age.")
        test(age = int(input("How old are you?: ")))
    else:
        print("Sorry you cannot take this test.")


test(age_user)

# Cool
