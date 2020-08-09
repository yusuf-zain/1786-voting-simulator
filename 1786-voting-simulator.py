import sys
print("""""")
print("""Welcome to Voting Simulator 1786.
Before we can decide whether you could vote,
we will have to ask you some questions.
Please answer in a yes/no format (besides age).
""")
closing = """Thank you for playing!"""
landowner = (input("Do you own any land? ").lower())
if landowner == "no":
    print("""   You can't vote""")
    print(closing)
    sys.exit()
Ethnicity = (input("Are you Caucasion? ").lower())
if Ethnicity == "no":
    print(" You can't vote")
    print(closing)
    sys.exit()
gender = (input("Are you female? ").lower())
if gender == "yes":
    print(" You can't vote")
    print(closing)
    sys.exit()
age = (int(input("How old are you? ")))
if age < 21:
    print(" You can't vote")
    print(closing)
    sys.exit()
if age >= 21:
    print(" Congratulations! You are a part of the 20% of the population who could vote at that time!")
    print(closing)
sys.exit()
