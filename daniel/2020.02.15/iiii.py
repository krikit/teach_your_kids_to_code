driving_age = eval(input("What is the legal driving age where you live"))
your_age = eval(input("How old are you"))
if your_age >= driving_age:
    print("your are old enough to drive")
if your_age < driving_age:
    print("sorry, you can drive", driving_age - your_age, "years")
