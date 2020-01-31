print("Mathhomework.py")
problem = input("Enter a math problem, or 'q' to quit: ")
while (problem != "q"):
    print("The answer to ", problem, "is:", eval(problem) )
    problem = input("Enter a math problem, or 'q' to quit: ")
