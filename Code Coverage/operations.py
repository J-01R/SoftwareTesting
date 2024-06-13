#Jonatan Rassekhnia
#2023.04.23
#Lab 6 Code Coverage
#Karlstad University

import sys
def compute(a, b, t_operation):
    if operation == "subtract":
        return a - b
    if operation == "add":
        return a + b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b
    else:
        return 'Operation is not defined'

if __name__ == '__main__':

    input(compute(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))

print("Jonatan Rassekhnia")