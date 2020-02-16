grade = eval(input("Enter your number grade (0-100): "))
if (grade > 100) or (grade < 0):
    print("Wrong number")
elif grade >= 90:
    print("You got an A! :) ")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D...")
else:
    print("You got an F. :( ")
